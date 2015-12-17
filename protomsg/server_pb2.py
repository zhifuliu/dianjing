# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=b'\n\x0cserver.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\"|\n\x06Server\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x36\n\x06status\x18\x03 \x02(\x0e\x32&.Dianjing.protocol.Server.ServerStatus\" \n\x0cServerStatus\x12\x07\n\x03NEW\x10\x01\x12\x07\n\x03HOT\x10\x02\"\'\n\x14GetServerListRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"a\n\x15GetServerListResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12*\n\x07servers\x18\x03 \x03(\x0b\x32\x19.Dianjing.protocol.Server\"6\n\x10StartGameRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x11\n\tserver_id\x18\x02 \x02(\x05\"g\n\x11StartGameResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12\x34\n\x04next\x18\x03 \x01(\x0e\x32\x1e.Dianjing.protocol.NextOperate:\x06OPT_OK'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SERVER_SERVERSTATUS = _descriptor.EnumDescriptor(
  name='ServerStatus',
  full_name='Dianjing.protocol.Server.ServerStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEW', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOT', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=141,
  serialized_end=173,
)
_sym_db.RegisterEnumDescriptor(_SERVER_SERVERSTATUS)


_SERVER = _descriptor.Descriptor(
  name='Server',
  full_name='Dianjing.protocol.Server',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Server.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dianjing.protocol.Server.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Dianjing.protocol.Server.status', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVER_SERVERSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=173,
)


_GETSERVERLISTREQUEST = _descriptor.Descriptor(
  name='GetServerListRequest',
  full_name='Dianjing.protocol.GetServerListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.GetServerListRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
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
  serialized_start=175,
  serialized_end=214,
)


_GETSERVERLISTRESPONSE = _descriptor.Descriptor(
  name='GetServerListResponse',
  full_name='Dianjing.protocol.GetServerListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.GetServerListResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.GetServerListResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='servers', full_name='Dianjing.protocol.GetServerListResponse.servers', index=2,
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
  serialized_start=216,
  serialized_end=313,
)


_STARTGAMEREQUEST = _descriptor.Descriptor(
  name='StartGameRequest',
  full_name='Dianjing.protocol.StartGameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.StartGameRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_id', full_name='Dianjing.protocol.StartGameRequest.server_id', index=1,
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
  serialized_start=315,
  serialized_end=369,
)


_STARTGAMERESPONSE = _descriptor.Descriptor(
  name='StartGameResponse',
  full_name='Dianjing.protocol.StartGameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.StartGameResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.StartGameResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next', full_name='Dianjing.protocol.StartGameResponse.next', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
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
  serialized_start=371,
  serialized_end=474,
)

_SERVER.fields_by_name['status'].enum_type = _SERVER_SERVERSTATUS
_SERVER_SERVERSTATUS.containing_type = _SERVER
_GETSERVERLISTRESPONSE.fields_by_name['servers'].message_type = _SERVER
_STARTGAMERESPONSE.fields_by_name['next'].enum_type = common__pb2._NEXTOPERATE
DESCRIPTOR.message_types_by_name['Server'] = _SERVER
DESCRIPTOR.message_types_by_name['GetServerListRequest'] = _GETSERVERLISTREQUEST
DESCRIPTOR.message_types_by_name['GetServerListResponse'] = _GETSERVERLISTRESPONSE
DESCRIPTOR.message_types_by_name['StartGameRequest'] = _STARTGAMEREQUEST
DESCRIPTOR.message_types_by_name['StartGameResponse'] = _STARTGAMERESPONSE

Server = _reflection.GeneratedProtocolMessageType('Server', (_message.Message,), dict(
  DESCRIPTOR = _SERVER,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Server)
  ))
_sym_db.RegisterMessage(Server)

GetServerListRequest = _reflection.GeneratedProtocolMessageType('GetServerListRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSERVERLISTREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.GetServerListRequest)
  ))
_sym_db.RegisterMessage(GetServerListRequest)

GetServerListResponse = _reflection.GeneratedProtocolMessageType('GetServerListResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSERVERLISTRESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.GetServerListResponse)
  ))
_sym_db.RegisterMessage(GetServerListResponse)

StartGameRequest = _reflection.GeneratedProtocolMessageType('StartGameRequest', (_message.Message,), dict(
  DESCRIPTOR = _STARTGAMEREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.StartGameRequest)
  ))
_sym_db.RegisterMessage(StartGameRequest)

StartGameResponse = _reflection.GeneratedProtocolMessageType('StartGameResponse', (_message.Message,), dict(
  DESCRIPTOR = _STARTGAMERESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.StartGameResponse)
  ))
_sym_db.RegisterMessage(StartGameResponse)


# @@protoc_insertion_point(module_scope)
