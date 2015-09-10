# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: friend.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import character_pb2 as character__pb2
import club_pb2 as club__pb2
import common_pb2 as common__pb2
import match_pb2 as match__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='friend.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=b'\n\x0c\x66riend.proto\x12\x11\x44ianjing.protocol\x1a\x0f\x63haracter.proto\x1a\nclub.proto\x1a\x0c\x63ommon.proto\x1a\x0bmatch.proto\"\xb3\x02\n\x0c\x46riendNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12\x37\n\x07\x66riends\x18\x03 \x03(\x0b\x32&.Dianjing.protocol.FriendNotify.Friend\x1a\xb0\x01\n\x06\x46riend\x12/\n\x06status\x18\x01 \x02(\x0e\x32\x1f.Dianjing.protocol.FriendStatus\x12\n\n\x02id\x18\x02 \x02(\t\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x0e\n\x06\x61vatar\x18\x04 \x02(\t\x12\x11\n\tclub_name\x18\x05 \x02(\t\x12\x11\n\tclub_flag\x18\x06 \x02(\x05\x12\x11\n\tclub_gold\x18\x07 \x02(\x05\x12\x12\n\nclub_level\x18\x08 \x02(\x05\"2\n\x12\x46riendRemoveNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0b\n\x03ids\x18\x02 \x03(\t\"3\n\x14\x46riendGetInfoRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\t\"\x88\x01\n\x15\x46riendGetInfoResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12*\n\x04\x63har\x18\x03 \x02(\x0b\x32\x1c.Dianjing.protocol.Character\x12%\n\x04\x63lub\x18\x04 \x02(\x0b\x32\x17.Dianjing.protocol.Club\"1\n\x10\x46riendAddRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0c\n\x04name\x18\x02 \x02(\t\"1\n\x11\x46riendAddResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"2\n\x13\x46riendRemoveRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\t\"4\n\x14\x46riendRemoveResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"2\n\x13\x46riendAcceptRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\t\"4\n\x14\x46riendAcceptResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"1\n\x12\x46riendMatchRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\t\"`\n\x13\x46riendMatchResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12+\n\x05match\x18\x03 \x01(\x0b\x32\x1c.Dianjing.protocol.ClubMatch*i\n\x0c\x46riendStatus\x12\x0e\n\nFRIEND_NOT\x10\x01\x12\x1c\n\x18\x46RIEND_NEED_PEER_CONFIRM\x10\x02\x12\x1c\n\x18\x46RIEND_NEED_SELF_CONFIRM\x10\x03\x12\r\n\tFRIEND_OK\x10\x04'
  ,
  dependencies=[character__pb2.DESCRIPTOR,club__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,match__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FRIENDSTATUS = _descriptor.EnumDescriptor(
  name='FriendStatus',
  full_name='Dianjing.protocol.FriendStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FRIEND_NOT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIEND_NEED_PEER_CONFIRM', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIEND_NEED_SELF_CONFIRM', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIEND_OK', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1108,
  serialized_end=1213,
)
_sym_db.RegisterEnumDescriptor(_FRIENDSTATUS)

FriendStatus = enum_type_wrapper.EnumTypeWrapper(_FRIENDSTATUS)
FRIEND_NOT = 1
FRIEND_NEED_PEER_CONFIRM = 2
FRIEND_NEED_SELF_CONFIRM = 3
FRIEND_OK = 4



_FRIENDNOTIFY_FRIEND = _descriptor.Descriptor(
  name='Friend',
  full_name='Dianjing.protocol.FriendNotify.Friend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Dianjing.protocol.FriendNotify.Friend.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.FriendNotify.Friend.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dianjing.protocol.FriendNotify.Friend.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='Dianjing.protocol.FriendNotify.Friend.avatar', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club_name', full_name='Dianjing.protocol.FriendNotify.Friend.club_name', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club_flag', full_name='Dianjing.protocol.FriendNotify.Friend.club_flag', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club_gold', full_name='Dianjing.protocol.FriendNotify.Friend.club_gold', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club_level', full_name='Dianjing.protocol.FriendNotify.Friend.club_level', index=7,
      number=8, type=5, cpp_type=1, label=2,
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
  serialized_start=223,
  serialized_end=399,
)

_FRIENDNOTIFY = _descriptor.Descriptor(
  name='FriendNotify',
  full_name='Dianjing.protocol.FriendNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.FriendNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friends', full_name='Dianjing.protocol.FriendNotify.friends', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FRIENDNOTIFY_FRIEND, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=399,
)


_FRIENDREMOVENOTIFY = _descriptor.Descriptor(
  name='FriendRemoveNotify',
  full_name='Dianjing.protocol.FriendRemoveNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendRemoveNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ids', full_name='Dianjing.protocol.FriendRemoveNotify.ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=401,
  serialized_end=451,
)


_FRIENDGETINFOREQUEST = _descriptor.Descriptor(
  name='FriendGetInfoRequest',
  full_name='Dianjing.protocol.FriendGetInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendGetInfoRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.FriendGetInfoRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=453,
  serialized_end=504,
)


_FRIENDGETINFORESPONSE = _descriptor.Descriptor(
  name='FriendGetInfoResponse',
  full_name='Dianjing.protocol.FriendGetInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FriendGetInfoResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendGetInfoResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char', full_name='Dianjing.protocol.FriendGetInfoResponse.char', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club', full_name='Dianjing.protocol.FriendGetInfoResponse.club', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=507,
  serialized_end=643,
)


_FRIENDADDREQUEST = _descriptor.Descriptor(
  name='FriendAddRequest',
  full_name='Dianjing.protocol.FriendAddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendAddRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dianjing.protocol.FriendAddRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=645,
  serialized_end=694,
)


_FRIENDADDRESPONSE = _descriptor.Descriptor(
  name='FriendAddResponse',
  full_name='Dianjing.protocol.FriendAddResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FriendAddResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendAddResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  serialized_start=696,
  serialized_end=745,
)


_FRIENDREMOVEREQUEST = _descriptor.Descriptor(
  name='FriendRemoveRequest',
  full_name='Dianjing.protocol.FriendRemoveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendRemoveRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.FriendRemoveRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=747,
  serialized_end=797,
)


_FRIENDREMOVERESPONSE = _descriptor.Descriptor(
  name='FriendRemoveResponse',
  full_name='Dianjing.protocol.FriendRemoveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FriendRemoveResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendRemoveResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  serialized_start=799,
  serialized_end=851,
)


_FRIENDACCEPTREQUEST = _descriptor.Descriptor(
  name='FriendAcceptRequest',
  full_name='Dianjing.protocol.FriendAcceptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendAcceptRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.FriendAcceptRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=853,
  serialized_end=903,
)


_FRIENDACCEPTRESPONSE = _descriptor.Descriptor(
  name='FriendAcceptResponse',
  full_name='Dianjing.protocol.FriendAcceptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FriendAcceptResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendAcceptResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  serialized_start=905,
  serialized_end=957,
)


_FRIENDMATCHREQUEST = _descriptor.Descriptor(
  name='FriendMatchRequest',
  full_name='Dianjing.protocol.FriendMatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendMatchRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.FriendMatchRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=959,
  serialized_end=1008,
)


_FRIENDMATCHRESPONSE = _descriptor.Descriptor(
  name='FriendMatchResponse',
  full_name='Dianjing.protocol.FriendMatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FriendMatchResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FriendMatchResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match', full_name='Dianjing.protocol.FriendMatchResponse.match', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1010,
  serialized_end=1106,
)

_FRIENDNOTIFY_FRIEND.fields_by_name['status'].enum_type = _FRIENDSTATUS
_FRIENDNOTIFY_FRIEND.containing_type = _FRIENDNOTIFY
_FRIENDNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_FRIENDNOTIFY.fields_by_name['friends'].message_type = _FRIENDNOTIFY_FRIEND
_FRIENDGETINFORESPONSE.fields_by_name['char'].message_type = character__pb2._CHARACTER
_FRIENDGETINFORESPONSE.fields_by_name['club'].message_type = club__pb2._CLUB
_FRIENDMATCHRESPONSE.fields_by_name['match'].message_type = match__pb2._CLUBMATCH
DESCRIPTOR.message_types_by_name['FriendNotify'] = _FRIENDNOTIFY
DESCRIPTOR.message_types_by_name['FriendRemoveNotify'] = _FRIENDREMOVENOTIFY
DESCRIPTOR.message_types_by_name['FriendGetInfoRequest'] = _FRIENDGETINFOREQUEST
DESCRIPTOR.message_types_by_name['FriendGetInfoResponse'] = _FRIENDGETINFORESPONSE
DESCRIPTOR.message_types_by_name['FriendAddRequest'] = _FRIENDADDREQUEST
DESCRIPTOR.message_types_by_name['FriendAddResponse'] = _FRIENDADDRESPONSE
DESCRIPTOR.message_types_by_name['FriendRemoveRequest'] = _FRIENDREMOVEREQUEST
DESCRIPTOR.message_types_by_name['FriendRemoveResponse'] = _FRIENDREMOVERESPONSE
DESCRIPTOR.message_types_by_name['FriendAcceptRequest'] = _FRIENDACCEPTREQUEST
DESCRIPTOR.message_types_by_name['FriendAcceptResponse'] = _FRIENDACCEPTRESPONSE
DESCRIPTOR.message_types_by_name['FriendMatchRequest'] = _FRIENDMATCHREQUEST
DESCRIPTOR.message_types_by_name['FriendMatchResponse'] = _FRIENDMATCHRESPONSE
DESCRIPTOR.enum_types_by_name['FriendStatus'] = _FRIENDSTATUS

FriendNotify = _reflection.GeneratedProtocolMessageType('FriendNotify', (_message.Message,), dict(

  Friend = _reflection.GeneratedProtocolMessageType('Friend', (_message.Message,), dict(
    DESCRIPTOR = _FRIENDNOTIFY_FRIEND,
    __module__ = 'friend_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendNotify.Friend)
    ))
  ,
  DESCRIPTOR = _FRIENDNOTIFY,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendNotify)
  ))
_sym_db.RegisterMessage(FriendNotify)
_sym_db.RegisterMessage(FriendNotify.Friend)

FriendRemoveNotify = _reflection.GeneratedProtocolMessageType('FriendRemoveNotify', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDREMOVENOTIFY,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendRemoveNotify)
  ))
_sym_db.RegisterMessage(FriendRemoveNotify)

FriendGetInfoRequest = _reflection.GeneratedProtocolMessageType('FriendGetInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDGETINFOREQUEST,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendGetInfoRequest)
  ))
_sym_db.RegisterMessage(FriendGetInfoRequest)

FriendGetInfoResponse = _reflection.GeneratedProtocolMessageType('FriendGetInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDGETINFORESPONSE,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendGetInfoResponse)
  ))
_sym_db.RegisterMessage(FriendGetInfoResponse)

FriendAddRequest = _reflection.GeneratedProtocolMessageType('FriendAddRequest', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDADDREQUEST,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendAddRequest)
  ))
_sym_db.RegisterMessage(FriendAddRequest)

FriendAddResponse = _reflection.GeneratedProtocolMessageType('FriendAddResponse', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDADDRESPONSE,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendAddResponse)
  ))
_sym_db.RegisterMessage(FriendAddResponse)

FriendRemoveRequest = _reflection.GeneratedProtocolMessageType('FriendRemoveRequest', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDREMOVEREQUEST,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendRemoveRequest)
  ))
_sym_db.RegisterMessage(FriendRemoveRequest)

FriendRemoveResponse = _reflection.GeneratedProtocolMessageType('FriendRemoveResponse', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDREMOVERESPONSE,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendRemoveResponse)
  ))
_sym_db.RegisterMessage(FriendRemoveResponse)

FriendAcceptRequest = _reflection.GeneratedProtocolMessageType('FriendAcceptRequest', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDACCEPTREQUEST,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendAcceptRequest)
  ))
_sym_db.RegisterMessage(FriendAcceptRequest)

FriendAcceptResponse = _reflection.GeneratedProtocolMessageType('FriendAcceptResponse', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDACCEPTRESPONSE,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendAcceptResponse)
  ))
_sym_db.RegisterMessage(FriendAcceptResponse)

FriendMatchRequest = _reflection.GeneratedProtocolMessageType('FriendMatchRequest', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDMATCHREQUEST,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendMatchRequest)
  ))
_sym_db.RegisterMessage(FriendMatchRequest)

FriendMatchResponse = _reflection.GeneratedProtocolMessageType('FriendMatchResponse', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDMATCHRESPONSE,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FriendMatchResponse)
  ))
_sym_db.RegisterMessage(FriendMatchResponse)


# @@protoc_insertion_point(module_scope)
