# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       club
Date Created:   2015-07-08 15:12
Description:

"""

from django.db import IntegrityError

from dianjing.exception import GameException
from apps.character.models import Character as ModelCharacter

from utils.http import ProtobufResponse
from config import ConfigErrorMessage

from core.signals import game_start_signal
from core.character import Character
from core.club import Club

from protomsg.club_pb2 import (
    CreateClubResponse,
    ClubSetPolicyResponse,
    ClubSetMatchStaffResponse,
    ClubStaffSlotBuyResponse,
    ClubSetUnitResponse,
    ClubSetFormationResponse,
)


def create(request):
    name = request._proto.name
    flag = request._proto.flag

    session = request._game_session
    server_id = session.server_id
    char_id = session.char_id

    char = ModelCharacter.objects.get(id=char_id)
    if char.club_name:
        raise GameException(ConfigErrorMessage.get_error_id("CLUB_ALREADY_CREATED"))

    try:
        char.club_name = name
        char.save()
    except IntegrityError:
        raise GameException(ConfigErrorMessage.get_error_id("CLUB_NAME_TAKEN"))

    Character.create(server_id, char_id, char.name, name, flag)

    game_start_signal.send(
        sender=None,
        server_id=server_id,
        char_id=char_id,
    )

    response = CreateClubResponse()
    response.ret = 0
    response.session = session.serialize()
    return ProtobufResponse(response)


def set_policy(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id
    policy = request._proto.policy_id

    club = Club(server_id, char_id)
    club.set_policy(policy)

    response = ClubSetPolicyResponse()
    response.ret = 0
    return ProtobufResponse(response)


def set_match_staffs(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id
    staff_ids = [i for i in  request._proto.staff_ids]

    club = Club(server_id, char_id)
    club.set_match_staffs(staff_ids)

    response = ClubSetMatchStaffResponse()
    response.ret = 0
    return ProtobufResponse(response)


def set_unit(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id
    index = request._proto.index
    staff_id = request._proto.staff_id
    unit_id = request._proto.unit_id

    club = Club(server_id, char_id)
    club.set_unit(index, staff_id, unit_id)

    response = ClubSetUnitResponse()
    response.ret = 0
    return ProtobufResponse(response)


def set_formation(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    formation = []
    for info in request._proto.position:
        formation.append((info.staff_id, info.position))

    club = Club(server_id, char_id)
    club.set_formation(formation)

    response = ClubSetFormationResponse()
    response.ret = 0
    return ProtobufResponse(response)


def buy_slots(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    club = Club(server_id, char_id)
    club.buy_slot()

    response = ClubStaffSlotBuyResponse()
    response.ret = 0
    return ProtobufResponse(response)
