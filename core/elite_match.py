# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       elite_match
Date Created:   2015-12-10 11:35
Description:

"""

import arrow

from dianjing.exception import GameException

from core.mongo import MongoEliteMatch, MongoCharacter
from core.abstract import AbstractClub, AbstractStaff
from core.club import Club
from core.match import ClubMatch
from core.package import Drop
from core.resource import Resource
from core.character import Character
from core.staff import StaffManger
from core.challenge import Challenge

from utils.message import MessagePipe

from config import ConfigEliteArea, ConfigEliteMatch, ConfigErrorMessage, ConfigStaff

from protomsg.common_pb2 import ACT_INIT, ACT_UPDATE
from protomsg.elite_match_pb2 import (
    EliteNotify
)


ELITE_MATCH_COST = 5


class EliteNPCStaff(AbstractStaff):
    __slots__ = []

    def __init__(self, _id, level):
        super(EliteNPCStaff, self).__init__()

        self.id = _id
        self.level = level

        config = ConfigStaff.get(_id)
        self.race = config.race
        self.skills = {i: 1 for i in config.skill_ids}

        self.luoji = config.luoji
        self.minjie = config.minjie
        self.lilun = config.lilun
        self.wuxing = config.wuxing
        self.meili = config.meili

        self.calculate_secondary_property()


class EliteNPCClub(AbstractClub):
    __slots__ = []

    def __init__(self, elite_match_id):
        super(EliteNPCClub, self).__init__()

        config = ConfigEliteMatch.get(elite_match_id)

        self.id = elite_match_id

        self.match_staffs = config.staffs
        self.policy = config.policy
        self.name = config.club_name
        self.flag = config.club_flag

        for i in self.match_staffs:
            self.staffs[i] = EliteNPCStaff(i, config.staff_level)

        self.qianban_affect()


def get_next_restore_timestamp():
    now = arrow.utcnow()
    next_hour = now.replace(hours=1)

    next_hour = arrow.Arrow(
        next_hour.year,
        next_hour.month,
        next_hour.day,
        next_hour.hour,
        0,
        0,
        0,
        tzinfo=next_hour.tzinfo
    )

    return next_hour.timestamp


class EliteMatch(object):
    __slots__ = ['server_id', 'char_id', 'cur_times']

    def __init__(self, server_id, char_id):
        self.server_id = server_id
        self.char_id = char_id

        doc = MongoEliteMatch.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'cur_times': 1}
        )

        if not doc:
            doc = MongoEliteMatch.document()
            doc['_id'] = self.char_id
            MongoEliteMatch.db(self.server_id).insert_one(doc)

    @classmethod
    def cronjob_clean_match_times(cls, server_id):
        """
        定时清除挑战次数
        """
        for char_id in Character.get_recent_login_char_ids(server_id):
            doc = MongoEliteMatch.db(server_id).find_one({'_id': char_id})

            updater = {}
            for area_id, area_info in doc['areas'].iteritems():
                for ch_id, ch_info in area_info['challenges']:
                    updater['areas.{0}.challenges.{1}.times'.format(area_id, ch_id)] = 0

            MongoEliteMatch.db(server_id).update_one(
                {'_id': char_id},
                {'$set': updater}
            )

    def refresh_challenge_times(self, area_id, challenge_id):
        MongoEliteMatch.db(self.server_id).update_one(
                {'_id': self.char_id},
                {'$set': {'areas.{0}.challenges.{1}.times'.format(area_id, challenge_id): 0}}
        )

        self.elite_notify(area_id=area_id)

    def open_area(self, aid):
        """
        开放精英赛大区
            这个函数由挑战赛大区通关后调用， 用来开启当前关卡精英赛
        """
        # 获取大区配置
        config = ConfigEliteArea.get(aid)
        if not config:
            raise GameException(ConfigErrorMessage.get_error_id("ELITE_CONFIG_NOT_EXIST"))

        # 获取玩家数据
        doc = MongoEliteMatch.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'areas.{0}'.format(aid): 1}
        )

        # 如果已经开启， 直接返回
        if str(aid) in doc['areas']:
            return

        # 未开启， 开启， 添加到 玩家数据库
        updater = {
            'areas.{0}'.format(aid): {
                'challenges': {
                    str(config.first_match_id()): {
                        'stars': 0,
                        'times': 0,
                    }
                },
                'packages': {
                    '1': True,
                    '2': True,
                    '3': True,
                }
            }
        }

        MongoEliteMatch.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$set': updater}
        )

        self.elite_notify(area_id=aid)

    def start(self, area_id, challenge_id):
        """
        开始精英赛关卡
        """
        # 判断大区是否存在
        if not ConfigEliteArea.get(area_id):
            raise GameException(ConfigErrorMessage.get_error_id("ELITE_CONFIG_NOT_EXIST"))

        # 获取玩家数据
        doc = MongoEliteMatch.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'areas.{0}.challenges.{1}'.format(area_id, challenge_id): 1}
        )

        # 判断大区是否已开启
        if not doc['areas'].get(str(area_id), {}):
            raise GameException(ConfigErrorMessage.get_error_id("ELITE_AREA_NOT_OPEN"))

        # 判断是否已开方关卡
        elite = doc['areas'][str(area_id)]['challenges'].get(str(challenge_id), {})
        if not elite:
            raise GameException(ConfigErrorMessage.get_error_id("ELITE_MATCH_NOT_OPEN"))

        # 挑战次数检查
        if elite.get('times', 0) >= ConfigEliteMatch.get(challenge_id).max_times:
            raise GameException(ConfigErrorMessage.get_error_id("ELITE_TOTAL_NO_TIMES"))

        # 体力检查
        doc_char = MongoCharacter.db(self.server_id).find_one({'_id': self.char_id}, {'energy': 1})
        if doc_char['energy']['power'] < ELITE_MATCH_COST:
            raise GameException(ConfigErrorMessage.get_error_id("CHALLENGE_NOT_ENOUGH_ENERGY"))

        # match
        club_one = Club(self.server_id, self.char_id)
        club_two = EliteNPCClub(challenge_id)
        match = ClubMatch(club_one, club_two)

        msg = match.start()
        msg.key = str(self.char_id) + ',' + str(area_id) + ',' + str(challenge_id)
        return msg

    def report(self, key, win_club, result):
        """
        精英赛结果汇报
        """
        # 解析key
        club_one, area_id, challenge_id = str(key).split(',')

        # 判断是否是用户自身比赛
        if club_one != str(self.char_id):
            raise GameException(ConfigErrorMessage.get_error_id("BAD_MESSAGE"))

        # 更新员工胜率
        StaffManger(self.server_id, self.char_id).update_winning_rate(result)

        ch = Challenge(self.server_id, self.char_id)
        # 扣除能量
        ch.change_energy(-ELITE_MATCH_COST)

        # 更新挑战次数
        updater = {'areas.{0}.challenges.{1}.times'.format(area_id, challenge_id): 1}
        MongoEliteMatch.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$inc': updater}
        )

        # 通关处理
        if win_club == club_one:
            counter = 0
            for r in result:
                if r.staff_one_win:
                    counter += 1

            if counter == 5:            # 3星
                stars = 3
            elif counter == 4:          # 2星
                stars = 2
            else:                       # 1星
                stars = 1
            doc = MongoEliteMatch.db(self.server_id).find_one(
                {'_id': self.char_id}, {'areas.{0}'.format(area_id): 1}
            )

            setter = {}
            # 判断是否需要更新星级
            if stars > doc['areas'][area_id]['challenges'].get(challenge_id, {}).get('stars', 0):
                setter['areas.{0}.challenges.{1}.stars'.format(area_id, challenge_id)] = stars

            next_challenge_id = int(challenge_id) + 1

            # 如果下一关存在
            if ConfigEliteMatch.get(next_challenge_id):
                # 如果当前大关的， 开启
                if ConfigEliteArea.get(int(area_id)).last_match_id() >= next_challenge_id:
                    setter['areas.{0}.challenges.{1}'.format(area_id, next_challenge_id)] = {'stars': 0,
                                                                                             'times': 0}
            # 更新数据
            if setter:
                MongoEliteMatch.db(self.server_id).update_one(
                    {'_id': self.char_id},
                    {'$set': setter}
                )

            # 同步到客户端
            self.elite_notify(area_id=area_id)

            # 通关奖励
            drop = Drop.generate(ConfigEliteMatch.get(int(challenge_id)).reward)
            Resource(self.server_id, self.char_id).save_drop(drop)
            return drop.make_protomsg()

        # # send signal
        # challenge_match_signal.send(
        #     sender=None,
        #     server_id=self.server_id,
        #     char_id=self.char_id,
        #     challenge_id=int(challenge_id),
        #     win=(win_club == club_one),
        # )

        return None

    def star_reward(self, area_id, index):
        """
        领取星级奖励
        """
        # 获取数据
        doc = MongoEliteMatch.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'areas.{0}.packages.{1}'.format(area_id, index+1): 1},
            {'areas.{0}.challenges'.format(area_id): 1},
        )

        # 判断是否有星级奖励（实际上是检测是否已开通大区）
        star_reward = doc['areas'].get(str(area_id), {}).get('packages', {})
        if not star_reward:
            raise GameException(ConfigErrorMessage.get_error_id("CHALLENGE_REWARD_NOT_EXIST"))

        # 已领取
        if not star_reward[str(index+1)]:
            raise GameException(ConfigErrorMessage.get_error_id("CHALLENGE_REWARD_HAVE_GET"))

        star_count = 0
        # 计算总星数
        for ch_id, ch_info in doc['areas'][str(area_id)]['challenges'].iteritems():
            star_count += ch_info['stars']

        conf = ConfigEliteArea.get(area_id)
        # 星数不足
        if conf.star_reward[index]['star'] > star_count:
            raise GameException(ConfigErrorMessage.get_error_id("CHALLENGE_REWARD_STARS_NOT_ENOUGH"))

        # 发放奖励
        drop = Drop.generate(conf.star_reward[index]['reward'])
        Resource(self.server_id, self.char_id).save_drop(drop)

        return drop.make_protomsg()

    def elite_notify(self, act=ACT_INIT, area_id=None):
        if area_id:
            projection = {'areas.{0}'.format(area_id): 1}
            act = ACT_UPDATE
        else:
            projection = {'areas': 1}

        doc = MongoEliteMatch.db(self.server_id).find_one({'_id': self.char_id}, projection)

        notify = EliteNotify()
        notify.act = act
        if doc['areas']:
            for k, v in doc['areas'].iteritems():
                notify_area = notify.area.add()
                notify_area.id = int(k)
                notify_area.package_one = v['packages']['1']
                notify_area.package_two = v['packages']['2']
                notify_area.package_three = v['packages']['3']

                for challenge_id, info in v['challenges'].iteritems():
                    notify_challenge = notify_area.challenge.add()
                    notify_challenge.id = int(challenge_id)
                    notify_challenge.times = info['times']
                    notify_challenge.stars = info['stars']
        else:
            notify_area = notify.area.add()
            notify_area.id = 1
            notify_area.package_one = True
            notify_area.package_two = True
            notify_area.package_three = True

        MessagePipe(self.char_id).put(msg=notify)
