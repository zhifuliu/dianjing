# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: challenge.proto

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


import match_pb2 as match__pb2
import package_pb2 as package__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='challenge.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x63hallenge.proto\x12\x11\x44ianjing.protocol\x1a\x0bmatch.proto\x1a\rpackage.proto\"W\n\x04\x41rea\x12\n\n\x02id\x18\x01 \x02(\x05\x12-\n\x06status\x18\x02 \x02(\x0e\x32\x1d.Dianjing.protocol.AreaStatus\x12\x14\n\x0c\x63hallenge_id\x18\x03 \x01(\x05\"b\n\x0f\x43hallengeNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x17\n\x0f\x63urrent_area_id\x18\x02 \x02(\x05\x12%\n\x04\x61rea\x18\x03 \x03(\x0b\x32\x17.Dianjing.protocol.Area\"9\n\x15\x43hallengeStartRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07\x61rea_id\x18\x02 \x02(\x05\"\x8a\x01\n\x16\x43hallengeStartResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12+\n\x05match\x18\x03 \x01(\x0b\x32\x1c.Dianjing.protocol.ClubMatch\x12%\n\x04\x64rop\x18\x04 \x01(\x0b\x32\x17.Dianjing.protocol.Drop\">\n\x1a\x43hallengeAreaSwitchRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07\x61rea_id\x18\x02 \x02(\x05\";\n\x1b\x43hallengeAreaSwitchResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c*N\n\nAreaStatus\x12\x16\n\x12\x43HALLENGE_NOT_OPEN\x10\x01\x12\x12\n\x0e\x43HALLENGE_OPEN\x10\x02\x12\x14\n\x10\x43HALLENGE_FINISH\x10\x03')
  ,
  dependencies=[match__pb2.DESCRIPTOR,package__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_AREASTATUS = _descriptor.EnumDescriptor(
  name='AreaStatus',
  full_name='Dianjing.protocol.AreaStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_NOT_OPEN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_OPEN', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_FINISH', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=580,
  serialized_end=658,
)
_sym_db.RegisterEnumDescriptor(_AREASTATUS)

AreaStatus = enum_type_wrapper.EnumTypeWrapper(_AREASTATUS)
CHALLENGE_NOT_OPEN = 1
CHALLENGE_OPEN = 2
CHALLENGE_FINISH = 3



_AREA = _descriptor.Descriptor(
  name='Area',
  full_name='Dianjing.protocol.Area',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Area.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Dianjing.protocol.Area.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='challenge_id', full_name='Dianjing.protocol.Area.challenge_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=66,
  serialized_end=153,
)


_CHALLENGENOTIFY = _descriptor.Descriptor(
  name='ChallengeNotify',
  full_name='Dianjing.protocol.ChallengeNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ChallengeNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_area_id', full_name='Dianjing.protocol.ChallengeNotify.current_area_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area', full_name='Dianjing.protocol.ChallengeNotify.area', index=2,
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
  serialized_start=155,
  serialized_end=253,
)


_CHALLENGESTARTREQUEST = _descriptor.Descriptor(
  name='ChallengeStartRequest',
  full_name='Dianjing.protocol.ChallengeStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ChallengeStartRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_id', full_name='Dianjing.protocol.ChallengeStartRequest.area_id', index=1,
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
  serialized_start=255,
  serialized_end=312,
)


_CHALLENGESTARTRESPONSE = _descriptor.Descriptor(
  name='ChallengeStartResponse',
  full_name='Dianjing.protocol.ChallengeStartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.ChallengeStartResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ChallengeStartResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match', full_name='Dianjing.protocol.ChallengeStartResponse.match', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.ChallengeStartResponse.drop', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=315,
  serialized_end=453,
)


_CHALLENGEAREASWITCHREQUEST = _descriptor.Descriptor(
  name='ChallengeAreaSwitchRequest',
  full_name='Dianjing.protocol.ChallengeAreaSwitchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ChallengeAreaSwitchRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='area_id', full_name='Dianjing.protocol.ChallengeAreaSwitchRequest.area_id', index=1,
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
  serialized_start=455,
  serialized_end=517,
)


_CHALLENGEAREASWITCHRESPONSE = _descriptor.Descriptor(
  name='ChallengeAreaSwitchResponse',
  full_name='Dianjing.protocol.ChallengeAreaSwitchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.ChallengeAreaSwitchResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ChallengeAreaSwitchResponse.session', index=1,
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
  serialized_start=519,
  serialized_end=578,
)

_AREA.fields_by_name['status'].enum_type = _AREASTATUS
_CHALLENGENOTIFY.fields_by_name['area'].message_type = _AREA
_CHALLENGESTARTRESPONSE.fields_by_name['match'].message_type = match__pb2._CLUBMATCH
_CHALLENGESTARTRESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
DESCRIPTOR.message_types_by_name['Area'] = _AREA
DESCRIPTOR.message_types_by_name['ChallengeNotify'] = _CHALLENGENOTIFY
DESCRIPTOR.message_types_by_name['ChallengeStartRequest'] = _CHALLENGESTARTREQUEST
DESCRIPTOR.message_types_by_name['ChallengeStartResponse'] = _CHALLENGESTARTRESPONSE
DESCRIPTOR.message_types_by_name['ChallengeAreaSwitchRequest'] = _CHALLENGEAREASWITCHREQUEST
DESCRIPTOR.message_types_by_name['ChallengeAreaSwitchResponse'] = _CHALLENGEAREASWITCHRESPONSE
DESCRIPTOR.enum_types_by_name['AreaStatus'] = _AREASTATUS

Area = _reflection.GeneratedProtocolMessageType('Area', (_message.Message,), dict(
  DESCRIPTOR = _AREA,
  __module__ = 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Area)
  ))
_sym_db.RegisterMessage(Area)

ChallengeNotify = _reflection.GeneratedProtocolMessageType('ChallengeNotify', (_message.Message,), dict(
  DESCRIPTOR = _CHALLENGENOTIFY,
  __module__ = 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ChallengeNotify)
  ))
_sym_db.RegisterMessage(ChallengeNotify)

ChallengeStartRequest = _reflection.GeneratedProtocolMessageType('ChallengeStartRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHALLENGESTARTREQUEST,
  __module__ = 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ChallengeStartRequest)
  ))
_sym_db.RegisterMessage(ChallengeStartRequest)

ChallengeStartResponse = _reflection.GeneratedProtocolMessageType('ChallengeStartResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHALLENGESTARTRESPONSE,
  __module__ = 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ChallengeStartResponse)
  ))
_sym_db.RegisterMessage(ChallengeStartResponse)

ChallengeAreaSwitchRequest = _reflection.GeneratedProtocolMessageType('ChallengeAreaSwitchRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHALLENGEAREASWITCHREQUEST,
  __module__ = 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ChallengeAreaSwitchRequest)
  ))
_sym_db.RegisterMessage(ChallengeAreaSwitchRequest)

ChallengeAreaSwitchResponse = _reflection.GeneratedProtocolMessageType('ChallengeAreaSwitchResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHALLENGEAREASWITCHRESPONSE,
  __module__ = 'challenge_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ChallengeAreaSwitchResponse)
  ))
_sym_db.RegisterMessage(ChallengeAreaSwitchResponse)


# @@protoc_insertion_point(module_scope)
