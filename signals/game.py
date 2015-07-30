# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       game
Date Created:   2015-04-30 15:23
Description:

"""

import arrow

from core.signals import game_start_signal
from core.character import Character
from core.club import Club
from core.staff import StaffRecruit, StaffManger
from core.skill import SkillManager
from core.challenge import Challenge
from core.building import BuildingManager
from core.training import Training
from core.league import League
from core.friend import FriendManager



from utils.message import MessagePipe
from protomsg.common_pb2 import UTCNotify


def start(server_id, char_id, **kwargs):
    MessagePipe(char_id).clean()

    msg = UTCNotify()
    msg.timestamp = arrow.utcnow().timestamp
    MessagePipe(char_id).put(msg=msg)

    Character(server_id, char_id).send_notify()

    Club(server_id, char_id).send_notify()
    StaffRecruit(server_id, char_id).send_notify()
    StaffManger(server_id, char_id).send_notify()
    SkillManager(server_id, char_id).send_notify()

    Challenge(server_id, char_id).send_notify()
    BuildingManager(server_id, char_id).send_notify()
    Training(server_id, char_id).send_notify()
    League(server_id, char_id).send_notify()
    FriendManager(server_id, char_id).send_notify()


game_start_signal.connect(
    start,
    dispatch_uid='signals.game.start'
)
