
MESSAGE_TO_ID = {
    "UTCNotify": 10,
    "SyncRequest": 11,
    "SyncResponse": 12,
    "PingRequest": 13,
    "PingResponse": 14,
    "SocketServerNotify": 49,
    "SocketConnectRequest": 50,
    "SocketConnectResponse": 51,
    "GetServerListRequest": 100,
    "GetServerListResponse": 101,
    "StartGameRequest": 102,
    "StartGameResponse": 103,
    "RegisterRequest": 200,
    "RegisterResponse": 201,
    "LoginRequest": 202,
    "LoginResponse": 203,
    "ClubNotify": 400,
    "CreateClubRequest": 401,
    "CreateClubResponse": 402,
    "CreateDaysNotify": 403,
    "ClubLeaderBoardRequest": 404,
    "ClubLeaderBoardResponse": 405,
    "StaffNotify": 500,
    "StaffRemoveNotify": 501,
    "StaffRecruitNotify": 520,
    "StaffRecruitRequest": 523,
    "StaffRecruitResponse": 524,
    "StaffEquipChangeRequest": 530,
    "StaffEquipChangeResponse": 531,
    "StaffLevelUpRequest": 532,
    "StaffLevelUpResponse": 533,
    "staffStepUpRequest": 534,
    "StaffStepUpResponse": 535,
    "StaffStarUpRequest": 536,
    "StaffStarUpResponse": 537,
    "StaffDestroyRequest": 538,
    "StaffDestroyResponse": 539,
    "StaffBatchDestroyRequest": 540,
    "StaffBatchDestroyResponse": 541,
    "ChallengeNotify": 700,
    "ChallengeStartRequest": 702,
    "ChallengeStartResponse": 703,
    "ChapterGetStarRewardRequest": 704,
    "ChapterGetStarRewardResponse": 705,
    "ChallengeMatchReportRequest": 706,
    "ChallengeMatchReportResponse": 707,
    "ChallengeSweepRequest": 710,
    "ChallengeSweepResponse": 711,
    "ChapterNotify": 720,
    "ChallengeResetRequest": 721,
    "ChallengeResetResponse": 722,
    "TaskNotify": 1100,
    "TaskDailyNotify": 1110,
    "TaskDailyGetRewardRequest": 1111,
    "TaskDailyGetRewardResponse": 1112,
    "FriendNotify": 1200,
    "FriendRemoveNotify": 1201,
    "FriendGetInfoRequest": 1202,
    "FriendGetInfoResponse": 1203,
    "FriendAddRequest": 1204,
    "FriendAddResponse": 1205,
    "FriendRemoveRequest": 1206,
    "FriendRemoveResponse": 1207,
    "FriendAcceptRequest": 1210,
    "FriendAcceptResponse": 1211,
    "FriendCandidatesRequest": 1212,
    "FriendCandidatesResponse": 1213,
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
    "BroadcastNotify": 2800,
    "BagSlotsNotify": 3000,
    "BagSlotsRemoveNotify": 3001,
    "BagItemUseRequest": 3002,
    "BagItemUseResponse": 3003,
    "BagItemMergeRequest": 3004,
    "BagItemMergeResponse": 3005,
    "BagItemDestroyRequest": 3006,
    "BagItemDestroyResponse": 3007,
    "BagEquipmentLevelupRequest": 3010,
    "BagEquipmentLevelupResponse": 3011,
    "BagEquipmentDestroyRequest": 3012,
    "BagEquipmentDestroyResponse": 3013,
    "BagEquipmentBatchDestroyRequest": 3014,
    "BagEquipmentBatchDestroyResponse": 3015,
    "UnitNotify": 3100,
    "UnitLevelUpRequest": 3101,
    "UnitLevelUpResponse": 3102,
    "UnitStepUpRequest": 3103,
    "UnitStepUpResponse": 3104,
    "UnitDestroyRequest": 3105,
    "UnitDestroyResponse": 3106,
    "FormationNotify": 3200,
    "FormationSetStaffRequest": 3201,
    "FormationSetStaffResponse": 3202,
    "FormationSetUnitRequest": 3203,
    "FormationSetUnitResponse": 3204,
    "FormationActiveRequest": 3207,
    "FormationActiveResponse": 3208,
    "FormationLevelUpRequest": 3209,
    "FormationLevelUpResponse": 3210,
    "FormationUseRequest": 3211,
    "FormationUseResponse": 3212,
    "FormationSlotNotify": 3215,
    "TalentNotify": 3300,
    "TalentLevelUpRequest": 3301,
    "TalentLevelUpResponse": 3302,
    "TalentResetTalentRequest": 3303,
    "TalentResetTalentResponse": 3304,
    "DungeonNotify": 3400,
    "DungeonMatchRequest": 3401,
    "DungeonMatchResponse": 3402,
    "DungeonMatchReportRequest": 3403,
    "DungeonMatchReportResponse": 3404,
    "DungeonBuyTimesRequest": 3405,
    "DungeonBuyTimesResponse": 3406,
    "ArenaNotify": 3500,
    "ArenaRefreshRequest": 3501,
    "ArenaRefreshResponse": 3502,
    "ArenaLeaderBoardRequest": 3503,
    "ArenaLeaderBoardResponse": 3504,
    "ArenaHonorStatusNotify": 3505,
    "ArenaHonorGetRewardRequest": 3507,
    "ArenaHonorGetRewardResponse": 3508,
    "ArenaMatchStartReqeust": 3509,
    "ArenaMatchStartResponse": 3510,
    "ArenaMatchReportReqeust": 3511,
    "ArenaMatchReportResponse": 3512,
    "ArenaBuyTimesRequest": 3514,
    "ArenaBuyTimesResponse": 3515,
    "TowerNotify": 3600,
    "TowerMatchStartRequest": 3601,
    "TowerMatchStartResponse": 3602,
    "TowerMatchReportReqeust": 3603,
    "TowerMatchReportResponse": 3604,
    "TowerResetRequest": 3605,
    "TowerResetResponse": 3606,
    "TowerTurnTableRequest": 3609,
    "TowerTurnTableResponse": 3610,
    "TowerSweepRequest": 3611,
    "TowerSweepResponse": 3612,
    "TowerSweepFinishRequest": 3613,
    "TowerSweepFinishResponse": 3614,
    "TowerLeaderBoardRequest": 3615,
    "TowerLeaderBoardResponse": 3616,
    "TowerStarRewardNotify": 3617,
    "TowerStarGetRewardReqeust": 3618,
    "TowerStarGetRewardResponse": 3619,
    "TowerGoodsNotify": 3620,
    "TowerGoodsBuyRequest": 3621,
    "TowerGoodsBuyResponse": 3622,
    "TerritoryNotify": 3700,
    "TerritoryTrainingStartReqeust": 3703,
    "TerritoryTrainingStartResponse": 3704,
    "TerritoryTrainingGetRewardReqeust": 3705,
    "TerritoryTrainingGetRewardResponse": 3706,
    "TerritoryStoreNotify": 3710,
    "TerritoryStoreBuyRequest": 3711,
    "TerritoryStoreBuyResponse": 3712,
    "TerritoryFriendListRequest": 3713,
    "TerritoryFriendListResponse": 3714,
    "TerritoryFriendHelpRequest": 3717,
    "TerritoryFriendHelpResponse": 3718,
    "TerritoryMatchReportRequest": 3719,
    "TerritoryMatchReportResponse": 3720,
    "TerritoryInspireRequest": 3721,
    "TerritoryInspireResponse": 3722,
    "TerritoryFriendHelpRemainedTimesNotify": 3723,
    "TerritoryMatchStartRequest": 3724,
    "TerritoryMatchStartResponse": 3725,
    "StoreNotify": 3800,
    "StoreBuyRequest": 3801,
    "StoreBuyResponse": 3802,
    "StoreRefreshRequest": 3803,
    "StoreRefreshResponse": 3804,
    "StoreAutoRefreshRequest": 3805,
    "StoreAutoRefreshResponse": 3806,
    "VIPNotify": 3900,
    "VIPBuyRewardRequest": 3901,
    "VIPBuyRewardResponse": 3902,
    "CollectionNotify": 4000,
    "EnergyNotify": 4100,
    "EnergyBuyRequest": 4101,
    "EnergyBuyResponse": 4102,
    "WelfareSignInNotify": 4200,
    "WelfareNewPlayerNotify": 4201,
    "WelfareLevelRewardNotify": 4202,
    "WelfareEnergyRewardNotify": 4203,
    "WelfareSignInRequest": 4204,
    "WelfareSignInResponse": 4205,
    "WelfareNewPlayerGetRequest": 4206,
    "WelfareNewPlayerGetResponse": 4207,
    "WelfareLevelRewardGetRequest": 4208,
    "WelfareLevelRewardGetResponse": 4209,
    "WelfareEnergyRewardGetReqeust": 4210,
    "WelfareEnergyRewardGetResponse": 4211,
    "ResourceNotify": 4300,
    "UnionNotify": 4400,
    "UnionCreateRequest": 4401,
    "UnionCreateResponse": 4402,
    "UnionSetBulletinRequest": 4403,
    "UnionSetBulletinResponse": 4404,
    "UnionListRequest": 4405,
    "UnionListResponse": 4406,
    "UnionApplyRequest": 4407,
    "UnionApplyResponse": 4408,
    "UnionAgreeRequest": 4409,
    "UnionAgreeResponse": 4410,
    "UnionRefuseRequest": 4411,
    "UnionRefuseResponse": 4412,
    "UnionKickRequest": 4413,
    "UnionKickResponse": 4414,
    "UnionTransferRequest": 4415,
    "UnionTransferResponse": 4416,
    "UnionQuitRequest": 4417,
    "UnionQuitResponse": 4418,
    "UnionMyAppliedNotify": 4419,
    "UnionMyCheckNotify": 4420,
    "UnionSigninRequest": 4421,
    "UnionSigninResponse": 4422,
    "PurchaseVerifyRequest": 4502,
    "PurchaseVerifyResponse": 4503,
    "PurchaseNotify": 4504,
    "PurchaseGetFirstRewardRequest": 4505,
    "PurchaseGetFirstRewardResponse": 4506,
    "ActivityNewPlayerNotify": 4600,
    "ActivityNewPlayerDailyBuyNotify": 4601,
    "ActivityNewPlayerGetRewardRequest": 4602,
    "ActivityNewPlayerGetRewardResponse": 4603,
    "ActivityNewPlayerDailyBuyRequest": 4604,
    "ActivityNewPlayerDailyBuyResponse": 4605,
    "PlunderFormationNotify": 4700,
    "PlunderFormationSetStaffRequest": 4701,
    "PlunderFormationSetStaffResponse": 4702,
    "PlunderFormationSetUnitRequest": 4703,
    "PlunderFormationSetUnitResponse": 4704,
    "PlunderSearchNotify": 4705,
    "PlunderSearchRequest": 4706,
    "PlunderSearchResponse": 4707,
    "PlunderSpyRequest": 4708,
    "PlunderSpyResponse": 4709,
    "PlunderTimesNotify": 4710,
    "PlunderStartRequest": 4711,
    "PlunderStartResponse": 4722,
    "PlunderReportRequest": 4723,
    "PlunderReportResponse": 4724,
    "PlunderRevengeNotify": 4725,
    "BaseStationNotify": 4726,
    "PlunderResultNotify": 4728,
    "PlunderGetRewardRequest": 4729,
    "PlunderGetRewardResponse": 4730,
    "BaseStationSyncRequest": 4731,
    "BaseStationSyncResponse": 4732,
    "PlunderBuyTimesRequest": 4733,
    "PlunderBuyTimesResponse": 4734,
    "BaseStationGetProductRequest": 4735,
    "BaseStationGetProductResponse": 4736,
    "SpecialEquipmentGenerateNotify": 4750,
    "SpecialEquipmentGenerateRequest": 4751,
    "SpecialEquipmentGenerateResponse": 4752,
    "SpecialEquipmentGenerateSpeedUpRequest": 4753,
    "SpecialEquipmentGenerateSpeedUpResponse": 4754,
    "SpecialEquipmentGetRequest": 4755,
    "SpecialEquipmentGetResponse": 4756,
    "PlunderDailyRewardNotify": 4757,
    "PlunderDailyRewardGetRequest": 4758,
    "PlunderDailyRewardGetResponse": 4759,
    "PartyInfoNotify": 4800,
    "PartyMessageNotify": 4801,
    "PartyRoomRequest": 4802,
    "PartyRoomResponse": 4803,
    "PartyCreateRequest": 4804,
    "PartyCreateResponse": 4805,
    "PartyJoinRequest": 4806,
    "PartyJoinResponse": 4807,
    "PartyQuitRequest": 4808,
    "PartyQuitResponse": 4809,
    "PartyKickRequest": 4810,
    "PartyKickResponse": 4811,
    "PartyChatRequest": 4812,
    "PartyChatResponse": 4813,
    "PartyBuyRequest": 4814,
    "PartyBuyResponse": 4815,
    "PartyStartRequest": 4816,
    "PartyStartResponse": 4817,
    "PartyDismissRequest": 4818,
    "PartyDismissResponse": 4819,
    "PartyNotify": 4820,
    "InspireNotify": 4900,
    "InspireSetStaffRequest": 4901,
    "InspireSetStaffResponse": 4902,
    "ChampionFormationNotify": 5000,
    "ChampionFormationSetStaffRequest": 5001,
    "ChampionFormationSetStaffResponse": 5002,
    "ChampionFormationSetUnitRequest": 5003,
    "ChampionFormationSetUnitResponse": 5004,
    "ChampionFormationSetPositionRequest": 5005,
    "ChampionFormationSetPositionResponse": 5006,
    "ChampionGroupNotify": 5008,
    "ChampionLevelNotify": 5009,
    "ChampionApplyRequest": 5010,
    "ChampionApplyResponse": 5011,
    "ChampionBetRequest": 5012,
    "ChampionBetResponse": 5013,
    "ChampionNotify": 5014,
    "ChampionGroupSyncRequest": 5015,
    "ChampionGroupSyncResponse": 5016,
    "ChampionLevelSyncRequest": 5017,
    "ChampionLevelSyncResponse": 5018,
}

ID_TO_MESSAGE = {
    10: "UTCNotify",
    11: "SyncRequest",
    12: "SyncResponse",
    13: "PingRequest",
    14: "PingResponse",
    49: "SocketServerNotify",
    50: "SocketConnectRequest",
    51: "SocketConnectResponse",
    100: "GetServerListRequest",
    101: "GetServerListResponse",
    102: "StartGameRequest",
    103: "StartGameResponse",
    200: "RegisterRequest",
    201: "RegisterResponse",
    202: "LoginRequest",
    203: "LoginResponse",
    400: "ClubNotify",
    401: "CreateClubRequest",
    402: "CreateClubResponse",
    403: "CreateDaysNotify",
    404: "ClubLeaderBoardRequest",
    405: "ClubLeaderBoardResponse",
    500: "StaffNotify",
    501: "StaffRemoveNotify",
    520: "StaffRecruitNotify",
    523: "StaffRecruitRequest",
    524: "StaffRecruitResponse",
    530: "StaffEquipChangeRequest",
    531: "StaffEquipChangeResponse",
    532: "StaffLevelUpRequest",
    533: "StaffLevelUpResponse",
    534: "staffStepUpRequest",
    535: "StaffStepUpResponse",
    536: "StaffStarUpRequest",
    537: "StaffStarUpResponse",
    538: "StaffDestroyRequest",
    539: "StaffDestroyResponse",
    540: "StaffBatchDestroyRequest",
    541: "StaffBatchDestroyResponse",
    700: "ChallengeNotify",
    702: "ChallengeStartRequest",
    703: "ChallengeStartResponse",
    704: "ChapterGetStarRewardRequest",
    705: "ChapterGetStarRewardResponse",
    706: "ChallengeMatchReportRequest",
    707: "ChallengeMatchReportResponse",
    710: "ChallengeSweepRequest",
    711: "ChallengeSweepResponse",
    720: "ChapterNotify",
    721: "ChallengeResetRequest",
    722: "ChallengeResetResponse",
    1100: "TaskNotify",
    1110: "TaskDailyNotify",
    1111: "TaskDailyGetRewardRequest",
    1112: "TaskDailyGetRewardResponse",
    1200: "FriendNotify",
    1201: "FriendRemoveNotify",
    1202: "FriendGetInfoRequest",
    1203: "FriendGetInfoResponse",
    1204: "FriendAddRequest",
    1205: "FriendAddResponse",
    1206: "FriendRemoveRequest",
    1207: "FriendRemoveResponse",
    1210: "FriendAcceptRequest",
    1211: "FriendAcceptResponse",
    1212: "FriendCandidatesRequest",
    1213: "FriendCandidatesResponse",
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
    2800: "BroadcastNotify",
    3000: "BagSlotsNotify",
    3001: "BagSlotsRemoveNotify",
    3002: "BagItemUseRequest",
    3003: "BagItemUseResponse",
    3004: "BagItemMergeRequest",
    3005: "BagItemMergeResponse",
    3006: "BagItemDestroyRequest",
    3007: "BagItemDestroyResponse",
    3010: "BagEquipmentLevelupRequest",
    3011: "BagEquipmentLevelupResponse",
    3012: "BagEquipmentDestroyRequest",
    3013: "BagEquipmentDestroyResponse",
    3014: "BagEquipmentBatchDestroyRequest",
    3015: "BagEquipmentBatchDestroyResponse",
    3100: "UnitNotify",
    3101: "UnitLevelUpRequest",
    3102: "UnitLevelUpResponse",
    3103: "UnitStepUpRequest",
    3104: "UnitStepUpResponse",
    3105: "UnitDestroyRequest",
    3106: "UnitDestroyResponse",
    3200: "FormationNotify",
    3201: "FormationSetStaffRequest",
    3202: "FormationSetStaffResponse",
    3203: "FormationSetUnitRequest",
    3204: "FormationSetUnitResponse",
    3207: "FormationActiveRequest",
    3208: "FormationActiveResponse",
    3209: "FormationLevelUpRequest",
    3210: "FormationLevelUpResponse",
    3211: "FormationUseRequest",
    3212: "FormationUseResponse",
    3215: "FormationSlotNotify",
    3300: "TalentNotify",
    3301: "TalentLevelUpRequest",
    3302: "TalentLevelUpResponse",
    3303: "TalentResetTalentRequest",
    3304: "TalentResetTalentResponse",
    3400: "DungeonNotify",
    3401: "DungeonMatchRequest",
    3402: "DungeonMatchResponse",
    3403: "DungeonMatchReportRequest",
    3404: "DungeonMatchReportResponse",
    3405: "DungeonBuyTimesRequest",
    3406: "DungeonBuyTimesResponse",
    3500: "ArenaNotify",
    3501: "ArenaRefreshRequest",
    3502: "ArenaRefreshResponse",
    3503: "ArenaLeaderBoardRequest",
    3504: "ArenaLeaderBoardResponse",
    3505: "ArenaHonorStatusNotify",
    3507: "ArenaHonorGetRewardRequest",
    3508: "ArenaHonorGetRewardResponse",
    3509: "ArenaMatchStartReqeust",
    3510: "ArenaMatchStartResponse",
    3511: "ArenaMatchReportReqeust",
    3512: "ArenaMatchReportResponse",
    3514: "ArenaBuyTimesRequest",
    3515: "ArenaBuyTimesResponse",
    3600: "TowerNotify",
    3601: "TowerMatchStartRequest",
    3602: "TowerMatchStartResponse",
    3603: "TowerMatchReportReqeust",
    3604: "TowerMatchReportResponse",
    3605: "TowerResetRequest",
    3606: "TowerResetResponse",
    3609: "TowerTurnTableRequest",
    3610: "TowerTurnTableResponse",
    3611: "TowerSweepRequest",
    3612: "TowerSweepResponse",
    3613: "TowerSweepFinishRequest",
    3614: "TowerSweepFinishResponse",
    3615: "TowerLeaderBoardRequest",
    3616: "TowerLeaderBoardResponse",
    3617: "TowerStarRewardNotify",
    3618: "TowerStarGetRewardReqeust",
    3619: "TowerStarGetRewardResponse",
    3620: "TowerGoodsNotify",
    3621: "TowerGoodsBuyRequest",
    3622: "TowerGoodsBuyResponse",
    3700: "TerritoryNotify",
    3703: "TerritoryTrainingStartReqeust",
    3704: "TerritoryTrainingStartResponse",
    3705: "TerritoryTrainingGetRewardReqeust",
    3706: "TerritoryTrainingGetRewardResponse",
    3710: "TerritoryStoreNotify",
    3711: "TerritoryStoreBuyRequest",
    3712: "TerritoryStoreBuyResponse",
    3713: "TerritoryFriendListRequest",
    3714: "TerritoryFriendListResponse",
    3717: "TerritoryFriendHelpRequest",
    3718: "TerritoryFriendHelpResponse",
    3719: "TerritoryMatchReportRequest",
    3720: "TerritoryMatchReportResponse",
    3721: "TerritoryInspireRequest",
    3722: "TerritoryInspireResponse",
    3723: "TerritoryFriendHelpRemainedTimesNotify",
    3724: "TerritoryMatchStartRequest",
    3725: "TerritoryMatchStartResponse",
    3800: "StoreNotify",
    3801: "StoreBuyRequest",
    3802: "StoreBuyResponse",
    3803: "StoreRefreshRequest",
    3804: "StoreRefreshResponse",
    3805: "StoreAutoRefreshRequest",
    3806: "StoreAutoRefreshResponse",
    3900: "VIPNotify",
    3901: "VIPBuyRewardRequest",
    3902: "VIPBuyRewardResponse",
    4000: "CollectionNotify",
    4100: "EnergyNotify",
    4101: "EnergyBuyRequest",
    4102: "EnergyBuyResponse",
    4200: "WelfareSignInNotify",
    4201: "WelfareNewPlayerNotify",
    4202: "WelfareLevelRewardNotify",
    4203: "WelfareEnergyRewardNotify",
    4204: "WelfareSignInRequest",
    4205: "WelfareSignInResponse",
    4206: "WelfareNewPlayerGetRequest",
    4207: "WelfareNewPlayerGetResponse",
    4208: "WelfareLevelRewardGetRequest",
    4209: "WelfareLevelRewardGetResponse",
    4210: "WelfareEnergyRewardGetReqeust",
    4211: "WelfareEnergyRewardGetResponse",
    4300: "ResourceNotify",
    4400: "UnionNotify",
    4401: "UnionCreateRequest",
    4402: "UnionCreateResponse",
    4403: "UnionSetBulletinRequest",
    4404: "UnionSetBulletinResponse",
    4405: "UnionListRequest",
    4406: "UnionListResponse",
    4407: "UnionApplyRequest",
    4408: "UnionApplyResponse",
    4409: "UnionAgreeRequest",
    4410: "UnionAgreeResponse",
    4411: "UnionRefuseRequest",
    4412: "UnionRefuseResponse",
    4413: "UnionKickRequest",
    4414: "UnionKickResponse",
    4415: "UnionTransferRequest",
    4416: "UnionTransferResponse",
    4417: "UnionQuitRequest",
    4418: "UnionQuitResponse",
    4419: "UnionMyAppliedNotify",
    4420: "UnionMyCheckNotify",
    4421: "UnionSigninRequest",
    4422: "UnionSigninResponse",
    4502: "PurchaseVerifyRequest",
    4503: "PurchaseVerifyResponse",
    4504: "PurchaseNotify",
    4505: "PurchaseGetFirstRewardRequest",
    4506: "PurchaseGetFirstRewardResponse",
    4600: "ActivityNewPlayerNotify",
    4601: "ActivityNewPlayerDailyBuyNotify",
    4602: "ActivityNewPlayerGetRewardRequest",
    4603: "ActivityNewPlayerGetRewardResponse",
    4604: "ActivityNewPlayerDailyBuyRequest",
    4605: "ActivityNewPlayerDailyBuyResponse",
    4700: "PlunderFormationNotify",
    4701: "PlunderFormationSetStaffRequest",
    4702: "PlunderFormationSetStaffResponse",
    4703: "PlunderFormationSetUnitRequest",
    4704: "PlunderFormationSetUnitResponse",
    4705: "PlunderSearchNotify",
    4706: "PlunderSearchRequest",
    4707: "PlunderSearchResponse",
    4708: "PlunderSpyRequest",
    4709: "PlunderSpyResponse",
    4710: "PlunderTimesNotify",
    4711: "PlunderStartRequest",
    4722: "PlunderStartResponse",
    4723: "PlunderReportRequest",
    4724: "PlunderReportResponse",
    4725: "PlunderRevengeNotify",
    4726: "BaseStationNotify",
    4728: "PlunderResultNotify",
    4729: "PlunderGetRewardRequest",
    4730: "PlunderGetRewardResponse",
    4731: "BaseStationSyncRequest",
    4732: "BaseStationSyncResponse",
    4733: "PlunderBuyTimesRequest",
    4734: "PlunderBuyTimesResponse",
    4735: "BaseStationGetProductRequest",
    4736: "BaseStationGetProductResponse",
    4750: "SpecialEquipmentGenerateNotify",
    4751: "SpecialEquipmentGenerateRequest",
    4752: "SpecialEquipmentGenerateResponse",
    4753: "SpecialEquipmentGenerateSpeedUpRequest",
    4754: "SpecialEquipmentGenerateSpeedUpResponse",
    4755: "SpecialEquipmentGetRequest",
    4756: "SpecialEquipmentGetResponse",
    4757: "PlunderDailyRewardNotify",
    4758: "PlunderDailyRewardGetRequest",
    4759: "PlunderDailyRewardGetResponse",
    4800: "PartyInfoNotify",
    4801: "PartyMessageNotify",
    4802: "PartyRoomRequest",
    4803: "PartyRoomResponse",
    4804: "PartyCreateRequest",
    4805: "PartyCreateResponse",
    4806: "PartyJoinRequest",
    4807: "PartyJoinResponse",
    4808: "PartyQuitRequest",
    4809: "PartyQuitResponse",
    4810: "PartyKickRequest",
    4811: "PartyKickResponse",
    4812: "PartyChatRequest",
    4813: "PartyChatResponse",
    4814: "PartyBuyRequest",
    4815: "PartyBuyResponse",
    4816: "PartyStartRequest",
    4817: "PartyStartResponse",
    4818: "PartyDismissRequest",
    4819: "PartyDismissResponse",
    4820: "PartyNotify",
    4900: "InspireNotify",
    4901: "InspireSetStaffRequest",
    4902: "InspireSetStaffResponse",
    5000: "ChampionFormationNotify",
    5001: "ChampionFormationSetStaffRequest",
    5002: "ChampionFormationSetStaffResponse",
    5003: "ChampionFormationSetUnitRequest",
    5004: "ChampionFormationSetUnitResponse",
    5005: "ChampionFormationSetPositionRequest",
    5006: "ChampionFormationSetPositionResponse",
    5008: "ChampionGroupNotify",
    5009: "ChampionLevelNotify",
    5010: "ChampionApplyRequest",
    5011: "ChampionApplyResponse",
    5012: "ChampionBetRequest",
    5013: "ChampionBetResponse",
    5014: "ChampionNotify",
    5015: "ChampionGroupSyncRequest",
    5016: "ChampionGroupSyncResponse",
    5017: "ChampionLevelSyncRequest",
    5018: "ChampionLevelSyncResponse",
}

PATH_TO_REQUEST = {
    "/game/sync/": ["common", "SyncRequest"],
    "/game/ping/": ["common", "PingRequest"],
    "/game/servers/": ["server", "GetServerListRequest"],
    "/game/start/": ["server", "StartGameRequest"],
    "/game/account/register/": ["account", "RegisterRequest"],
    "/game/account/login/": ["account", "LoginRequest"],
    "/game/club/create/": ["club", "CreateClubRequest"],
    "/game/club/leaderboard/": ["club", "ClubLeaderBoardRequest"],
    "/game/staff/recruit/": ["staff", "StaffRecruitRequest"],
    "/game/staff/equipchange/": ["staff", "StaffEquipChangeRequest"],
    "/game/staff/levelup/": ["staff", "StaffLevelUpRequest"],
    "/game/staff/stepup/": ["staff", "staffStepUpRequest"],
    "/game/staff/starup/": ["staff", "StaffStarUpRequest"],
    "/game/staff/destroy/": ["staff", "StaffDestroyRequest"],
    "/game/staff/batchdestroy/": ["staff", "StaffBatchDestroyRequest"],
    "/game/challenge/start/": ["challenge", "ChallengeStartRequest"],
    "/game/challenge/chapter/reward/": ["challenge", "ChapterGetStarRewardRequest"],
    "/game/challenge/report/": ["challenge", "ChallengeMatchReportRequest"],
    "/game/challenge/sweep/": ["challenge", "ChallengeSweepRequest"],
    "/game/challenge/reset/": ["challenge", "ChallengeResetRequest"],
    "/game/taskdaily/getreward/": ["task", "TaskDailyGetRewardRequest"],
    "/game/friend/info/": ["friend", "FriendGetInfoRequest"],
    "/game/friend/add/": ["friend", "FriendAddRequest"],
    "/game/friend/remove/": ["friend", "FriendRemoveRequest"],
    "/game/friend/accept/": ["friend", "FriendAcceptRequest"],
    "/game/friend/candidates/": ["friend", "FriendCandidatesRequest"],
    "/game/mail/send/": ["mail", "MailSendRequest"],
    "/game/mail/open/": ["mail", "MailOpenRequest"],
    "/game/mail/delete/": ["mail", "MailDeleteRequest"],
    "/game/mail/getattachment/": ["mail", "MailGetAttachmentRequest"],
    "/game/chat/send/": ["chat", "ChatSendRequest"],
    "/game/notification/open/": ["notification", "NotificationOpenRequest"],
    "/game/notification/delete/": ["notification", "NotificationDeleteRequest"],
    "/game/bagitem/use/": ["bag", "BagItemUseRequest"],
    "/game/bagitem/merge/": ["bag", "BagItemMergeRequest"],
    "/game/bagitem/destroy/": ["bag", "BagItemDestroyRequest"],
    "/game/bagequipment/levelup/": ["bag", "BagEquipmentLevelupRequest"],
    "/game/bagequipment/destroy/": ["bag", "BagEquipmentDestroyRequest"],
    "/game/bagequipment/batchdestroy/": ["bag", "BagEquipmentBatchDestroyRequest"],
    "/game/unit/levelup/": ["unit", "UnitLevelUpRequest"],
    "/game/unit/stepup/": ["unit", "UnitStepUpRequest"],
    "/game/unit/destroy/": ["unit", "UnitDestroyRequest"],
    "/game/formation/setstaff/": ["formation", "FormationSetStaffRequest"],
    "/game/formation/setunit/": ["formation", "FormationSetUnitRequest"],
    "/game/formation/active/": ["formation", "FormationActiveRequest"],
    "/game/formation/levelup/": ["formation", "FormationLevelUpRequest"],
    "/game/formation/use/": ["formation", "FormationUseRequest"],
    "/game/talent/levelup/": ["talent", "TalentLevelUpRequest"],
    "/game/talent/reset/": ["talent", "TalentResetTalentRequest"],
    "/game/dungeon/start/": ["dungeon", "DungeonMatchRequest"],
    "/game/dungeon/report/": ["dungeon", "DungeonMatchReportRequest"],
    "/game/dungeon/buytimes/": ["dungeon", "DungeonBuyTimesRequest"],
    "/game/arena/refresh/": ["arena", "ArenaRefreshRequest"],
    "/game/arena/leaderboard/": ["arena", "ArenaLeaderBoardRequest"],
    "/game/arena/honorreward/": ["arena", "ArenaHonorGetRewardRequest"],
    "/game/arena/matchstart/": ["arena", "ArenaMatchStartReqeust"],
    "/game/arena/matchreport/": ["arena", "ArenaMatchReportReqeust"],
    "/game/arena/buytimes/": ["arena", "ArenaBuyTimesRequest"],
    "/game/tower/matchstart/": ["tower", "TowerMatchStartRequest"],
    "/game/tower/matchreport/": ["tower", "TowerMatchReportReqeust"],
    "/game/tower/reset/": ["tower", "TowerResetRequest"],
    "/game/tower/turntable/": ["tower", "TowerTurnTableRequest"],
    "/game/tower/sweep/": ["tower", "TowerSweepRequest"],
    "/game/tower/sweepfinish/": ["tower", "TowerSweepFinishRequest"],
    "/game/tower/leaderboard/": ["tower", "TowerLeaderBoardRequest"],
    "/game/tower/starreward/": ["tower", "TowerStarGetRewardReqeust"],
    "/game/tower/goodsbuy/": ["tower", "TowerGoodsBuyRequest"],
    "/game/territory/start/": ["territory", "TerritoryTrainingStartReqeust"],
    "/game/territory/getreward/": ["territory", "TerritoryTrainingGetRewardReqeust"],
    "/game/territory/store/buy/": ["territory", "TerritoryStoreBuyRequest"],
    "/game/territory/friend/list/": ["territory", "TerritoryFriendListRequest"],
    "/game/territory/friend/help/": ["territory", "TerritoryFriendHelpRequest"],
    "/game/territory/friend/report/": ["territory", "TerritoryMatchReportRequest"],
    "/game/territory/inspire/": ["territory", "TerritoryInspireRequest"],
    "/game/territory/friend/match/": ["territory", "TerritoryMatchStartRequest"],
    "/game/store/buy/": ["store", "StoreBuyRequest"],
    "/game/store/refresh/": ["store", "StoreRefreshRequest"],
    "/game/store/autorefresh/": ["store", "StoreAutoRefreshRequest"],
    "/game/vip/buyreward/": ["vip", "VIPBuyRewardRequest"],
    "/game/energy/buy/": ["energy", "EnergyBuyRequest"],
    "/game/welfare/signin/": ["welfare", "WelfareSignInRequest"],
    "/game/welfare/newplayer/": ["welfare", "WelfareNewPlayerGetRequest"],
    "/game/welfare/levelreward/": ["welfare", "WelfareLevelRewardGetRequest"],
    "/game/welfare/energyreward/": ["welfare", "WelfareEnergyRewardGetReqeust"],
    "/game/union/create/": ["union", "UnionCreateRequest"],
    "/game/union/setbulletin/": ["union", "UnionSetBulletinRequest"],
    "/game/union/list/": ["union", "UnionListRequest"],
    "/game/union/apply/": ["union", "UnionApplyRequest"],
    "/game/union/agree/": ["union", "UnionAgreeRequest"],
    "/game/union/refuse/": ["union", "UnionRefuseRequest"],
    "/game/union/kick/": ["union", "UnionKickRequest"],
    "/game/union/transfer/": ["union", "UnionTransferRequest"],
    "/game/union/quit/": ["union", "UnionQuitRequest"],
    "/game/union/signin/": ["union", "UnionSigninRequest"],
    "/game/purchase/verify/": ["purchase", "PurchaseVerifyRequest"],
    "/game/purchase/getfirstreward/": ["purchase", "PurchaseGetFirstRewardRequest"],
    "/game/activity/newplayer/getreward/": ["activity", "ActivityNewPlayerGetRewardRequest"],
    "/game/activity/newplayer/dailybuy/": ["activity", "ActivityNewPlayerDailyBuyRequest"],
    "/game/plunder/formation/setstaff/": ["plunder", "PlunderFormationSetStaffRequest"],
    "/game/plunder/formation/setunit/": ["plunder", "PlunderFormationSetUnitRequest"],
    "/game/plunder/search/": ["plunder", "PlunderSearchRequest"],
    "/game/plunder/spy/": ["plunder", "PlunderSpyRequest"],
    "/game/plunder/start/": ["plunder", "PlunderStartRequest"],
    "/game/plunder/report/": ["plunder", "PlunderReportRequest"],
    "/game/plunder/getreward/": ["plunder", "PlunderGetRewardRequest"],
    "/game/plunder/station/sync/": ["plunder", "BaseStationSyncRequest"],
    "/game/plunder/buytimes/": ["plunder", "PlunderBuyTimesRequest"],
    "/game/plunder/station/getproduct/": ["plunder", "BaseStationGetProductRequest"],
    "/game/plunder/specialequip/generate/": ["plunder", "SpecialEquipmentGenerateRequest"],
    "/game/plunder/specialequip/speedup/": ["plunder", "SpecialEquipmentGenerateSpeedUpRequest"],
    "/game/plunder/specialequip/get/": ["plunder", "SpecialEquipmentGetRequest"],
    "/game/plunder/dailyreward/get/": ["plunder", "PlunderDailyRewardGetRequest"],
    "/game/inspire/setstaff/": ["inspire", "InspireSetStaffRequest"],
    "/game/champion/formation/setstaff/": ["championship", "ChampionFormationSetStaffRequest"],
    "/game/champion/formation/setunit/": ["championship", "ChampionFormationSetUnitRequest"],
    "/game/champion/formation/setposition/": ["championship", "ChampionFormationSetPositionRequest"],
    "/game/champion/apply/": ["championship", "ChampionApplyRequest"],
    "/game/champion/bet/": ["championship", "ChampionBetRequest"],
    "/game/champion/group/sync/": ["championship", "ChampionGroupSyncRequest"],
    "/game/champion/level/sync/": ["championship", "ChampionLevelSyncRequest"],
}

PATH_TO_RESPONSE = {
    "/game/sync/": ["common", "SyncResponse"],
    "/game/ping/": ["common", "PingResponse"],
    "/game/servers/": ["server", "GetServerListResponse"],
    "/game/start/": ["server", "StartGameResponse"],
    "/game/account/register/": ["account", "RegisterResponse"],
    "/game/account/login/": ["account", "LoginResponse"],
    "/game/club/create/": ["club", "CreateClubResponse"],
    "/game/club/leaderboard/": ["club", "ClubLeaderBoardResponse"],
    "/game/staff/recruit/": ["staff", "StaffRecruitResponse"],
    "/game/staff/equipchange/": ["staff", "StaffEquipChangeResponse"],
    "/game/staff/levelup/": ["staff", "StaffLevelUpResponse"],
    "/game/staff/stepup/": ["staff", "StaffStepUpResponse"],
    "/game/staff/starup/": ["staff", "StaffStarUpResponse"],
    "/game/staff/destroy/": ["staff", "StaffDestroyResponse"],
    "/game/staff/batchdestroy/": ["staff", "StaffBatchDestroyResponse"],
    "/game/challenge/start/": ["challenge", "ChallengeStartResponse"],
    "/game/challenge/chapter/reward/": ["challenge", "ChapterGetStarRewardResponse"],
    "/game/challenge/report/": ["challenge", "ChallengeMatchReportResponse"],
    "/game/challenge/sweep/": ["challenge", "ChallengeSweepResponse"],
    "/game/challenge/reset/": ["challenge", "ChallengeResetResponse"],
    "/game/taskdaily/getreward/": ["task", "TaskDailyGetRewardResponse"],
    "/game/friend/info/": ["friend", "FriendGetInfoResponse"],
    "/game/friend/add/": ["friend", "FriendAddResponse"],
    "/game/friend/remove/": ["friend", "FriendRemoveResponse"],
    "/game/friend/accept/": ["friend", "FriendAcceptResponse"],
    "/game/friend/candidates/": ["friend", "FriendCandidatesResponse"],
    "/game/mail/send/": ["mail", "MailSendResponse"],
    "/game/mail/open/": ["mail", "MailOpenResponse"],
    "/game/mail/delete/": ["mail", "MailDeleteResponse"],
    "/game/mail/getattachment/": ["mail", "MailGetAttachmentResponse"],
    "/game/chat/send/": ["chat", "ChatSendResponse"],
    "/game/notification/open/": ["notification", "NotificationOpenResponse"],
    "/game/notification/delete/": ["notification", "NotificationDeleteResponse"],
    "/game/bagitem/use/": ["bag", "BagItemUseResponse"],
    "/game/bagitem/merge/": ["bag", "BagItemMergeResponse"],
    "/game/bagitem/destroy/": ["bag", "BagItemDestroyResponse"],
    "/game/bagequipment/levelup/": ["bag", "BagEquipmentLevelupResponse"],
    "/game/bagequipment/destroy/": ["bag", "BagEquipmentDestroyResponse"],
    "/game/bagequipment/batchdestroy/": ["bag", "BagEquipmentBatchDestroyResponse"],
    "/game/unit/levelup/": ["unit", "UnitLevelUpResponse"],
    "/game/unit/stepup/": ["unit", "UnitStepUpResponse"],
    "/game/unit/destroy/": ["unit", "UnitDestroyResponse"],
    "/game/formation/setstaff/": ["formation", "FormationSetStaffResponse"],
    "/game/formation/setunit/": ["formation", "FormationSetUnitResponse"],
    "/game/formation/active/": ["formation", "FormationActiveResponse"],
    "/game/formation/levelup/": ["formation", "FormationLevelUpResponse"],
    "/game/formation/use/": ["formation", "FormationUseResponse"],
    "/game/talent/levelup/": ["talent", "TalentLevelUpResponse"],
    "/game/talent/reset/": ["talent", "TalentResetTalentResponse"],
    "/game/dungeon/start/": ["dungeon", "DungeonMatchResponse"],
    "/game/dungeon/report/": ["dungeon", "DungeonMatchReportResponse"],
    "/game/dungeon/buytimes/": ["dungeon", "DungeonBuyTimesResponse"],
    "/game/arena/refresh/": ["arena", "ArenaRefreshResponse"],
    "/game/arena/leaderboard/": ["arena", "ArenaLeaderBoardResponse"],
    "/game/arena/honorreward/": ["arena", "ArenaHonorGetRewardResponse"],
    "/game/arena/matchstart/": ["arena", "ArenaMatchStartResponse"],
    "/game/arena/matchreport/": ["arena", "ArenaMatchReportResponse"],
    "/game/arena/buytimes/": ["arena", "ArenaBuyTimesResponse"],
    "/game/tower/matchstart/": ["tower", "TowerMatchStartResponse"],
    "/game/tower/matchreport/": ["tower", "TowerMatchReportResponse"],
    "/game/tower/reset/": ["tower", "TowerResetResponse"],
    "/game/tower/turntable/": ["tower", "TowerTurnTableResponse"],
    "/game/tower/sweep/": ["tower", "TowerSweepResponse"],
    "/game/tower/sweepfinish/": ["tower", "TowerSweepFinishResponse"],
    "/game/tower/leaderboard/": ["tower", "TowerLeaderBoardResponse"],
    "/game/tower/starreward/": ["tower", "TowerStarGetRewardResponse"],
    "/game/tower/goodsbuy/": ["tower", "TowerGoodsBuyResponse"],
    "/game/territory/start/": ["territory", "TerritoryTrainingStartResponse"],
    "/game/territory/getreward/": ["territory", "TerritoryTrainingGetRewardResponse"],
    "/game/territory/store/buy/": ["territory", "TerritoryStoreBuyResponse"],
    "/game/territory/friend/list/": ["territory", "TerritoryFriendListResponse"],
    "/game/territory/friend/help/": ["territory", "TerritoryFriendHelpResponse"],
    "/game/territory/friend/report/": ["territory", "TerritoryMatchReportResponse"],
    "/game/territory/inspire/": ["territory", "TerritoryInspireResponse"],
    "/game/territory/friend/match/": ["territory", "TerritoryMatchStartResponse"],
    "/game/store/buy/": ["store", "StoreBuyResponse"],
    "/game/store/refresh/": ["store", "StoreRefreshResponse"],
    "/game/store/autorefresh/": ["store", "StoreAutoRefreshResponse"],
    "/game/vip/buyreward/": ["vip", "VIPBuyRewardResponse"],
    "/game/energy/buy/": ["energy", "EnergyBuyResponse"],
    "/game/welfare/signin/": ["welfare", "WelfareSignInResponse"],
    "/game/welfare/newplayer/": ["welfare", "WelfareNewPlayerGetResponse"],
    "/game/welfare/levelreward/": ["welfare", "WelfareLevelRewardGetResponse"],
    "/game/welfare/energyreward/": ["welfare", "WelfareEnergyRewardGetResponse"],
    "/game/union/create/": ["union", "UnionCreateResponse"],
    "/game/union/setbulletin/": ["union", "UnionSetBulletinResponse"],
    "/game/union/list/": ["union", "UnionListResponse"],
    "/game/union/apply/": ["union", "UnionApplyResponse"],
    "/game/union/agree/": ["union", "UnionAgreeResponse"],
    "/game/union/refuse/": ["union", "UnionRefuseResponse"],
    "/game/union/kick/": ["union", "UnionKickResponse"],
    "/game/union/transfer/": ["union", "UnionTransferResponse"],
    "/game/union/quit/": ["union", "UnionQuitResponse"],
    "/game/union/signin/": ["union", "UnionSigninResponse"],
    "/game/purchase/verify/": ["purchase", "PurchaseVerifyResponse"],
    "/game/purchase/getfirstreward/": ["purchase", "PurchaseGetFirstRewardResponse"],
    "/game/activity/newplayer/getreward/": ["activity", "ActivityNewPlayerGetRewardResponse"],
    "/game/activity/newplayer/dailybuy/": ["activity", "ActivityNewPlayerDailyBuyResponse"],
    "/game/plunder/formation/setstaff/": ["plunder", "PlunderFormationSetStaffResponse"],
    "/game/plunder/formation/setunit/": ["plunder", "PlunderFormationSetUnitResponse"],
    "/game/plunder/search/": ["plunder", "PlunderSearchResponse"],
    "/game/plunder/spy/": ["plunder", "PlunderSpyResponse"],
    "/game/plunder/start/": ["plunder", "PlunderStartResponse"],
    "/game/plunder/report/": ["plunder", "PlunderReportResponse"],
    "/game/plunder/getreward/": ["plunder", "PlunderGetRewardResponse"],
    "/game/plunder/station/sync/": ["plunder", "BaseStationSyncResponse"],
    "/game/plunder/buytimes/": ["plunder", "PlunderBuyTimesResponse"],
    "/game/plunder/station/getproduct/": ["plunder", "BaseStationGetProductResponse"],
    "/game/plunder/specialequip/generate/": ["plunder", "SpecialEquipmentGenerateResponse"],
    "/game/plunder/specialequip/speedup/": ["plunder", "SpecialEquipmentGenerateSpeedUpResponse"],
    "/game/plunder/specialequip/get/": ["plunder", "SpecialEquipmentGetResponse"],
    "/game/plunder/dailyreward/get/": ["plunder", "PlunderDailyRewardGetResponse"],
    "/game/inspire/setstaff/": ["inspire", "InspireSetStaffResponse"],
    "/game/champion/formation/setstaff/": ["championship", "ChampionFormationSetStaffResponse"],
    "/game/champion/formation/setunit/": ["championship", "ChampionFormationSetUnitResponse"],
    "/game/champion/formation/setposition/": ["championship", "ChampionFormationSetPositionResponse"],
    "/game/champion/apply/": ["championship", "ChampionApplyResponse"],
    "/game/champion/bet/": ["championship", "ChampionBetResponse"],
    "/game/champion/group/sync/": ["championship", "ChampionGroupSyncResponse"],
    "/game/champion/level/sync/": ["championship", "ChampionLevelSyncResponse"],
}
