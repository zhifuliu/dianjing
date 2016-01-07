
MESSAGE_TO_ID = {
    "UTCNotify": 10,
    "SyncRequest": 11,
    "SyncResponse": 12,
    "PingRequest": 13,
    "PingResponse": 14,
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
    "CharacterUploadAvatarRequest": 303,
    "CharacterUploadAvatarResponse": 304,
    "ClubNotify": 400,
    "CreateClubRequest": 401,
    "CreateClubResponse": 402,
    "ClubSetPolicyRequest": 410,
    "ClubSetPolicyResponse": 411,
    "ClubSetMatchStaffRequest": 412,
    "ClubSetMatchStaffResponse": 413,
    "ClubStaffSlotsAmountNotify": 420,
    "ClubStaffSlotBuyRequest": 421,
    "ClubStaffSlotBuyResponse": 422,
    "StaffNotify": 500,
    "StaffRemoveNotify": 501,
    "StaffRecruitNotify": 520,
    "StaffRecruitRefreshRequest": 521,
    "StaffRecruitRefreshResponse": 522,
    "StaffRecruitRequest": 523,
    "StaffRecruitResponse": 524,
    "StaffFireRequest": 525,
    "StaffFireResponse": 526,
    "LeagueClubNotify": 600,
    "LeagueUserNotify": 601,
    "LeagueChallengeRequest": 602,
    "LeagueChallengeResponse": 603,
    "LeagueMatchReportRequest": 604,
    "LeagueMatchReportResponse": 605,
    "LeagueMatchRefreshRequest": 606,
    "LeagueMatchRefreshResponse": 607,
    "LeagueGetRewardRequest": 608,
    "LeagueGetRewardResponse": 609,
    "LeagueGetClubDetailInfoRequest": 610,
    "LeagueGetClubDetailInfoResponse": 611,
    "ChallengeNotify": 700,
    "ChallengeEnergyNotify": 701,
    "ChallengeStartRequest": 702,
    "ChallengeStartResponse": 703,
    "ChallengeGetStarRewardRequest": 704,
    "ChallengeGetStarRewardResponse": 705,
    "ChallengeMatchReportRequest": 706,
    "ChallengeMatchReportResponse": 707,
    "ChallengeBuyEnergyRequest": 708,
    "ChallengeBuyEnergyResponse": 709,
    "BuildingNotify": 800,
    "BuildingLevelUpRequest": 801,
    "BuildingLevelUpResponse": 802,
    "BuildingLevelSpeedUpRequest": 803,
    "buildinglevelspeedupResponse": 804,
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
    "TrainingBroadcastDetailRequest": 960,
    "TrainingBroadcastDetailResponse": 961,
    "TrainingShopNotify": 940,
    "TrainingShopStartRequest": 941,
    "TrainingShopStartResponse": 942,
    "TrainingShopSellRequest": 943,
    "TrainingShopSellResponse": 944,
    "TrainingShopCancelRequest": 945,
    "TrainingShopCancelResponse": 946,
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
    "TaskGetRewardRequest": 1103,
    "TaskGetRewardResponse": 1104,
    "TaskDoingRequest": 1105,
    "TaskDoingResponse": 1106,
    "RandomEventDoneRequest": 1107,
    "RandomEventDoneResponse": 1108,
    "RandomEventNotify": 1109,
    "TaskRemoveNotify": 1110,
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
    "LadderMatchReportRequest": 1712,
    "LadderMatchReportResponse": 1713,
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
    "ItemNotify": 2200,
    "ItemRemoveNotify": 2201,
    "ItemSellRequest": 2202,
    "ItemSellResponse": 2203,
    "ItemShopBuyRequest": 2300,
    "ItemShopBuyResponse": 2301,
    "TrainingMatchNotify": 2500,
    "TrainingMatchStartRequest": 2501,
    "TrainingMatchStartResponse": 2502,
    "TrainingMatchReportRequest": 2503,
    "TrainingMatchReportResponse": 2504,
    "TrainingMatchGetAdditionalRewardRequest": 2505,
    "TrainingMatchGetAdditionalRewardResponse": 2506,
    "EliteNotify": 2600,
    "EliteStartRequest": 2601,
    "EliteStartResponse": 2602,
    "EliteGetStarRewardRequest": 2603,
    "EliteGetStarRewardResponse": 2604,
    "EliteMatchReportRequest": 2605,
    "EliteMatchReportResponse": 2606,
    "StaffAuctionSellListNotify": 2700,
    "StaffAuctionSellRemoveNotify": 2701,
    "StaffAuctionSearchRequest": 2702,
    "StaffAuctionSearchResponse": 2703,
    "StaffAuctionSellRequest": 2704,
    "StaffAuctionSellResponse": 2705,
    "StaffAuctionCancelRequest": 2706,
    "StaffAuctionCancelResponse": 2707,
    "StaffAuctionBidingRequest": 2708,
    "StaffAuctionBiddingResponse": 2709,
    "StaffAuctionBidingListNotify": 2710,
    "StaffAuctionBidingRemoveNotify": 2711,
}

ID_TO_MESSAGE = {
    10: "UTCNotify",
    11: "SyncRequest",
    12: "SyncResponse",
    13: "PingRequest",
    14: "PingResponse",
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
    303: "CharacterUploadAvatarRequest",
    304: "CharacterUploadAvatarResponse",
    400: "ClubNotify",
    401: "CreateClubRequest",
    402: "CreateClubResponse",
    410: "ClubSetPolicyRequest",
    411: "ClubSetPolicyResponse",
    412: "ClubSetMatchStaffRequest",
    413: "ClubSetMatchStaffResponse",
    420: "ClubStaffSlotsAmountNotify",
    421: "ClubStaffSlotBuyRequest",
    422: "ClubStaffSlotBuyResponse",
    500: "StaffNotify",
    501: "StaffRemoveNotify",
    520: "StaffRecruitNotify",
    521: "StaffRecruitRefreshRequest",
    522: "StaffRecruitRefreshResponse",
    523: "StaffRecruitRequest",
    524: "StaffRecruitResponse",
    525: "StaffFireRequest",
    526: "StaffFireResponse",
    600: "LeagueClubNotify",
    601: "LeagueUserNotify",
    602: "LeagueChallengeRequest",
    603: "LeagueChallengeResponse",
    604: "LeagueMatchReportRequest",
    605: "LeagueMatchReportResponse",
    606: "LeagueMatchRefreshRequest",
    607: "LeagueMatchRefreshResponse",
    608: "LeagueGetRewardRequest",
    609: "LeagueGetRewardResponse",
    610: "LeagueGetClubDetailInfoRequest",
    611: "LeagueGetClubDetailInfoResponse",
    700: "ChallengeNotify",
    701: "ChallengeEnergyNotify",
    702: "ChallengeStartRequest",
    703: "ChallengeStartResponse",
    704: "ChallengeGetStarRewardRequest",
    705: "ChallengeGetStarRewardResponse",
    706: "ChallengeMatchReportRequest",
    707: "ChallengeMatchReportResponse",
    708: "ChallengeBuyEnergyRequest",
    709: "ChallengeBuyEnergyResponse",
    800: "BuildingNotify",
    801: "BuildingLevelUpRequest",
    802: "BuildingLevelUpResponse",
    803: "BuildingLevelSpeedUpRequest",
    804: "buildinglevelspeedupResponse",
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
    960: "TrainingBroadcastDetailRequest",
    961: "TrainingBroadcastDetailResponse",
    940: "TrainingShopNotify",
    941: "TrainingShopStartRequest",
    942: "TrainingShopStartResponse",
    943: "TrainingShopSellRequest",
    944: "TrainingShopSellResponse",
    945: "TrainingShopCancelRequest",
    946: "TrainingShopCancelResponse",
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
    1103: "TaskGetRewardRequest",
    1104: "TaskGetRewardResponse",
    1105: "TaskDoingRequest",
    1106: "TaskDoingResponse",
    1107: "RandomEventDoneRequest",
    1108: "RandomEventDoneResponse",
    1109: "RandomEventNotify",
    1110: "TaskRemoveNotify",
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
    1712: "LadderMatchReportRequest",
    1713: "LadderMatchReportResponse",
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
    2200: "ItemNotify",
    2201: "ItemRemoveNotify",
    2202: "ItemSellRequest",
    2203: "ItemSellResponse",
    2300: "ItemShopBuyRequest",
    2301: "ItemShopBuyResponse",
    2500: "TrainingMatchNotify",
    2501: "TrainingMatchStartRequest",
    2502: "TrainingMatchStartResponse",
    2503: "TrainingMatchReportRequest",
    2504: "TrainingMatchReportResponse",
    2505: "TrainingMatchGetAdditionalRewardRequest",
    2506: "TrainingMatchGetAdditionalRewardResponse",
    2600: "EliteNotify",
    2601: "EliteStartRequest",
    2602: "EliteStartResponse",
    2603: "EliteGetStarRewardRequest",
    2604: "EliteGetStarRewardResponse",
    2605: "EliteMatchReportRequest",
    2606: "EliteMatchReportResponse",
    2700: "StaffAuctionSellListNotify",
    2701: "StaffAuctionSellRemoveNotify",
    2702: "StaffAuctionSearchRequest",
    2703: "StaffAuctionSearchResponse",
    2704: "StaffAuctionSellRequest",
    2705: "StaffAuctionSellResponse",
    2706: "StaffAuctionCancelRequest",
    2707: "StaffAuctionCancelResponse",
    2708: "StaffAuctionBidingRequest",
    2709: "StaffAuctionBiddingResponse",
    2710: "StaffAuctionBidingListNotify",
    2711: "StaffAuctionBidingRemoveNotify",
}

PATH_TO_REQUEST = {
    "/game/sync/": ["common", "SyncRequest"],
    "/game/ping/": ["common", "PingRequest"],
    "/game/servers/": ["server", "GetServerListRequest"],
    "/game/start/": ["server", "StartGameRequest"],
    "/game/account/register/": ["account", "RegisterRequest"],
    "/game/account/login/": ["account", "LoginRequest"],
    "/game/character/create/": ["character", "CreateCharacterRequest"],
    "/game/character/avatar/upload/": ["character", "CharacterUploadAvatarRequest"],
    "/game/club/create/": ["club", "CreateClubRequest"],
    "/game/club/policy/": ["club", "ClubSetPolicyRequest"],
    "/game/club/matchstaff/": ["club", "ClubSetMatchStaffRequest"],
    "/game/club/staffslots/buy/": ["club", "ClubStaffSlotBuyRequest"],
    "/game/staff/recruit/refresh/": ["staff", "StaffRecruitRefreshRequest"],
    "/game/staff/recruit/": ["staff", "StaffRecruitRequest"],
    "/game/staff/fire/": ["staff", "StaffFireRequest"],
    "/game/league/challenge/": ["league", "LeagueChallengeRequest"],
    "/game/league/report/": ["league", "LeagueMatchReportRequest"],
    "/game/league/refresh/": ["league", "LeagueMatchRefreshRequest"],
    "/game/league/reward/": ["league", "LeagueGetRewardRequest"],
    "/game/league/detail/": ["league", "LeagueGetClubDetailInfoRequest"],
    "/game/challenge/start/": ["challenge", "ChallengeStartRequest"],
    "/game/challenge/reward/": ["challenge", "ChallengeGetStarRewardRequest"],
    "/game/challenge/report/": ["challenge", "ChallengeMatchReportRequest"],
    "/game/challenge/buy/": ["challenge", "ChallengeBuyEnergyRequest"],
    "/game/building/levelup/": ["building", "BuildingLevelUpRequest"],
    "/game/building/speedup/": ["building", "BuildingLevelSpeedUpRequest"],
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
    "/game/training/broadcast/detail/": ["training", "TrainingBroadcastDetailRequest"],
    "/game/training/shop/start/": ["training", "TrainingShopStartRequest"],
    "/game/training/shop/sell/": ["training", "TrainingShopSellRequest"],
    "/game/training/shop/cancel/": ["training", "TrainingShopCancelRequest"],
    "/game/training/sponsor/start/": ["training", "TrainingSponsorStartRequest"],
    "/game/skill/locktoggle/": ["skill", "SkillLockToggleRequest"],
    "/game/skill/wash/": ["skill", "SkillWashRequest"],
    "/game/skill/upgrade/speedup/": ["skill", "SkillUpgradeSpeedupRequest"],
    "/game/skill/upgrade/": ["skill", "SkillUpgradeRequest"],
    "/game/task/getreward/": ["task", "TaskGetRewardRequest"],
    "/game/task/doing/": ["task", "TaskDoingRequest"],
    "/game/randomevent/done/": ["task", "RandomEventDoneRequest"],
    "/game/friend/info/": ["friend", "FriendGetInfoRequest"],
    "/game/friend/add/": ["friend", "FriendAddRequest"],
    "/game/friend/remove/": ["friend", "FriendRemoveRequest"],
    "/game/friend/match/": ["friend", "FriendMatchRequest"],
    "/game/friend/accept/": ["friend", "FriendAcceptRequest"],
    "/game/friend/candidates/": ["friend", "FriendCandidatesRequest"],
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
    "/game/ladder/store/report/": ["ladder", "LadderMatchReportRequest"],
    "/game/cup/infomation/": ["cup", "CupInfomationRequest"],
    "/game/cup/join/": ["cup", "CupJoinRequest"],
    "/game/sponsor/": ["spread", "SponsorRequest"],
    "/game/sponsor/getincome/": ["spread", "SponsorGetIncomeRequest"],
    "/game/signin/": ["activity", "ActivitySignInRequest"],
    "/game/activity/loginreward/": ["activity", "ActivityLoginRewardRequest"],
    "/game/activevalue/getreward/": ["active_value", "ActiveValueGetRewardRequest"],
    "/game/item/sell/": ["item", "ItemSellRequest"],
    "/game/itemshop/buy/": ["shop", "ItemShopBuyRequest"],
    "/game/trainingmatch/start/": ["training_match", "TrainingMatchStartRequest"],
    "/game/trainingmatch/report/": ["training_match", "TrainingMatchReportRequest"],
    "/game/trainingmatch/additional/": ["training_match", "TrainingMatchGetAdditionalRewardRequest"],
    "/game/elite/start/": ["elite_match", "EliteStartRequest"],
    "/game/elite/reward/": ["elite_match", "EliteGetStarRewardRequest"],
    "/game/elite/report/": ["elite_match", "EliteMatchReportRequest"],
    "/game/auction/search/": ["auction", "StaffAuctionSearchRequest"],
    "/game/auction/sell/": ["auction", "StaffAuctionSellRequest"],
    "/game/auction/cancel/": ["auction", "StaffAuctionCancelRequest"],
    "/game/auction/bidding/": ["auction", "StaffAuctionBidingRequest"],
}

PATH_TO_RESPONSE = {
    "/game/sync/": ["common", "SyncResponse"],
    "/game/sync/": ["common", "PingResponse"],
    "/game/servers/": ["server", "GetServerListResponse"],
    "/game/start/": ["server", "StartGameResponse"],
    "/game/account/register/": ["account", "RegisterResponse"],
    "/game/account/login/": ["account", "LoginResponse"],
    "/game/character/create/": ["character", "CreateCharacterResponse"],
    "/game/character/avatar/upload/": ["character", "CharacterUploadAvatarResponse"],
    "/game/club/create/": ["club", "CreateClubResponse"],
    "/game/club/policy/": ["club", "ClubSetPolicyResponse"],
    "/game/club/matchstaff/": ["club", "ClubSetMatchStaffResponse"],
    "/game/club/staffslots/buy/": ["club", "ClubStaffSlotBuyResponse"],
    "/game/staff/recruit/refresh/": ["staff", "StaffRecruitRefreshResponse"],
    "/game/staff/recruit/": ["staff", "StaffRecruitResponse"],
    "/game/staff/fire/": ["staff", "StaffFireResponse"],
    "/game/league/challenge/": ["league", "LeagueChallengeResponse"],
    "/game/league/report/": ["league", "LeagueMatchReportResponse"],
    "/game/league/refresh/": ["league", "LeagueMatchRefreshResponse"],
    "/game/league/reward/": ["league", "LeagueGetRewardResponse"],
    "/game/league/detail/": ["league", "LeagueGetClubDetailInfoResponse"],
    "/game/challenge/start/": ["challenge", "ChallengeStartResponse"],
    "/game/challenge/reward/": ["challenge", "ChallengeGetStarRewardResponse"],
    "/game/challenge/report/": ["challenge", "ChallengeMatchReportResponse"],
    "/game/challenge/buy/": ["challenge", "ChallengeBuyEnergyResponse"],
    "/game/building/levelup/": ["building", "BuildingLevelUpResponse"],
    "/game/building/speedup/": ["building", "buildinglevelspeedupResponse"],
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
    "/game/training/broadcast/detail/": ["training", "TrainingBroadcastDetailResponse"],
    "/game/training/shop/start/": ["training", "TrainingShopStartResponse"],
    "/game/training/shop/sell/": ["training", "TrainingShopSellResponse"],
    "/game/training/shop/cancel/": ["training", "TrainingShopCancelResponse"],
    "/game/training/sponsor/start/": ["training", "TrainingSponsorStartResponse"],
    "/game/skill/locktoggle/": ["skill", "SkillLockToggleResponse"],
    "/game/skill/wash/": ["skill", "SkillWashResponse"],
    "/game/skill/upgrade/speedup/": ["skill", "SkillUpgradeSpeedupResponse"],
    "/game/skill/upgrade/": ["skill", "SkillUpgradeResponse"],
    "/game/task/getreward/": ["task", "TaskGetRewardResponse"],
    "/game/task/doing/": ["task", "TaskDoingResponse"],
    "/game/randomevent/done/": ["task", "RandomEventDoneResponse"],
    "/game/friend/info/": ["friend", "FriendGetInfoResponse"],
    "/game/friend/add/": ["friend", "FriendAddResponse"],
    "/game/friend/remove/": ["friend", "FriendRemoveResponse"],
    "/game/friend/match/": ["friend", "FriendMatchResponse"],
    "/game/friend/accept/": ["friend", "FriendAcceptResponse"],
    "/game/friend/candidates/": ["friend", "FriendCandidatesResponse"],
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
    "/game/ladder/store/report/": ["ladder", "LadderMatchReportResponse"],
    "/game/cup/infomation/": ["cup", "CupInfomationResponse"],
    "/game/cup/join/": ["cup", "CupJoinResponse"],
    "/game/sponsor/": ["spread", "SponsorResponse"],
    "/game/sponsor/getincome/": ["spread", "SponsorGetIncomeResponse"],
    "/game/signin/": ["activity", "ActivitySignInResponse"],
    "/game/activity/loginreward/": ["activity", "ActivityLoginRewardResponse"],
    "/game/activevalue/getreward/": ["active_value", "ActiveValueGetRewardResponse"],
    "/game/item/sell/": ["item", "ItemSellResponse"],
    "/game/itemshop/buy/": ["shop", "ItemShopBuyResponse"],
    "/game/trainingmatch/start/": ["training_match", "TrainingMatchStartResponse"],
    "/game/trainingmatch/report/": ["training_match", "TrainingMatchReportResponse"],
    "/game/trainingmatch/additional/": ["training_match", "TrainingMatchGetAdditionalRewardResponse"],
    "/game/elite/start/": ["elite_match", "EliteStartResponse"],
    "/game/elite/reward/": ["elite_match", "EliteGetStarRewardResponse"],
    "/game/elite/report/": ["elite_match", "EliteMatchReportResponse"],
    "/game/auction/search/": ["auction", "StaffAuctionSearchResponse"],
    "/game/auction/sell/": ["auction", "StaffAuctionSellResponse"],
    "/game/auction/cancel/": ["auction", "StaffAuctionCancelResponse"],
    "/game/auction/bidding/": ["auction", "StaffAuctionBiddingResponse"],
}
