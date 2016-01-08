# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: package.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import item_pb2 as item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='package.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\rpackage.proto\x12\x11\x44ianjing.protocol\x1a\nitem.proto\".\n\x08Resource\x12\x13\n\x0bresource_id\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x05\"\xb0\x01\n\x04\x44rop\x12.\n\tresources\x18\x01 \x03(\x0b\x32\x1b.Dianjing.protocol.Resource\x12+\n\x05items\x18\x02 \x03(\x0b\x32\x1c.Dianjing.protocol.Drop.Item\x1aK\n\x04Item\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x02(\x05\x12\'\n\x02tp\x18\x03 \x02(\x0e\x32\x1b.Dianjing.protocol.ItemType\":\n\x08Property\x12.\n\tresources\x18\x01 \x03(\x0b\x32\x1b.Dianjing.protocol.Resource')
  ,
  dependencies=[item__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='Dianjing.protocol.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='Dianjing.protocol.Resource.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dianjing.protocol.Resource.value', index=1,
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
  serialized_start=48,
  serialized_end=94,
)


_DROP_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Dianjing.protocol.Drop.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Drop.Item.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Dianjing.protocol.Drop.Item.amount', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tp', full_name='Dianjing.protocol.Drop.Item.tp', index=2,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=273,
)

_DROP = _descriptor.Descriptor(
  name='Drop',
  full_name='Dianjing.protocol.Drop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Dianjing.protocol.Drop.resources', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='Dianjing.protocol.Drop.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DROP_ITEM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=273,
)


_PROPERTY = _descriptor.Descriptor(
  name='Property',
  full_name='Dianjing.protocol.Property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Dianjing.protocol.Property.resources', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=275,
  serialized_end=333,
)

_DROP_ITEM.fields_by_name['tp'].enum_type = item__pb2._ITEMTYPE
_DROP_ITEM.containing_type = _DROP
_DROP.fields_by_name['resources'].message_type = _RESOURCE
_DROP.fields_by_name['items'].message_type = _DROP_ITEM
_PROPERTY.fields_by_name['resources'].message_type = _RESOURCE
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
DESCRIPTOR.message_types_by_name['Drop'] = _DROP
DESCRIPTOR.message_types_by_name['Property'] = _PROPERTY

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCE,
  __module__ = 'package_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Resource)
  ))
_sym_db.RegisterMessage(Resource)

Drop = _reflection.GeneratedProtocolMessageType('Drop', (_message.Message,), dict(

  Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
    DESCRIPTOR = _DROP_ITEM,
    __module__ = 'package_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.Drop.Item)
    ))
  ,
  DESCRIPTOR = _DROP,
  __module__ = 'package_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Drop)
  ))
_sym_db.RegisterMessage(Drop)
_sym_db.RegisterMessage(Drop.Item)

Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTY,
  __module__ = 'package_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Property)
  ))
_sym_db.RegisterMessage(Property)


# @@protoc_insertion_point(module_scope)
