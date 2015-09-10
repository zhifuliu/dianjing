# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=b'\n\ntask.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\"\xc7\x01\n\nTaskNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12\x30\n\x04task\x18\x03 \x03(\x0b\x32\".Dianjing.protocol.TaskNotify.Task\x1aN\n\x04Task\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0b\n\x03num\x18\x02 \x02(\x05\x12-\n\x06status\x18\x03 \x02(\x0e\x32\x1d.Dianjing.protocol.TaskStatus\"1\n\x12TaskAcquireRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"3\n\x13TaskAcquireResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"3\n\x14TaskGetRewardRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"5\n\x15TaskGetRewardResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c*P\n\nTaskStatus\x12\x13\n\x0fTASK_UNRECEIVED\x10\x00\x12\x0e\n\nTASK_DOING\x10\x01\x12\x0f\n\x0bTASK_FINISH\x10\x02\x12\x0c\n\x08TASK_END\x10\x03'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TASKSTATUS = _descriptor.EnumDescriptor(
  name='TaskStatus',
  full_name='Dianjing.protocol.TaskStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TASK_UNRECEIVED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_DOING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_FINISH', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_END', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=461,
  serialized_end=541,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATUS)

TaskStatus = enum_type_wrapper.EnumTypeWrapper(_TASKSTATUS)
TASK_UNRECEIVED = 0
TASK_DOING = 1
TASK_FINISH = 2
TASK_END = 3



_TASKNOTIFY_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='Dianjing.protocol.TaskNotify.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.TaskNotify.Task.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='Dianjing.protocol.TaskNotify.Task.num', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Dianjing.protocol.TaskNotify.Task.status', index=2,
      number=3, type=14, cpp_type=8, label=2,
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
  serialized_start=169,
  serialized_end=247,
)

_TASKNOTIFY = _descriptor.Descriptor(
  name='TaskNotify',
  full_name='Dianjing.protocol.TaskNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.TaskNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.TaskNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task', full_name='Dianjing.protocol.TaskNotify.task', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TASKNOTIFY_TASK, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=247,
)


_TASKACQUIREREQUEST = _descriptor.Descriptor(
  name='TaskAcquireRequest',
  full_name='Dianjing.protocol.TaskAcquireRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.TaskAcquireRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.TaskAcquireRequest.id', index=1,
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
  serialized_start=249,
  serialized_end=298,
)


_TASKACQUIRERESPONSE = _descriptor.Descriptor(
  name='TaskAcquireResponse',
  full_name='Dianjing.protocol.TaskAcquireResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.TaskAcquireResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.TaskAcquireResponse.session', index=1,
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
  serialized_end=351,
)


_TASKGETREWARDREQUEST = _descriptor.Descriptor(
  name='TaskGetRewardRequest',
  full_name='Dianjing.protocol.TaskGetRewardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.TaskGetRewardRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.TaskGetRewardRequest.id', index=1,
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
  serialized_start=353,
  serialized_end=404,
)


_TASKGETREWARDRESPONSE = _descriptor.Descriptor(
  name='TaskGetRewardResponse',
  full_name='Dianjing.protocol.TaskGetRewardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.TaskGetRewardResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.TaskGetRewardResponse.session', index=1,
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
  serialized_start=406,
  serialized_end=459,
)

_TASKNOTIFY_TASK.fields_by_name['status'].enum_type = _TASKSTATUS
_TASKNOTIFY_TASK.containing_type = _TASKNOTIFY
_TASKNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_TASKNOTIFY.fields_by_name['task'].message_type = _TASKNOTIFY_TASK
DESCRIPTOR.message_types_by_name['TaskNotify'] = _TASKNOTIFY
DESCRIPTOR.message_types_by_name['TaskAcquireRequest'] = _TASKACQUIREREQUEST
DESCRIPTOR.message_types_by_name['TaskAcquireResponse'] = _TASKACQUIRERESPONSE
DESCRIPTOR.message_types_by_name['TaskGetRewardRequest'] = _TASKGETREWARDREQUEST
DESCRIPTOR.message_types_by_name['TaskGetRewardResponse'] = _TASKGETREWARDRESPONSE
DESCRIPTOR.enum_types_by_name['TaskStatus'] = _TASKSTATUS

TaskNotify = _reflection.GeneratedProtocolMessageType('TaskNotify', (_message.Message,), dict(

  Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
    DESCRIPTOR = _TASKNOTIFY_TASK,
    __module__ = 'task_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.TaskNotify.Task)
    ))
  ,
  DESCRIPTOR = _TASKNOTIFY,
  __module__ = 'task_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.TaskNotify)
  ))
_sym_db.RegisterMessage(TaskNotify)
_sym_db.RegisterMessage(TaskNotify.Task)

TaskAcquireRequest = _reflection.GeneratedProtocolMessageType('TaskAcquireRequest', (_message.Message,), dict(
  DESCRIPTOR = _TASKACQUIREREQUEST,
  __module__ = 'task_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.TaskAcquireRequest)
  ))
_sym_db.RegisterMessage(TaskAcquireRequest)

TaskAcquireResponse = _reflection.GeneratedProtocolMessageType('TaskAcquireResponse', (_message.Message,), dict(
  DESCRIPTOR = _TASKACQUIRERESPONSE,
  __module__ = 'task_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.TaskAcquireResponse)
  ))
_sym_db.RegisterMessage(TaskAcquireResponse)

TaskGetRewardRequest = _reflection.GeneratedProtocolMessageType('TaskGetRewardRequest', (_message.Message,), dict(
  DESCRIPTOR = _TASKGETREWARDREQUEST,
  __module__ = 'task_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.TaskGetRewardRequest)
  ))
_sym_db.RegisterMessage(TaskGetRewardRequest)

TaskGetRewardResponse = _reflection.GeneratedProtocolMessageType('TaskGetRewardResponse', (_message.Message,), dict(
  DESCRIPTOR = _TASKGETREWARDRESPONSE,
  __module__ = 'task_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.TaskGetRewardResponse)
  ))
_sym_db.RegisterMessage(TaskGetRewardResponse)


# @@protoc_insertion_point(module_scope)
