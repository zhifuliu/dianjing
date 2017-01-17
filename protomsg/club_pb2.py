# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: club.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='club.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\nclub.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\"\xa6\x01\n\x04\x43lub\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04\x66lag\x18\x03 \x02(\x05\x12\r\n\x05level\x18\x04 \x02(\x05\x12\x0b\n\x03\x65xp\x18\x05 \x02(\x05\x12\x0c\n\x04gold\x18\x06 \x02(\x05\x12\x0f\n\x07\x64iamond\x18\x07 \x02(\x05\x12\x0f\n\x07\x63rystal\x18\x08 \x02(\x05\x12\x0b\n\x03gas\x18\t \x02(\x05\x12\x0e\n\x06renown\x18\n \x02(\x05\x12\r\n\x05power\x18\x0b \x02(\x05\"D\n\nClubNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12%\n\x04\x63lub\x18\x02 \x02(\x0b\x32\x17.Dianjing.protocol.Club\"D\n\x10\x43reateDaysNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0c\n\x04\x64\x61ys\x18\x02 \x02(\x05\x12\x11\n\tcreate_at\x18\x03 \x02(\x03\"@\n\x11\x43reateClubRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04\x66lag\x18\x03 \x02(\x05\"2\n\x12\x43reateClubResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\")\n\x16\x43lubLeaderBoardRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"\xdf\x01\n\x17\x43lubLeaderBoardResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12\x16\n\x0enext_update_at\x18\x03 \x02(\x03\x12/\n\x0e\x63lubs_by_level\x18\x04 \x03(\x0b\x32\x17.Dianjing.protocol.Club\x12/\n\x0e\x63lubs_by_power\x18\x05 \x03(\x0b\x32\x17.Dianjing.protocol.Club\x12\x15\n\rmy_level_rank\x18\x06 \x02(\x05\x12\x15\n\rmy_power_rank\x18\x07 \x02(\x05')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CLUB = _descriptor.Descriptor(
  name='Club',
  full_name='Dianjing.protocol.Club',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Club.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dianjing.protocol.Club.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='Dianjing.protocol.Club.flag', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Dianjing.protocol.Club.level', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='Dianjing.protocol.Club.exp', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='Dianjing.protocol.Club.gold', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diamond', full_name='Dianjing.protocol.Club.diamond', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crystal', full_name='Dianjing.protocol.Club.crystal', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gas', full_name='Dianjing.protocol.Club.gas', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='renown', full_name='Dianjing.protocol.Club.renown', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='Dianjing.protocol.Club.power', index=10,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=214,
)


_CLUBNOTIFY = _descriptor.Descriptor(
  name='ClubNotify',
  full_name='Dianjing.protocol.ClubNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ClubNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club', full_name='Dianjing.protocol.ClubNotify.club', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=284,
)


_CREATEDAYSNOTIFY = _descriptor.Descriptor(
  name='CreateDaysNotify',
  full_name='Dianjing.protocol.CreateDaysNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.CreateDaysNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='days', full_name='Dianjing.protocol.CreateDaysNotify.days', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_at', full_name='Dianjing.protocol.CreateDaysNotify.create_at', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=354,
)


_CREATECLUBREQUEST = _descriptor.Descriptor(
  name='CreateClubRequest',
  full_name='Dianjing.protocol.CreateClubRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.CreateClubRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dianjing.protocol.CreateClubRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='Dianjing.protocol.CreateClubRequest.flag', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=420,
)


_CREATECLUBRESPONSE = _descriptor.Descriptor(
  name='CreateClubResponse',
  full_name='Dianjing.protocol.CreateClubResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.CreateClubResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.CreateClubResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=422,
  serialized_end=472,
)


_CLUBLEADERBOARDREQUEST = _descriptor.Descriptor(
  name='ClubLeaderBoardRequest',
  full_name='Dianjing.protocol.ClubLeaderBoardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ClubLeaderBoardRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=515,
)


_CLUBLEADERBOARDRESPONSE = _descriptor.Descriptor(
  name='ClubLeaderBoardResponse',
  full_name='Dianjing.protocol.ClubLeaderBoardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.ClubLeaderBoardResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ClubLeaderBoardResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_update_at', full_name='Dianjing.protocol.ClubLeaderBoardResponse.next_update_at', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clubs_by_level', full_name='Dianjing.protocol.ClubLeaderBoardResponse.clubs_by_level', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clubs_by_power', full_name='Dianjing.protocol.ClubLeaderBoardResponse.clubs_by_power', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='my_level_rank', full_name='Dianjing.protocol.ClubLeaderBoardResponse.my_level_rank', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='my_power_rank', full_name='Dianjing.protocol.ClubLeaderBoardResponse.my_power_rank', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=741,
)

_CLUBNOTIFY.fields_by_name['club'].message_type = _CLUB
_CLUBLEADERBOARDRESPONSE.fields_by_name['clubs_by_level'].message_type = _CLUB
_CLUBLEADERBOARDRESPONSE.fields_by_name['clubs_by_power'].message_type = _CLUB
DESCRIPTOR.message_types_by_name['Club'] = _CLUB
DESCRIPTOR.message_types_by_name['ClubNotify'] = _CLUBNOTIFY
DESCRIPTOR.message_types_by_name['CreateDaysNotify'] = _CREATEDAYSNOTIFY
DESCRIPTOR.message_types_by_name['CreateClubRequest'] = _CREATECLUBREQUEST
DESCRIPTOR.message_types_by_name['CreateClubResponse'] = _CREATECLUBRESPONSE
DESCRIPTOR.message_types_by_name['ClubLeaderBoardRequest'] = _CLUBLEADERBOARDREQUEST
DESCRIPTOR.message_types_by_name['ClubLeaderBoardResponse'] = _CLUBLEADERBOARDRESPONSE

Club = _reflection.GeneratedProtocolMessageType('Club', (_message.Message,), dict(
  DESCRIPTOR = _CLUB,
  __module__ = 'club_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Club)
  ))
_sym_db.RegisterMessage(Club)

ClubNotify = _reflection.GeneratedProtocolMessageType('ClubNotify', (_message.Message,), dict(
  DESCRIPTOR = _CLUBNOTIFY,
  __module__ = 'club_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubNotify)
  ))
_sym_db.RegisterMessage(ClubNotify)

CreateDaysNotify = _reflection.GeneratedProtocolMessageType('CreateDaysNotify', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDAYSNOTIFY,
  __module__ = 'club_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.CreateDaysNotify)
  ))
_sym_db.RegisterMessage(CreateDaysNotify)

CreateClubRequest = _reflection.GeneratedProtocolMessageType('CreateClubRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATECLUBREQUEST,
  __module__ = 'club_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.CreateClubRequest)
  ))
_sym_db.RegisterMessage(CreateClubRequest)

CreateClubResponse = _reflection.GeneratedProtocolMessageType('CreateClubResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATECLUBRESPONSE,
  __module__ = 'club_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.CreateClubResponse)
  ))
_sym_db.RegisterMessage(CreateClubResponse)

ClubLeaderBoardRequest = _reflection.GeneratedProtocolMessageType('ClubLeaderBoardRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLUBLEADERBOARDREQUEST,
  __module__ = 'club_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubLeaderBoardRequest)
  ))
_sym_db.RegisterMessage(ClubLeaderBoardRequest)

ClubLeaderBoardResponse = _reflection.GeneratedProtocolMessageType('ClubLeaderBoardResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLUBLEADERBOARDRESPONSE,
  __module__ = 'club_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubLeaderBoardResponse)
  ))
_sym_db.RegisterMessage(ClubLeaderBoardResponse)


# @@protoc_insertion_point(module_scope)
