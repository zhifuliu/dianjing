# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: welfare.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import package_pb2 as package__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='welfare.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\rwelfare.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\x1a\rpackage.proto\"K\n\x0bWelfareItem\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x30\n\x06status\x18\x02 \x02(\x0e\x32 .Dianjing.protocol.WelfareStatus\"C\n\x13WelfareSignInNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0b\n\x03\x64\x61y\x18\x03 \x02(\x05\x12\x0e\n\x06signed\x18\x04 \x02(\x08\"\x80\x01\n\x16WelfareNewPlayerNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12-\n\x05items\x18\x03 \x03(\x0b\x32\x1e.Dianjing.protocol.WelfareItem\"\x82\x01\n\x18WelfareLevelRewardNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12-\n\x05items\x18\x03 \x03(\x0b\x32\x1e.Dianjing.protocol.WelfareItem\"\xb2\x01\n\x19WelfareEnergyRewardNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12J\n\ntime_range\x18\x02 \x03(\x0b\x32\x36.Dianjing.protocol.WelfareEnergyRewardNotify.TimeRange\x1a\x38\n\tTimeRange\x12\r\n\x05start\x18\x01 \x02(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x02(\x05\x12\x0f\n\x07\x63\x61n_get\x18\x03 \x02(\x08\"\'\n\x14WelfareSignInRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"\\\n\x15WelfareSignInResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12%\n\x04\x64rop\x18\x03 \x01(\x0b\x32\x17.Dianjing.protocol.Drop\"9\n\x1aWelfareNewPlayerGetRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"b\n\x1bWelfareNewPlayerGetResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12%\n\x04\x64rop\x18\x03 \x01(\x0b\x32\x17.Dianjing.protocol.Drop\";\n\x1cWelfareLevelRewardGetRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"d\n\x1dWelfareLevelRewardGetResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12%\n\x04\x64rop\x18\x03 \x01(\x0b\x32\x17.Dianjing.protocol.Drop\"0\n\x1dWelfareEnergyRewardGetReqeust\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"e\n\x1eWelfareEnergyRewardGetResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12%\n\x04\x64rop\x18\x03 \x01(\x0b\x32\x17.Dianjing.protocol.Drop*N\n\rWelfareStatus\x12\x13\n\x0fWELFARE_CAN_GET\x10\x01\x12\x13\n\x0fWELFARE_HAS_GOT\x10\x02\x12\x13\n\x0fWELFARE_CAN_NOT\x10\x03')
  ,
  dependencies=[common__pb2.DESCRIPTOR,package__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_WELFARESTATUS = _descriptor.EnumDescriptor(
  name='WelfareStatus',
  full_name='Dianjing.protocol.WelfareStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WELFARE_CAN_GET', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WELFARE_HAS_GOT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WELFARE_CAN_NOT', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1266,
  serialized_end=1344,
)
_sym_db.RegisterEnumDescriptor(_WELFARESTATUS)

WelfareStatus = enum_type_wrapper.EnumTypeWrapper(_WELFARESTATUS)
WELFARE_CAN_GET = 1
WELFARE_HAS_GOT = 2
WELFARE_CAN_NOT = 3



_WELFAREITEM = _descriptor.Descriptor(
  name='WelfareItem',
  full_name='Dianjing.protocol.WelfareItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.WelfareItem.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Dianjing.protocol.WelfareItem.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=65,
  serialized_end=140,
)


_WELFARESIGNINNOTIFY = _descriptor.Descriptor(
  name='WelfareSignInNotify',
  full_name='Dianjing.protocol.WelfareSignInNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareSignInNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day', full_name='Dianjing.protocol.WelfareSignInNotify.day', index=1,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signed', full_name='Dianjing.protocol.WelfareSignInNotify.signed', index=2,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=142,
  serialized_end=209,
)


_WELFARENEWPLAYERNOTIFY = _descriptor.Descriptor(
  name='WelfareNewPlayerNotify',
  full_name='Dianjing.protocol.WelfareNewPlayerNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareNewPlayerNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.WelfareNewPlayerNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='Dianjing.protocol.WelfareNewPlayerNotify.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=212,
  serialized_end=340,
)


_WELFARELEVELREWARDNOTIFY = _descriptor.Descriptor(
  name='WelfareLevelRewardNotify',
  full_name='Dianjing.protocol.WelfareLevelRewardNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareLevelRewardNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.WelfareLevelRewardNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='Dianjing.protocol.WelfareLevelRewardNotify.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=343,
  serialized_end=473,
)


_WELFAREENERGYREWARDNOTIFY_TIMERANGE = _descriptor.Descriptor(
  name='TimeRange',
  full_name='Dianjing.protocol.WelfareEnergyRewardNotify.TimeRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='Dianjing.protocol.WelfareEnergyRewardNotify.TimeRange.start', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='Dianjing.protocol.WelfareEnergyRewardNotify.TimeRange.end', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='can_get', full_name='Dianjing.protocol.WelfareEnergyRewardNotify.TimeRange.can_get', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=598,
  serialized_end=654,
)

_WELFAREENERGYREWARDNOTIFY = _descriptor.Descriptor(
  name='WelfareEnergyRewardNotify',
  full_name='Dianjing.protocol.WelfareEnergyRewardNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareEnergyRewardNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_range', full_name='Dianjing.protocol.WelfareEnergyRewardNotify.time_range', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WELFAREENERGYREWARDNOTIFY_TIMERANGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=654,
)


_WELFARESIGNINREQUEST = _descriptor.Descriptor(
  name='WelfareSignInRequest',
  full_name='Dianjing.protocol.WelfareSignInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareSignInRequest.session', index=0,
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
  serialized_start=656,
  serialized_end=695,
)


_WELFARESIGNINRESPONSE = _descriptor.Descriptor(
  name='WelfareSignInResponse',
  full_name='Dianjing.protocol.WelfareSignInResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.WelfareSignInResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareSignInResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.WelfareSignInResponse.drop', index=2,
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
  serialized_start=697,
  serialized_end=789,
)


_WELFARENEWPLAYERGETREQUEST = _descriptor.Descriptor(
  name='WelfareNewPlayerGetRequest',
  full_name='Dianjing.protocol.WelfareNewPlayerGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareNewPlayerGetRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.WelfareNewPlayerGetRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=791,
  serialized_end=848,
)


_WELFARENEWPLAYERGETRESPONSE = _descriptor.Descriptor(
  name='WelfareNewPlayerGetResponse',
  full_name='Dianjing.protocol.WelfareNewPlayerGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.WelfareNewPlayerGetResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareNewPlayerGetResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.WelfareNewPlayerGetResponse.drop', index=2,
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
  serialized_start=850,
  serialized_end=948,
)


_WELFARELEVELREWARDGETREQUEST = _descriptor.Descriptor(
  name='WelfareLevelRewardGetRequest',
  full_name='Dianjing.protocol.WelfareLevelRewardGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareLevelRewardGetRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.WelfareLevelRewardGetRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=950,
  serialized_end=1009,
)


_WELFARELEVELREWARDGETRESPONSE = _descriptor.Descriptor(
  name='WelfareLevelRewardGetResponse',
  full_name='Dianjing.protocol.WelfareLevelRewardGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.WelfareLevelRewardGetResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareLevelRewardGetResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.WelfareLevelRewardGetResponse.drop', index=2,
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
  serialized_start=1011,
  serialized_end=1111,
)


_WELFAREENERGYREWARDGETREQEUST = _descriptor.Descriptor(
  name='WelfareEnergyRewardGetReqeust',
  full_name='Dianjing.protocol.WelfareEnergyRewardGetReqeust',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareEnergyRewardGetReqeust.session', index=0,
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
  serialized_start=1113,
  serialized_end=1161,
)


_WELFAREENERGYREWARDGETRESPONSE = _descriptor.Descriptor(
  name='WelfareEnergyRewardGetResponse',
  full_name='Dianjing.protocol.WelfareEnergyRewardGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.WelfareEnergyRewardGetResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.WelfareEnergyRewardGetResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.WelfareEnergyRewardGetResponse.drop', index=2,
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
  serialized_start=1163,
  serialized_end=1264,
)

_WELFAREITEM.fields_by_name['status'].enum_type = _WELFARESTATUS
_WELFARENEWPLAYERNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_WELFARENEWPLAYERNOTIFY.fields_by_name['items'].message_type = _WELFAREITEM
_WELFARELEVELREWARDNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_WELFARELEVELREWARDNOTIFY.fields_by_name['items'].message_type = _WELFAREITEM
_WELFAREENERGYREWARDNOTIFY_TIMERANGE.containing_type = _WELFAREENERGYREWARDNOTIFY
_WELFAREENERGYREWARDNOTIFY.fields_by_name['time_range'].message_type = _WELFAREENERGYREWARDNOTIFY_TIMERANGE
_WELFARESIGNINRESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
_WELFARENEWPLAYERGETRESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
_WELFARELEVELREWARDGETRESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
_WELFAREENERGYREWARDGETRESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
DESCRIPTOR.message_types_by_name['WelfareItem'] = _WELFAREITEM
DESCRIPTOR.message_types_by_name['WelfareSignInNotify'] = _WELFARESIGNINNOTIFY
DESCRIPTOR.message_types_by_name['WelfareNewPlayerNotify'] = _WELFARENEWPLAYERNOTIFY
DESCRIPTOR.message_types_by_name['WelfareLevelRewardNotify'] = _WELFARELEVELREWARDNOTIFY
DESCRIPTOR.message_types_by_name['WelfareEnergyRewardNotify'] = _WELFAREENERGYREWARDNOTIFY
DESCRIPTOR.message_types_by_name['WelfareSignInRequest'] = _WELFARESIGNINREQUEST
DESCRIPTOR.message_types_by_name['WelfareSignInResponse'] = _WELFARESIGNINRESPONSE
DESCRIPTOR.message_types_by_name['WelfareNewPlayerGetRequest'] = _WELFARENEWPLAYERGETREQUEST
DESCRIPTOR.message_types_by_name['WelfareNewPlayerGetResponse'] = _WELFARENEWPLAYERGETRESPONSE
DESCRIPTOR.message_types_by_name['WelfareLevelRewardGetRequest'] = _WELFARELEVELREWARDGETREQUEST
DESCRIPTOR.message_types_by_name['WelfareLevelRewardGetResponse'] = _WELFARELEVELREWARDGETRESPONSE
DESCRIPTOR.message_types_by_name['WelfareEnergyRewardGetReqeust'] = _WELFAREENERGYREWARDGETREQEUST
DESCRIPTOR.message_types_by_name['WelfareEnergyRewardGetResponse'] = _WELFAREENERGYREWARDGETRESPONSE
DESCRIPTOR.enum_types_by_name['WelfareStatus'] = _WELFARESTATUS

WelfareItem = _reflection.GeneratedProtocolMessageType('WelfareItem', (_message.Message,), dict(
  DESCRIPTOR = _WELFAREITEM,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareItem)
  ))
_sym_db.RegisterMessage(WelfareItem)

WelfareSignInNotify = _reflection.GeneratedProtocolMessageType('WelfareSignInNotify', (_message.Message,), dict(
  DESCRIPTOR = _WELFARESIGNINNOTIFY,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareSignInNotify)
  ))
_sym_db.RegisterMessage(WelfareSignInNotify)

WelfareNewPlayerNotify = _reflection.GeneratedProtocolMessageType('WelfareNewPlayerNotify', (_message.Message,), dict(
  DESCRIPTOR = _WELFARENEWPLAYERNOTIFY,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareNewPlayerNotify)
  ))
_sym_db.RegisterMessage(WelfareNewPlayerNotify)

WelfareLevelRewardNotify = _reflection.GeneratedProtocolMessageType('WelfareLevelRewardNotify', (_message.Message,), dict(
  DESCRIPTOR = _WELFARELEVELREWARDNOTIFY,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareLevelRewardNotify)
  ))
_sym_db.RegisterMessage(WelfareLevelRewardNotify)

WelfareEnergyRewardNotify = _reflection.GeneratedProtocolMessageType('WelfareEnergyRewardNotify', (_message.Message,), dict(

  TimeRange = _reflection.GeneratedProtocolMessageType('TimeRange', (_message.Message,), dict(
    DESCRIPTOR = _WELFAREENERGYREWARDNOTIFY_TIMERANGE,
    __module__ = 'welfare_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareEnergyRewardNotify.TimeRange)
    ))
  ,
  DESCRIPTOR = _WELFAREENERGYREWARDNOTIFY,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareEnergyRewardNotify)
  ))
_sym_db.RegisterMessage(WelfareEnergyRewardNotify)
_sym_db.RegisterMessage(WelfareEnergyRewardNotify.TimeRange)

WelfareSignInRequest = _reflection.GeneratedProtocolMessageType('WelfareSignInRequest', (_message.Message,), dict(
  DESCRIPTOR = _WELFARESIGNINREQUEST,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareSignInRequest)
  ))
_sym_db.RegisterMessage(WelfareSignInRequest)

WelfareSignInResponse = _reflection.GeneratedProtocolMessageType('WelfareSignInResponse', (_message.Message,), dict(
  DESCRIPTOR = _WELFARESIGNINRESPONSE,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareSignInResponse)
  ))
_sym_db.RegisterMessage(WelfareSignInResponse)

WelfareNewPlayerGetRequest = _reflection.GeneratedProtocolMessageType('WelfareNewPlayerGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _WELFARENEWPLAYERGETREQUEST,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareNewPlayerGetRequest)
  ))
_sym_db.RegisterMessage(WelfareNewPlayerGetRequest)

WelfareNewPlayerGetResponse = _reflection.GeneratedProtocolMessageType('WelfareNewPlayerGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _WELFARENEWPLAYERGETRESPONSE,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareNewPlayerGetResponse)
  ))
_sym_db.RegisterMessage(WelfareNewPlayerGetResponse)

WelfareLevelRewardGetRequest = _reflection.GeneratedProtocolMessageType('WelfareLevelRewardGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _WELFARELEVELREWARDGETREQUEST,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareLevelRewardGetRequest)
  ))
_sym_db.RegisterMessage(WelfareLevelRewardGetRequest)

WelfareLevelRewardGetResponse = _reflection.GeneratedProtocolMessageType('WelfareLevelRewardGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _WELFARELEVELREWARDGETRESPONSE,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareLevelRewardGetResponse)
  ))
_sym_db.RegisterMessage(WelfareLevelRewardGetResponse)

WelfareEnergyRewardGetReqeust = _reflection.GeneratedProtocolMessageType('WelfareEnergyRewardGetReqeust', (_message.Message,), dict(
  DESCRIPTOR = _WELFAREENERGYREWARDGETREQEUST,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareEnergyRewardGetReqeust)
  ))
_sym_db.RegisterMessage(WelfareEnergyRewardGetReqeust)

WelfareEnergyRewardGetResponse = _reflection.GeneratedProtocolMessageType('WelfareEnergyRewardGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _WELFAREENERGYREWARDGETRESPONSE,
  __module__ = 'welfare_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.WelfareEnergyRewardGetResponse)
  ))
_sym_db.RegisterMessage(WelfareEnergyRewardGetResponse)


# @@protoc_insertion_point(module_scope)
