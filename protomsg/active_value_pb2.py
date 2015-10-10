# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: active_value.proto

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
  name='active_value.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=b'\n\x12\x61\x63tive_value.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\x1a\rpackage.proto\"\xd9\x01\n\x11\x41\x63tiveValueNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\r\n\x05value\x18\x02 \x02(\x05\x12G\n\x07rewards\x18\x03 \x03(\x0b\x32\x36.Dianjing.protocol.ActiveValueNotify.ActiveValueReward\x1a[\n\x11\x41\x63tiveValueReward\x12\n\n\x02id\x18\x01 \x02(\x05\x12:\n\x06status\x18\x02 \x02(\x0e\x32*.Dianjing.protocol.ActiveValueRewardStatus\"\xda\x01\n\x14\x41\x63tiveFunctionNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12I\n\tfunctions\x18\x03 \x03(\x0b\x32\x36.Dianjing.protocol.ActiveFunctionNotify.ActiveFunction\x1a>\n\x0e\x41\x63tiveFunction\x12\x15\n\rfunction_name\x18\x01 \x02(\t\x12\x15\n\rcurrent_times\x18\x02 \x02(\x05\":\n\x1b\x41\x63tiveValueGetRewardRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"c\n\x1c\x41\x63tiveValueGetRewardResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12%\n\x04\x64rop\x18\x03 \x01(\x0b\x32\x17.Dianjing.protocol.Drop*w\n\x17\x41\x63tiveValueRewardStatus\x12\x1e\n\x1a\x41\x43TIVE_VALUE_REWARD_UNABLE\x10\x01\x12\x1e\n\x1a\x41\x43TIVE_VALUE_REWARD_ENABLE\x10\x02\x12\x1c\n\x18\x41\x43TIVE_VALUE_REWARD_DONE\x10\x03'
  ,
  dependencies=[common__pb2.DESCRIPTOR,package__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ACTIVEVALUEREWARDSTATUS = _descriptor.EnumDescriptor(
  name='ActiveValueRewardStatus',
  full_name='Dianjing.protocol.ActiveValueRewardStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE_VALUE_REWARD_UNABLE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE_VALUE_REWARD_ENABLE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE_VALUE_REWARD_DONE', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=672,
  serialized_end=791,
)
_sym_db.RegisterEnumDescriptor(_ACTIVEVALUEREWARDSTATUS)

ActiveValueRewardStatus = enum_type_wrapper.EnumTypeWrapper(_ACTIVEVALUEREWARDSTATUS)
ACTIVE_VALUE_REWARD_UNABLE = 1
ACTIVE_VALUE_REWARD_ENABLE = 2
ACTIVE_VALUE_REWARD_DONE = 3



_ACTIVEVALUENOTIFY_ACTIVEVALUEREWARD = _descriptor.Descriptor(
  name='ActiveValueReward',
  full_name='Dianjing.protocol.ActiveValueNotify.ActiveValueReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.ActiveValueNotify.ActiveValueReward.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Dianjing.protocol.ActiveValueNotify.ActiveValueReward.status', index=1,
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
  serialized_start=197,
  serialized_end=288,
)

_ACTIVEVALUENOTIFY = _descriptor.Descriptor(
  name='ActiveValueNotify',
  full_name='Dianjing.protocol.ActiveValueNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ActiveValueNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dianjing.protocol.ActiveValueNotify.value', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='Dianjing.protocol.ActiveValueNotify.rewards', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACTIVEVALUENOTIFY_ACTIVEVALUEREWARD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=288,
)


_ACTIVEFUNCTIONNOTIFY_ACTIVEFUNCTION = _descriptor.Descriptor(
  name='ActiveFunction',
  full_name='Dianjing.protocol.ActiveFunctionNotify.ActiveFunction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='function_name', full_name='Dianjing.protocol.ActiveFunctionNotify.ActiveFunction.function_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_times', full_name='Dianjing.protocol.ActiveFunctionNotify.ActiveFunction.current_times', index=1,
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
  serialized_start=447,
  serialized_end=509,
)

_ACTIVEFUNCTIONNOTIFY = _descriptor.Descriptor(
  name='ActiveFunctionNotify',
  full_name='Dianjing.protocol.ActiveFunctionNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ActiveFunctionNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.ActiveFunctionNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functions', full_name='Dianjing.protocol.ActiveFunctionNotify.functions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACTIVEFUNCTIONNOTIFY_ACTIVEFUNCTION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=509,
)


_ACTIVEVALUEGETREWARDREQUEST = _descriptor.Descriptor(
  name='ActiveValueGetRewardRequest',
  full_name='Dianjing.protocol.ActiveValueGetRewardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ActiveValueGetRewardRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.ActiveValueGetRewardRequest.id', index=1,
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
  serialized_start=511,
  serialized_end=569,
)


_ACTIVEVALUEGETREWARDRESPONSE = _descriptor.Descriptor(
  name='ActiveValueGetRewardResponse',
  full_name='Dianjing.protocol.ActiveValueGetRewardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.ActiveValueGetRewardResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ActiveValueGetRewardResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.ActiveValueGetRewardResponse.drop', index=2,
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
  serialized_start=571,
  serialized_end=670,
)

_ACTIVEVALUENOTIFY_ACTIVEVALUEREWARD.fields_by_name['status'].enum_type = _ACTIVEVALUEREWARDSTATUS
_ACTIVEVALUENOTIFY_ACTIVEVALUEREWARD.containing_type = _ACTIVEVALUENOTIFY
_ACTIVEVALUENOTIFY.fields_by_name['rewards'].message_type = _ACTIVEVALUENOTIFY_ACTIVEVALUEREWARD
_ACTIVEFUNCTIONNOTIFY_ACTIVEFUNCTION.containing_type = _ACTIVEFUNCTIONNOTIFY
_ACTIVEFUNCTIONNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_ACTIVEFUNCTIONNOTIFY.fields_by_name['functions'].message_type = _ACTIVEFUNCTIONNOTIFY_ACTIVEFUNCTION
_ACTIVEVALUEGETREWARDRESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
DESCRIPTOR.message_types_by_name['ActiveValueNotify'] = _ACTIVEVALUENOTIFY
DESCRIPTOR.message_types_by_name['ActiveFunctionNotify'] = _ACTIVEFUNCTIONNOTIFY
DESCRIPTOR.message_types_by_name['ActiveValueGetRewardRequest'] = _ACTIVEVALUEGETREWARDREQUEST
DESCRIPTOR.message_types_by_name['ActiveValueGetRewardResponse'] = _ACTIVEVALUEGETREWARDRESPONSE
DESCRIPTOR.enum_types_by_name['ActiveValueRewardStatus'] = _ACTIVEVALUEREWARDSTATUS

ActiveValueNotify = _reflection.GeneratedProtocolMessageType('ActiveValueNotify', (_message.Message,), dict(

  ActiveValueReward = _reflection.GeneratedProtocolMessageType('ActiveValueReward', (_message.Message,), dict(
    DESCRIPTOR = _ACTIVEVALUENOTIFY_ACTIVEVALUEREWARD,
    __module__ = 'active_value_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.ActiveValueNotify.ActiveValueReward)
    ))
  ,
  DESCRIPTOR = _ACTIVEVALUENOTIFY,
  __module__ = 'active_value_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ActiveValueNotify)
  ))
_sym_db.RegisterMessage(ActiveValueNotify)
_sym_db.RegisterMessage(ActiveValueNotify.ActiveValueReward)

ActiveFunctionNotify = _reflection.GeneratedProtocolMessageType('ActiveFunctionNotify', (_message.Message,), dict(

  ActiveFunction = _reflection.GeneratedProtocolMessageType('ActiveFunction', (_message.Message,), dict(
    DESCRIPTOR = _ACTIVEFUNCTIONNOTIFY_ACTIVEFUNCTION,
    __module__ = 'active_value_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.ActiveFunctionNotify.ActiveFunction)
    ))
  ,
  DESCRIPTOR = _ACTIVEFUNCTIONNOTIFY,
  __module__ = 'active_value_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ActiveFunctionNotify)
  ))
_sym_db.RegisterMessage(ActiveFunctionNotify)
_sym_db.RegisterMessage(ActiveFunctionNotify.ActiveFunction)

ActiveValueGetRewardRequest = _reflection.GeneratedProtocolMessageType('ActiveValueGetRewardRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACTIVEVALUEGETREWARDREQUEST,
  __module__ = 'active_value_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ActiveValueGetRewardRequest)
  ))
_sym_db.RegisterMessage(ActiveValueGetRewardRequest)

ActiveValueGetRewardResponse = _reflection.GeneratedProtocolMessageType('ActiveValueGetRewardResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACTIVEVALUEGETREWARDRESPONSE,
  __module__ = 'active_value_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ActiveValueGetRewardResponse)
  ))
_sym_db.RegisterMessage(ActiveValueGetRewardResponse)


# @@protoc_insertion_point(module_scope)