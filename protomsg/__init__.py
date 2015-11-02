
MESSAGE_TO_ID = {
    "UTCNotify": 10,
    "SyncRequest": 11,
    "SyncResponse": 12,
    "GetServerListRequest": 100,
    "GetServerListResponse": 101,
    "StartGameRequest": 102,
    "StartGameResponse": 103,
    "RegisterRequest": 200,
    "RegisterResponse": 201,
    "LoginRequest": 202,
    "LoginResponse": 203,
    "CharacterNotify": 300,
    "CreateCharacterRequest": 301,
    "CreateCharacterResponse": 302,
    "ClubNotify": 400,
    "CreateClubRequest": 401,
    "CreateClubResponse": 402,
    "ClubSetPolicyRequest": 410,
    "ClubSetPolicyResponse": 411,
    "ClubSetMatchStaffRequest": 412,
    "ClubSetMatchStaffResponse": 413,
    "StaffNotify": 500,
    "StaffRemoveNotify": 501,
    "StaffRecruitNotify": 520,
    "StaffRecruitRefreshRequest": 521,
    "StaffRecruitRefreshResponse": 522,
    "StaffRecruitRequest": 523,
    "StaffRecruitResponse": 524,
    "StaffFireRequest": 525,
    "StaffFireResponse": 526,
    "LeagueNotify": 600,
    "LeagueGetStatisticsRequest": 601,
    "LeagueGetStatisticsResponse": 602,
    "LeagueGetBattleLogRequest": 603,
    "LeagueGetBattleLogResponse": 604,
    "ChallengeNotify": 700,
    "ChallengeStartRequest": 701,
    "ChallengeStartResponse": 702,
    "BuildingNotify": 800,
    "BuildingLevelUpRequest": 801,
    "BuildingLevelUpResponse": 802,
    "TrainingExpSlotNotify": 900,
    "TrainingExpStartRequest": 901,
    "TrainingExpStartResponse": 902,
    "TrainingExpCancelRequest": 903,
    "TrainingExpCancelResponse": 904,
    "TrainingExpSpeedupRequest": 905,
    "TrainingExpSpeedupResponse": 906,
    "TrainingExpGetRewardRequest": 907,
    "TrainingExpGetRewardResponse": 908,
    "TrainingPropertyNotify": 920,
    "TrainingPropertyStartRequest": 921,
    "TrainingPropertyStartResponse": 922,
    "TrainingPropertyCancelRequest": 923,
    "TrainingPropertyCancelResponse": 924,
    "TrainingPropertySpeedupRequest": 925,
    "TrainingPropertySpeedupResponse": 926,
    "TrainingPropertyGetRewardRequest": 927,
    "TrainingPropertyGetRewardResponse": 928,
    "TrainingBroadcastNotify": 930,
    "TrainingBroadcastStartRequest": 931,
    "TrainingBroadcastStartResponse": 932,
    "TrainingBroadcastCancelRequest": 933,
    "TrainingBroadcastCancelResponse": 934,
    "TrainingBroadcastSpeedupRequest": 935,
    "TrainingBroadcastSpeedupResponse": 936,
    "TrainingBroadcastGetRewardRequest": 937,
    "TrainingBroadcastGetRewardResponse": 938,
    "TrainingShopNotify": 940,
    "TrainingShopStartRequest": 941,
    "TrainingShopStartResponse": 942,
    "TrainingSponsorNotify": 950,
    "TrainingSponsorStartRequest": 951,
    "TrainingSponsorStartResponse": 952,
    "SkillNotify": 1000,
    "SkillLockToggleRequest": 1001,
    "SkillLockToggleResponse": 1002,
    "SkillWashRequest": 1003,
    "SkillWashResponse": 1004,
    "SkillUpgradeSpeedupRequest": 1005,
    "SkillUpgradeSpeedupResponse": 1006,
    "SkillUpgradeRequest": 1007,
    "SkillUpgradeResponse": 1008,
    "TaskNotify": 1100,
    "TaskAcquireRequest": 1101,
    "TaskAcquireResponse": 1102,
    "TaskGetRewardRequest": 1103,
    "TaskGetRewardResponse": 1104,
    "TaskDoingRequest": 1105,
    "TaskDoingResponse": 1106,
    "RandomEventDoneRequest": 1107,
    "RandomEventDoneResponse": 1108,
    "FriendNotify": 1200,
    "FriendRemoveNotify": 1201,
    "FriendGetInfoRequest": 1202,
    "FriendGetInfoResponse": 1203,
    "FriendAddRequest": 1204,
    "FriendAddResponse": 1205,
    "FriendRemoveRequest": 1206,
    "FriendRemoveResponse": 1207,
    "FriendMatchRequest": 1208,
    "FriendMatchResponse": 1209,
    "FriendAcceptRequest": 1210,
    "FriendAcceptResponse": 1211,
    "MailNotify": 1300,
    "MailRemoveNotify": 1301,
    "MailSendRequest": 1302,
    "MailSendResponse": 1303,
    "MailOpenRequest": 1304,
    "MailOpenResponse": 1305,
    "MailDeleteRequest": 1306,
    "MailDeleteResponse": 1307,
    "MailGetAttachmentRequest": 1308,
    "MailGetAttachmentResponse": 1309,
    "ChatNotify": 1400,
    "ChatSendRequest": 1401,
    "ChatSendResponse": 1402,
    "NotificationNotify": 1500,
    "NotificationOpenRequest": 1501,
    "NotificationOpenResponse": 1502,
    "NotificationRemoveNotify": 1503,
    "NotificationDeleteRequest": 1504,
    "NotificationDeleteResponse": 1505,
    "FinanceStatisticsNotify": 1600,
    "LadderNotify": 1700,
    "LadderRefreshRequest": 1701,
    "LadderRefreshResponse": 1702,
    "LadderMatchRequest": 1703,
    "LadderMatchResponse": 1704,
    "LadderStoreNotify": 1705,
    "LadderStoreBuyRequest": 1706,
    "LadderStoreBuyResponse": 1707,
    "LadderLeaderBoardRequest": 1708,
    "LadderLeaderBoardResponse": 1709,
    "LadderStoreRefreshRequest": 1710,
    "LadderStoreRefreshResponse": 1711,
    "CupInfomationRequest": 1800,
    "CupInfomationResponse": 1801,
    "CupJoinRequest": 1802,
    "CupJoinResponse": 1803,
    "SponsorNotify": 1900,
    "SponsorRequest": 1903,
    "SponsorResponse": 1904,
    "SponsorGetIncomeRequest": 1905,
    "SponsorGetIncomeResponse": 1906,
    "ActivityCategoryNotify": 2000,
    "ActivitySignInNotify": 2001,
    "ActivitySignInRequest": 2002,
    "ActivitySignInResponse": 2003,
    "ActivityLoginRewardNotify": 2004,
    "ActivityLoginRewardRequest": 2005,
    "ActivityLoginRewardResponse": 2006,
    "ActiveValueNotify": 2100,
    "ActiveFunctionNotify": 2101,
    "ActiveValueGetRewardRequest": 2102,
    "ActiveValueGetRewardResponse": 2103,
    "TrainingSkillItemNotify": 2200,
    "TrainingSkillItemRemoveNotify": 2201,
    "ItemNotify": 2202,
    "ItemRemoveNotify": 2203,
}

ID_TO_MESSAGE = {
    10: "UTCNotify",
    11: "SyncRequest",
    12: "SyncResponse",
    100: "GetServerListRequest",
    101: "GetServerListResponse",
    102: "StartGameRequest",
    103: "StartGameResponse",
    200: "RegisterRequest",
    201: "RegisterResponse",
    202: "LoginRequest",
    203: "LoginResponse",
    300: "CharacterNotify",
    301: "CreateCharacterRequest",
    302: "CreateCharacterResponse",
    400: "ClubNotify",
    401: "CreateClubRequest",
    402: "CreateClubResponse",
    410: "ClubSetPolicyRequest",
    411: "ClubSetPolicyResponse",
    412: "ClubSetMatchStaffRequest",
    413: "ClubSetMatchStaffResponse",
    500: "StaffNotify",
    501: "StaffRemoveNotify",
    520: "StaffRecruitNotify",
    521: "StaffRecruitRefreshRequest",
    522: "StaffRecruitRefreshResponse",
    523: "StaffRecruitRequest",
    524: "StaffRecruitResponse",
    525: "StaffFireRequest",
    526: "StaffFireResponse",
    600: "LeagueNotify",
    601: "LeagueGetStatisticsRequest",
    602: "LeagueGetStatisticsResponse",
    603: "LeagueGetBattleLogRequest",
    604: "LeagueGetBattleLogResponse",
    700: "ChallengeNotify",
    701: "ChallengeStartRequest",
    702: "ChallengeStartResponse",
    800: "BuildingNotify",
    801: "BuildingLevelUpRequest",
    802: "BuildingLevelUpResponse",
    900: "TrainingExpSlotNotify",
    901: "TrainingExpStartRequest",
    902: "TrainingExpStartResponse",
    903: "TrainingExpCancelRequest",
    904: "TrainingExpCancelResponse",
    905: "TrainingExpSpeedupRequest",
    906: "TrainingExpSpeedupResponse",
    907: "TrainingExpGetRewardRequest",
    908: "TrainingExpGetRewardResponse",
    920: "TrainingPropertyNotify",
    921: "TrainingPropertyStartRequest",
    922: "TrainingPropertyStartResponse",
    923: "TrainingPropertyCancelRequest",
    924: "TrainingPropertyCancelResponse",
    925: "TrainingPropertySpeedupRequest",
    926: "TrainingPropertySpeedupResponse",
    927: "TrainingPropertyGetRewardRequest",
    928: "TrainingPropertyGetRewardResponse",
    930: "TrainingBroadcastNotify",
    931: "TrainingBroadcastStartRequest",
    932: "TrainingBroadcastStartResponse",
    933: "TrainingBroadcastCancelRequest",
    934: "TrainingBroadcastCancelResponse",
    935: "TrainingBroadcastSpeedupRequest",
    936: "TrainingBroadcastSpeedupResponse",
    937: "TrainingBroadcastGetRewardRequest",
    938: "TrainingBroadcastGetRewardResponse",
    940: "TrainingShopNotify",
    941: "TrainingShopStartRequest",
    942: "TrainingShopStartResponse",
    950: "TrainingSponsorNotify",
    951: "TrainingSponsorStartRequest",
    952: "TrainingSponsorStartResponse",
    1000: "SkillNotify",
    1001: "SkillLockToggleRequest",
    1002: "SkillLockToggleResponse",
    1003: "SkillWashRequest",
    1004: "SkillWashResponse",
    1005: "SkillUpgradeSpeedupRequest",
    1006: "SkillUpgradeSpeedupResponse",
    1007: "SkillUpgradeRequest",
    1008: "SkillUpgradeResponse",
    1100: "TaskNotify",
    1101: "TaskAcquireRequest",
    1102: "TaskAcquireResponse",
    1103: "TaskGetRewardRequest",
    1104: "TaskGetRewardResponse",
    1105: "TaskDoingRequest",
    1106: "TaskDoingResponse",
    1107: "RandomEventDoneRequest",
    1108: "RandomEventDoneResponse",
    1200: "FriendNotify",
    1201: "FriendRemoveNotify",
    1202: "FriendGetInfoRequest",
    1203: "FriendGetInfoResponse",
    1204: "FriendAddRequest",
    1205: "FriendAddResponse",
    1206: "FriendRemoveRequest",
    1207: "FriendRemoveResponse",
    1208: "FriendMatchRequest",
    1209: "FriendMatchResponse",
    1210: "FriendAcceptRequest",
    1211: "FriendAcceptResponse",
    1300: "MailNotify",
    1301: "MailRemoveNotify",
    1302: "MailSendRequest",
    1303: "MailSendResponse",
    1304: "MailOpenRequest",
    1305: "MailOpenResponse",
    1306: "MailDeleteRequest",
    1307: "MailDeleteResponse",
    1308: "MailGetAttachmentRequest",
    1309: "MailGetAttachmentResponse",
    1400: "ChatNotify",
    1401: "ChatSendRequest",
    1402: "ChatSendResponse",
    1500: "NotificationNotify",
    1501: "NotificationOpenRequest",
    1502: "NotificationOpenResponse",
    1503: "NotificationRemoveNotify",
    1504: "NotificationDeleteRequest",
    1505: "NotificationDeleteResponse",
    1600: "FinanceStatisticsNotify",
    1700: "LadderNotify",
    1701: "LadderRefreshRequest",
    1702: "LadderRefreshResponse",
    1703: "LadderMatchRequest",
    1704: "LadderMatchResponse",
    1705: "LadderStoreNotify",
    1706: "LadderStoreBuyRequest",
    1707: "LadderStoreBuyResponse",
    1708: "LadderLeaderBoardRequest",
    1709: "LadderLeaderBoardResponse",
    1710: "LadderStoreRefreshRequest",
    1711: "LadderStoreRefreshResponse",
    1800: "CupInfomationRequest",
    1801: "CupInfomationResponse",
    1802: "CupJoinRequest",
    1803: "CupJoinResponse",
    1900: "SponsorNotify",
    1903: "SponsorRequest",
    1904: "SponsorResponse",
    1905: "SponsorGetIncomeRequest",
    1906: "SponsorGetIncomeResponse",
    2000: "ActivityCategoryNotify",
    2001: "ActivitySignInNotify",
    2002: "ActivitySignInRequest",
    2003: "ActivitySignInResponse",
    2004: "ActivityLoginRewardNotify",
    2005: "ActivityLoginRewardRequest",
    2006: "ActivityLoginRewardResponse",
    2100: "ActiveValueNotify",
    2101: "ActiveFunctionNotify",
    2102: "ActiveValueGetRewardRequest",
    2103: "ActiveValueGetRewardResponse",
    2200: "TrainingSkillItemNotify",
    2201: "TrainingSkillItemRemoveNotify",
    2202: "ItemNotify",
    2203: "ItemRemoveNotify",
}

PATH_TO_REQUEST = {
    "/game/sync/": ["common", "SyncRequest"],
    "/game/servers/": ["server", "GetServerListRequest"],
    "/game/start/": ["server", "StartGameRequest"],
    "/game/account/register/": ["account", "RegisterRequest"],
    "/game/account/login/": ["account", "LoginRequest"],
    "/game/character/create/": ["character", "CreateCharacterRequest"],
    "/game/club/create/": ["club", "CreateClubRequest"],
    "/game/club/policy/": ["club", "ClubSetPolicyRequest"],
    "/game/club/matchstaff/": ["club", "ClubSetMatchStaffRequest"],
    "/game/staff/recruit/refresh/": ["staff", "StaffRecruitRefreshRequest"],
    "/game/staff/recruit/": ["staff", "StaffRecruitRequest"],
    "/game/staff/fire/": ["staff", "StaffFireRequest"],
    "/game/league/statistics/": ["league", "LeagueGetStatisticsRequest"],
    "/game/league/log/": ["league", "LeagueGetBattleLogRequest"],
    "/game/challenge/start/": ["challenge", "ChallengeStartRequest"],
    "/game/building/levelup/": ["building", "BuildingLevelUpRequest"],
    "/game/training/exp/start/": ["training", "TrainingExpStartRequest"],
    "/game/training/exp/cancel/": ["training", "TrainingExpCancelRequest"],
    "/game/training/exp/speedup/": ["training", "TrainingExpSpeedupRequest"],
    "/game/training/exp/getreward/": ["training", "TrainingExpGetRewardRequest"],
    "/game/training/property/start/": ["training", "TrainingPropertyStartRequest"],
    "/game/training/property/cancel/": ["training", "TrainingPropertyCancelRequest"],
    "/game/training/property/speedup/": ["training", "TrainingPropertySpeedupRequest"],
    "/game/training/property/getreward/": ["training", "TrainingPropertyGetRewardRequest"],
    "/game/training/broadcast/start/": ["training", "TrainingBroadcastStartRequest"],
    "/game/training/broadcast/cancel/": ["training", "TrainingBroadcastCancelRequest"],
    "/game/training/broadcast/speedup/": ["training", "TrainingBroadcastSpeedupRequest"],
    "/game/training/broadcast/getreward/": ["training", "TrainingBroadcastGetRewardRequest"],
    "/game/training/shop/start/": ["training", "TrainingShopStartRequest"],
    "/game/training/sponsor/start/": ["training", "TrainingSponsorStartRequest"],
    "/game/skill/locktoggle/": ["skill", "SkillLockToggleRequest"],
    "/game/skill/wash/": ["skill", "SkillWashRequest"],
    "/game/skill/upgrade/speedup/": ["skill", "SkillUpgradeSpeedupRequest"],
    "/game/skill/upgrade/": ["skill", "SkillUpgradeRequest"],
    "/game/task/acquire/": ["task", "TaskAcquireRequest"],
    "/game/task/getreward/": ["task", "TaskGetRewardRequest"],
    "/game/task/doing/": ["task", "TaskDoingRequest"],
    "/game/randomevent/done/": ["task", "RandomEventDoneRequest"],
    "/game/friend/info/": ["friend", "FriendGetInfoRequest"],
    "/game/friend/add/": ["friend", "FriendAddRequest"],
    "/game/friend/remove/": ["friend", "FriendRemoveRequest"],
    "/game/friend/match/": ["friend", "FriendMatchRequest"],
    "/game/friend/accept/": ["friend", "FriendAcceptRequest"],
    "/game/mail/send/": ["mail", "MailSendRequest"],
    "/game/mail/open/": ["mail", "MailOpenRequest"],
    "/game/mail/delete/": ["mail", "MailDeleteRequest"],
    "/game/mail/getattachment/": ["mail", "MailGetAttachmentRequest"],
    "/game/chat/send/": ["chat", "ChatSendRequest"],
    "/game/notification/open/": ["notification", "NotificationOpenRequest"],
    "/game/notification/delete/": ["notification", "NotificationDeleteRequest"],
    "/game/ladder/refresh/": ["ladder", "LadderRefreshRequest"],
    "/game/ladder/match/": ["ladder", "LadderMatchRequest"],
    "/game/ladder/store/buy/": ["ladder", "LadderStoreBuyRequest"],
    "/game/ladder/leaderboard/": ["ladder", "LadderLeaderBoardRequest"],
    "/game/ladder/store/refresh/": ["ladder", "LadderStoreRefreshRequest"],
    "/game/cup/infomation/": ["cup", "CupInfomationRequest"],
    "/game/cup/join/": ["cup", "CupJoinRequest"],
    "/game/sponsor/": ["spread", "SponsorRequest"],
    "/game/sponsor/getincome/": ["spread", "SponsorGetIncomeRequest"],
    "/game/signin/": ["activity", "ActivitySignInRequest"],
    "/game/activity/loginreward/": ["activity", "ActivityLoginRewardRequest"],
    "/game/activevalue/getreward/": ["active_value", "ActiveValueGetRewardRequest"],
}

PATH_TO_RESPONSE = {
    "/game/sync/": ["common", "SyncResponse"],
    "/game/servers/": ["server", "GetServerListResponse"],
    "/game/start/": ["server", "StartGameResponse"],
    "/game/account/register/": ["account", "RegisterResponse"],
    "/game/account/login/": ["account", "LoginResponse"],
    "/game/character/create/": ["character", "CreateCharacterResponse"],
    "/game/club/create/": ["club", "CreateClubResponse"],
    "/game/club/policy/": ["club", "ClubSetPolicyResponse"],
    "/game/club/matchstaff/": ["club", "ClubSetMatchStaffResponse"],
    "/game/staff/recruit/refresh/": ["staff", "StaffRecruitRefreshResponse"],
    "/game/staff/recruit/": ["staff", "StaffRecruitResponse"],
    "/game/staff/fire/": ["staff", "StaffFireResponse"],
    "/game/league/statistics/": ["league", "LeagueGetStatisticsResponse"],
    "/game/league/log/": ["league", "LeagueGetBattleLogResponse"],
    "/game/challenge/start/": ["challenge", "ChallengeStartResponse"],
    "/game/building/levelup/": ["building", "BuildingLevelUpResponse"],
    "/game/training/exp/start/": ["training", "TrainingExpStartResponse"],
    "/game/training/exp/cancel/": ["training", "TrainingExpCancelResponse"],
    "/game/training/exp/speedup/": ["training", "TrainingExpSpeedupResponse"],
    "/game/training/exp/getreward/": ["training", "TrainingExpGetRewardResponse"],
    "/game/training/property/start/": ["training", "TrainingPropertyStartResponse"],
    "/game/training/property/cancel/": ["training", "TrainingPropertyCancelResponse"],
    "/game/training/property/speedup/": ["training", "TrainingPropertySpeedupResponse"],
    "/game/training/property/getreward/": ["training", "TrainingPropertyGetRewardResponse"],
    "/game/training/broadcast/start/": ["training", "TrainingBroadcastStartResponse"],
    "/game/training/broadcast/cancel/": ["training", "TrainingBroadcastCancelResponse"],
    "/game/training/broadcast/speedup/": ["training", "TrainingBroadcastSpeedupResponse"],
    "/game/training/broadcast/getreward/": ["training", "TrainingBroadcastGetRewardResponse"],
    "/game/training/shop/start/": ["training", "TrainingShopStartResponse"],
    "/game/training/sponsor/start/": ["training", "TrainingSponsorStartResponse"],
    "/game/skill/locktoggle/": ["skill", "SkillLockToggleResponse"],
    "/game/skill/wash/": ["skill", "SkillWashResponse"],
    "/game/skill/upgrade/speedup/": ["skill", "SkillUpgradeSpeedupResponse"],
    "/game/skill/upgrade/": ["skill", "SkillUpgradeResponse"],
    "/game/task/acquire/": ["task", "TaskAcquireResponse"],
    "/game/task/getreward/": ["task", "TaskGetRewardResponse"],
    "/game/task/doing/": ["task", "TaskDoingResponse"],
    "/game/randomevent/done/": ["task", "RandomEventDoneResponse"],
    "/game/friend/info/": ["friend", "FriendGetInfoResponse"],
    "/game/friend/add/": ["friend", "FriendAddResponse"],
    "/game/friend/remove/": ["friend", "FriendRemoveResponse"],
    "/game/friend/match/": ["friend", "FriendMatchResponse"],
    "/game/friend/accept/": ["friend", "FriendAcceptResponse"],
    "/game/mail/send/": ["mail", "MailSendResponse"],
    "/game/mail/open/": ["mail", "MailOpenResponse"],
    "/game/mail/delete/": ["mail", "MailDeleteResponse"],
    "/game/mail/getattachment/": ["mail", "MailGetAttachmentResponse"],
    "/game/chat/send/": ["chat", "ChatSendResponse"],
    "/game/notification/open/": ["notification", "NotificationOpenResponse"],
    "/game/notification/delete/": ["notification", "NotificationDeleteResponse"],
    "/game/ladder/refresh/": ["ladder", "LadderRefreshResponse"],
    "/game/ladder/match/": ["ladder", "LadderMatchResponse"],
    "/game/ladder/store/buy/": ["ladder", "LadderStoreBuyResponse"],
    "/game/ladder/leaderboard/": ["ladder", "LadderLeaderBoardResponse"],
    "/game/ladder/store/refresh/": ["ladder", "LadderStoreRefreshResponse"],
    "/game/cup/infomation/": ["cup", "CupInfomationResponse"],
    "/game/cup/join/": ["cup", "CupJoinResponse"],
    "/game/sponsor/": ["spread", "SponsorResponse"],
    "/game/sponsor/getincome/": ["spread", "SponsorGetIncomeResponse"],
    "/game/signin/": ["activity", "ActivitySignInResponse"],
    "/game/activity/loginreward/": ["activity", "ActivityLoginRewardResponse"],
    "/game/activevalue/getreward/": ["active_value", "ActiveValueGetRewardResponse"],
}
