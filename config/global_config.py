# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       global_config
Date Created:   2016-03-11 11-00
Description:

"""

from config.base import ConfigBase


class _global_config(object):
    __slots__ = ['id', 'value', 'value_string']

    def __init__(self):
        self.id = ''
        self.value = 0
        self.value_string = ''


class GlobalConfig(ConfigBase):
    EntityClass = _global_config
    INSTANCES = {}
    FILTER_CACHE = {}

    @classmethod
    def value(cls, _id):
        """

        :rtype: int
        """
        return cls.INSTANCES[_id].value

    @classmethod
    def value_string(cls, _id):
        return cls.INSTANCES[_id].value_string
