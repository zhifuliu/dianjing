# -*- coding: utf-8 -*-
"""
Author:         Ouyang_Yibei <said047@163.com>
Filename:       task
Date Created:   2015-07-28 11:20
Description:

"""
from utils.http import ProtobufResponse
from core.task import TaskManage

from protomsg.task_pb2 import TaskAcquireResponse, TaskGetRewardResponse

def receive(request):
    task_id = request._proto.id
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    task = TaskManage(server_id, char_id)
    task.receive(task_id)

    response = TaskAcquireResponse()
    response.ret = 0
    return ProtobufResponse(response)


def reward(request):
    task_id = request._proto.id
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    task = TaskManage(server_id, char_id)
    task.get_reward(task_id)

    response = TaskGetRewardResponse()
    response.ret = 0
    return ProtobufResponse(response)
