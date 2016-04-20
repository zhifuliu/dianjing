# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       __init__
Date Created:   2015-04-23 23:09
Description:

"""

import os
import sys
import json
import zipfile

from config.global_config import GlobalConfig
from config.errormsg import ConfigErrorMessage
from config.staff import ConfigStaffHot, ConfigStaffRecruit, ConfigStaffNew, ConfigStaffStar, ConfigStaffLevelNew, ConfigStaffEquipmentLevelAddition, ConfigStaffEquipmentQualityAddition, ConfigStaffEquipmentAddition
from config.challenge import ConfigChallengeMatch, ConfigChapter
from config.unit import ConfigUnitNew, ConfigUnitUnLock, ConfigUnitStepAddition, ConfigUnitLevelAddition, ConfigUnitAddition
from config.building import ConfigBuilding
from config.package import ConfigPackage
from config.item import ConfigItemNew, ConfigItemUse, ConfigItemMerge, ConfigEquipmentNew, ConfigItemExp
from config.npc import ConfigNPC
from config.skill import ConfigTalentSkill
from config.task import ConfigTask, ConfigRandomEvent, ConfigTaskTargetType
from config.club import ConfigClubLevel, ConfigClubFlag
from config.ladder import ConfigLadderRankReward, ConfigLadderScoreStore
from config.qianban import ConfigQianBan
from config.league import ConfigLeague
from config.activity import ConfigActivityCategory
from config.signin import ConfigSignIn
from config.activity_login_reward import ConfigLoginReward
from config.active_value import ConfigActiveFunction, ConfigActiveReward
from config.training_match import ConfigTrainingMatchReward, ConfigTrainingMatchStore
from config.talent import ConfigTalent

_has_configed = False


def load_config():
    from django.conf import settings
    from apps.config.models import Config as ModelConfig

    global _has_configed
    if _has_configed:
        return

    _has_configed = True

    if settings.TEST:
        z_file = os.path.join(settings.BASE_DIR, 'config', 'config.zip')
    else:
        c = ModelConfig.get_config()
        if c:
            z_file = c.config.path
        else:
            z_file = os.path.join(settings.BASE_DIR, 'config', 'config.zip')

    z = zipfile.ZipFile(z_file)
    for item in z.namelist():
        content = z.open(item).read()
        if not content:
            continue

        data = json.loads(content)

        if item == 'global_config.json':
            GlobalConfig.initialize(data)
        elif item == 'errormsg.json':
            ConfigErrorMessage.initialize(data)
        elif item == 'item_new.json':
            ConfigItemNew.initialize(data)
        elif item == 'item_use.json':
            ConfigItemUse.initialize(data)
        elif item == 'item_merge.json':
            ConfigItemMerge.initialize(data)
        elif item == 'equipment_new.json':
            ConfigEquipmentNew.initialize(data)
        elif item == 'item_exp.json':
            ConfigItemExp.initialize(data)
        elif item == 'staff_new.json':
            ConfigStaffNew.initialize(data)
        elif item == 'staff_level_new.json':
            ConfigStaffLevelNew.initialize(data)
        elif item == 'staff_star.json':
            ConfigStaffStar.initialize(data)
        elif item == 'staff_equip_level_addition.json':
            ConfigStaffEquipmentLevelAddition.initialize(data)
        elif item == 'staff_equip_quality_addition.json':
            ConfigStaffEquipmentQualityAddition.initialize(data)
        elif item == 'staff_hot.json':
            ConfigStaffHot.initialize(data)
        elif item == 'staff_recruit.json':
            ConfigStaffRecruit.initialize(data)
        elif item == 'challenge_chapter.json':
            ConfigChapter.initialize(data)
        elif item == 'challenge_match.json':
            ConfigChallengeMatch.initialize(data)
        elif item == 'unit_new.json':
            ConfigUnitNew.initialize(data)
        elif item == 'unit_unlock.json':
            ConfigUnitUnLock.initialize(data)
        elif item == 'unit_level_addition.json':
            ConfigUnitLevelAddition.initialize(data)
        elif item == 'unit_step_addition.json':
            ConfigUnitStepAddition.initialize(data)
        elif item == 'building.json':
            ConfigBuilding.initialize(data)
        elif item == 'package.json':
            ConfigPackage.initialize(data)
        elif item == 'npc_club.json':
            ConfigNPC.initialize(data)
        elif item == 'npc_club_name.json':
            ConfigNPC.initialize_club_names(data)
        elif item == 'npc_manager_name.json':
            ConfigNPC.initialize_manager_name(data)
        elif item == 'talent_skill.json':
            ConfigTalentSkill.initialize(data)
        elif item == 'task.json':
            ConfigTask.initialize(data)
        elif item == 'random_event.json':
            ConfigRandomEvent.initialize(data)
        elif item == 'club_level.json':
            ConfigClubLevel.initialize(data)
        elif item == 'club_flag.json':
            ConfigClubFlag.initialize(data)
        elif item == 'ladder_rank_reward.json':
            ConfigLadderRankReward.initialize(data)
        elif item == 'ladder_score_store.json':
            ConfigLadderScoreStore.initialize(data)
        elif item == 'qianban.json':
            ConfigQianBan.initialize(data)
        elif item == 'league.json':
            ConfigLeague.initialize(data)
        elif item == 'activity_category.json':
            ConfigActivityCategory.initialize(data)
        elif item == 'activity_signin.json':
            ConfigSignIn.initialize(data)
        elif item == 'activity_login_reward.json':
            ConfigLoginReward.initialize(data)
        elif item == 'active_function.json':
            ConfigActiveFunction.initialize(data)
        elif item == 'active_reward.json':
            ConfigActiveReward.initialize(data)
        elif item == 'task_target.json':
            ConfigTaskTargetType.initialize(data)
        elif item == 'training_match_reward.json':
            ConfigTrainingMatchReward.initialize(data)
        elif item == 'training_match_store.json':
            ConfigTrainingMatchStore.initialize(data)
        elif item == 'talent.json':
            ConfigTalent.initialize(data)


    sys.stderr.write("LOAD CONFIG FROM {0}\n".format(z_file))
