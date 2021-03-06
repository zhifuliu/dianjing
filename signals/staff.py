# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       staff
Date Created:   2016-05-27 15-24
Description:

"""

from django.dispatch import receiver
from core.signals import (
    staff_new_add_signal,
    recruit_staff_diamond_signal,
    staff_star_up_signal,
    staff_step_up_signal,
)

from core.collection import Collection
from core.system import BroadCast

from config import ConfigItemNew

@receiver(staff_new_add_signal, dispatch_uid='signals.staff.staff_new_add_handler')
def staff_new_add_handler(server_id, char_id, staffs_info, force_load_staffs, **kwargs):
    oids = [o for o, _ in staffs_info]
    Collection(server_id, char_id).add(oids, force_load_staffs=force_load_staffs)


@receiver(recruit_staff_diamond_signal, dispatch_uid='signals.staff.recruit_diamond')
def recruit_staff_diamond_handler(server_id, char_id, times, staffs, **kwargs):
    b = BroadCast(server_id, char_id)
    for _sid, _amount in staffs:
        if ConfigItemNew.get(_sid).sub_tp == 1:
            b.cast_diamond_recruit_staff_notify(_sid)


@receiver(staff_star_up_signal, dispatch_uid='signals.staff.star_up_handler')
def star_up_handler(server_id, char_id, staff_id, staff_oid, new_star, **kwargs):
    major, minor = divmod(new_star, 10)
    if minor == 0:
        b = BroadCast(server_id, char_id)
        b.cast_staff_star_up_notify(staff_oid, major)

@receiver(staff_step_up_signal, dispatch_uid='signals.staff.step_up_handler')
def step_up_handler(server_id, char_id, staff_id, staff_oid, new_step, **kwargs):
    if new_step > 3:
        b = BroadCast(server_id, char_id)
        b.cast_staff_step_up_notify(staff_oid, new_step)