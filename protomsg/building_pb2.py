# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: building.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='building.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=b'\n\x0e\x62uilding.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\"\xbf\x01\n\x0e\x42uildingNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12=\n\tbuildings\x18\x02 \x03(\x0b\x32*.Dianjing.protocol.BuildingNotify.Building\x12&\n\x03\x61\x63t\x18\x03 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x1a\x35\n\x08\x42uilding\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05level\x18\x02 \x02(\x05\x12\x0e\n\x06\x65nd_at\x18\x03 \x02(\x03\"5\n\x16\x42uildingLevelUpRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"7\n\x17\x42uildingLevelUpResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BUILDINGNOTIFY_BUILDING = _descriptor.Descriptor(
  name='Building',
  full_name='Dianjing.protocol.BuildingNotify.Building',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.BuildingNotify.Building.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Dianjing.protocol.BuildingNotify.Building.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_at', full_name='Dianjing.protocol.BuildingNotify.Building.end_at', index=2,
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
  serialized_start=190,
  serialized_end=243,
)

_BUILDINGNOTIFY = _descriptor.Descriptor(
  name='BuildingNotify',
  full_name='Dianjing.protocol.BuildingNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BuildingNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buildings', full_name='Dianjing.protocol.BuildingNotify.buildings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.BuildingNotify.act', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BUILDINGNOTIFY_BUILDING, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=243,
)


_BUILDINGLEVELUPREQUEST = _descriptor.Descriptor(
  name='BuildingLevelUpRequest',
  full_name='Dianjing.protocol.BuildingLevelUpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BuildingLevelUpRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.BuildingLevelUpRequest.id', index=1,
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
  serialized_start=245,
  serialized_end=298,
)


_BUILDINGLEVELUPRESPONSE = _descriptor.Descriptor(
  name='BuildingLevelUpResponse',
  full_name='Dianjing.protocol.BuildingLevelUpResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.BuildingLevelUpResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BuildingLevelUpResponse.session', index=1,
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
  serialized_start=300,
  serialized_end=355,
)

_BUILDINGNOTIFY_BUILDING.containing_type = _BUILDINGNOTIFY
_BUILDINGNOTIFY.fields_by_name['buildings'].message_type = _BUILDINGNOTIFY_BUILDING
_BUILDINGNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
DESCRIPTOR.message_types_by_name['BuildingNotify'] = _BUILDINGNOTIFY
DESCRIPTOR.message_types_by_name['BuildingLevelUpRequest'] = _BUILDINGLEVELUPREQUEST
DESCRIPTOR.message_types_by_name['BuildingLevelUpResponse'] = _BUILDINGLEVELUPRESPONSE

BuildingNotify = _reflection.GeneratedProtocolMessageType('BuildingNotify', (_message.Message,), dict(

  Building = _reflection.GeneratedProtocolMessageType('Building', (_message.Message,), dict(
    DESCRIPTOR = _BUILDINGNOTIFY_BUILDING,
    __module__ = 'building_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.BuildingNotify.Building)
    ))
  ,
  DESCRIPTOR = _BUILDINGNOTIFY,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BuildingNotify)
  ))
_sym_db.RegisterMessage(BuildingNotify)
_sym_db.RegisterMessage(BuildingNotify.Building)

BuildingLevelUpRequest = _reflection.GeneratedProtocolMessageType('BuildingLevelUpRequest', (_message.Message,), dict(
  DESCRIPTOR = _BUILDINGLEVELUPREQUEST,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BuildingLevelUpRequest)
  ))
_sym_db.RegisterMessage(BuildingLevelUpRequest)

BuildingLevelUpResponse = _reflection.GeneratedProtocolMessageType('BuildingLevelUpResponse', (_message.Message,), dict(
  DESCRIPTOR = _BUILDINGLEVELUPRESPONSE,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BuildingLevelUpResponse)
  ))
_sym_db.RegisterMessage(BuildingLevelUpResponse)


# @@protoc_insertion_point(module_scope)
