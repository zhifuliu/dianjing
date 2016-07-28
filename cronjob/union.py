# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       union
Date Created:   2016-07-28 10:50
Description:

"""

import traceback

import uwsgidecorators
from apps.server.models import Server
from core.mongo import MongoUnionMember
from cronjob.log import Logger

@uwsgidecorators.cron(0, 0, -1, -1, -1, target="spooler")
def reset_union_today_contribution(*args):
    logger = Logger("reset_union_today_contribution")
    logger.write("Start")

    try:
        for sid in Server.opened_server_ids():
            MongoUnionMember.db(sid).update_many(
                {},
                {'$set': {
                    'today_contribution': 0
                }}
            )

            logger.write("Server {0} Finish".format(sid))
    except:
        logger.error(traceback.format_exc())
    else:
        logger.write("Done")
    finally:
        logger.close()