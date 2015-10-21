# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       bag
Date Created:   2015-10-21 14:48
Description:

"""
from contextlib import contextmanager

from dianjing.exception import GameException

from core.mongo import MongoBag

from utils.message import MessagePipe

from config import ConfigTrainingSkillItem, ConfigItem, ConfigErrorMessage

from protomsg.common_pb2 import ACT_UPDATE, ACT_INIT
from protomsg.bag_pb2 import (
    TrainingSkillItemNotify,
    TrainingSkillItemRemoveNotify,
    ItemNotify,
    ItemRemoveNotify,
)


class BagBase(object):
    MONGODB_FIELD_NAME = None
    ERROR_NAME_NOT_EXIST = None
    ERROR_NAME_NOT_ENOUGH = None

    CONFIG = None

    MSG_NOTIFY = None
    MSG_REMOVE_NOTIFY = None

    def __init__(self, server_id, char_id):
        self.server_id = server_id
        self.char_id = char_id

        if not MongoBag.exist(self.server_id, self.char_id):
            doc = MongoBag.document()
            doc['_id'] = self.char_id
            MongoBag.db(self.server_id).insert_one(doc)

    def has(self, ids):
        if not isinstance(ids, (list, tuple)):
            ids = [ids]

        projection = {'{0}.{1}'.format(self.MONGODB_FIELD_NAME, i): 1 for i in ids}
        doc = MongoBag.db(self.server_id).find_one(
            {'_id': self.char_id},
            projection
        )

        for i in ids:
            if not doc[self.MONGODB_FIELD_NAME].get(str(i), 0):
                return False

        return True

    def add(self, items):
        # items = [(id, amount)...]

        items_dict = {}
        for _id, _amount in items:
            items_dict[_id] = items_dict.get(_id, 0) + _amount

        ids = items_dict.keys()
        for i in ids:
            if not self.CONFIG.get(i):
                raise GameException(ConfigErrorMessage.get_error_id(self.ERROR_NAME_NOT_EXIST))

        updater = {'{0}.{1}'.format(self.MONGODB_FIELD_NAME, _id): _amount for _id, _amount in items_dict.iteritems()}
        MongoBag.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$inc': updater}
        )

        self.send_notify(ids=ids)

    def _remove_check(self, _id, amount):
        doc = MongoBag.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'{0}.{1}'.format(self.MONGODB_FIELD_NAME, _id): 1}
        )

        original_amount = doc[self.MONGODB_FIELD_NAME].get(str(_id), 0)
        if not original_amount:
            raise GameException(ConfigErrorMessage.get(self.ERROR_NAME_NOT_EXIST))

        new_amount = original_amount - amount
        if new_amount < 0:
            raise GameException(ConfigErrorMessage.get(self.ERROR_NAME_NOT_ENOUGH))

        return new_amount

    def _remove_done(self, _id, new_amount):
        if new_amount == 0:
            MongoBag.db(self.server_id).update_one(
                {'_id': self.char_id},
                {'$unset': {
                    '{0}.{1}'.format(self.MONGODB_FIELD_NAME, _id): 1
                }}
            )

            self.send_remove_notify([_id])
        else:
            MongoBag.db(self.server_id).update_one(
                {'_id': self.char_id},
                {'$set': {
                    '{0}.{1}'.format(self.MONGODB_FIELD_NAME, _id): new_amount
                }}
            )
            self.send_notify(ids=[_id])

    def remove(self, _id, amount=1):
        new_amount = self._remove_check(_id, amount)
        self._remove_done(_id, new_amount)

    @contextmanager
    def remove_context(self, _id, amount=1):
        new_amount = self._remove_check(_id, amount)
        yield
        self._remove_done(_id, new_amount)

    def send_remove_notify(self, ids):
        notify = self.MSG_REMOVE_NOTIFY()
        notify.ids.extend(ids)
        MessagePipe(self.char_id).put(msg=notify)

    def send_notify(self, ids=None):
        if ids:
            projection = {'{0}.{1}'.format(self.MONGODB_FIELD_NAME, i): 1 for i in ids}
            act = ACT_UPDATE
        else:
            projection = {self.MONGODB_FIELD_NAME: 1}
            act = ACT_INIT

        doc = MongoBag.db(self.server_id).find_one(
            {'_id': self.char_id},
            projection
        )

        notify = self.MSG_NOTIFY()
        notify.act = act
        for _id, _amount in doc[self.MONGODB_FIELD_NAME].iteritems():
            notify_item = notify.items.add()
            notify_item.id = int(_id)
            notify_item.amount = _amount

        MessagePipe(self.char_id).put(msg=notify)


class BagTrainingSkill(BagBase):
    MONGODB_FIELD_NAME = 'training_skills'
    ERROR_NAME_NOT_EXIST = "TRAINING_SKILL_NOT_EXIST"
    ERROR_NAME_NOT_ENOUGH = "TRAINING_SKILL_NOT_ENOUGH"

    CONFIG = ConfigTrainingSkillItem

    MSG_NOTIFY = TrainingSkillItemNotify
    MSG_REMOVE_NOTIFY = TrainingSkillItemRemoveNotify


class BagItem(BagBase):
    MONGODB_FIELD_NAME = 'items'
    ERROR_NAME_NOT_EXIST = "ITEM_NOT_EXIST"
    ERROR_NAME_NOT_ENOUGH = "ITEM_NOT_ENOUGH"

    CONFIG = ConfigItem

    MSG_NOTIFY = ItemNotify
    MSG_REMOVE_NOTIFY = ItemRemoveNotify