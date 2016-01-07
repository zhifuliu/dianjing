# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: item.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='item.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\nitem.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\"\xcd\x01\n\tAttribute\x12\x0c\n\x04star\x18\x01 \x02(\x05\x12\r\n\x05luoji\x18\x02 \x01(\x05\x12\x0e\n\x06minjie\x18\x03 \x01(\x05\x12\r\n\x05lilun\x18\x04 \x01(\x05\x12\x0e\n\x06wuxing\x18\x05 \x01(\x05\x12\r\n\x05meili\x18\x06 \x01(\x05\x12\x0e\n\x06\x63\x61ozuo\x18\x07 \x01(\x05\x12\x10\n\x08jingying\x18\x08 \x01(\x05\x12\x0f\n\x07\x62\x61obing\x18\t \x01(\x05\x12\x0f\n\x07zhanshu\x18\n \x01(\x05\x12\x0f\n\x07\x62iaoyan\x18\x0b \x01(\x05\x12\x10\n\x08yingxiao\x18\x0c \x01(\x05\"\x84\x01\n\x04Item\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0b\n\x03oid\x18\x02 \x02(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x02(\x05\x12\'\n\x02tp\x18\x04 \x02(\x0e\x32\x1b.Dianjing.protocol.ItemType\x12*\n\x04\x61ttr\x18\x05 \x01(\x0b\x32\x1c.Dianjing.protocol.Attribute\"m\n\nItemNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12&\n\x05items\x18\x03 \x03(\x0b\x32\x17.Dianjing.protocol.Item\"0\n\x10ItemRemoveNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0b\n\x03ids\x18\x02 \x03(\t*\xa3\x01\n\x08ItemType\x12\x1c\n\x18ITEM_TRAINING_EXPENDABLE\x10\x01\x12\x13\n\x0fITEM_SHOP_GOODS\x10\x02\x12\x1d\n\x19ITEM_BUILDING_CERTIFICATE\x10\x03\x12\x1c\n\x18ITEM_SKILL_TRAINING_BOOK\x10\x04\x12\x12\n\x0eITEM_EQUIPMENT\x10\x0b\x12\x13\n\x0fITEM_STAFF_CARD\x10\x15')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ITEMTYPE = _descriptor.EnumDescriptor(
  name='ItemType',
  full_name='Dianjing.protocol.ItemType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_TRAINING_EXPENDABLE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SHOP_GOODS', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_BUILDING_CERTIFICATE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SKILL_TRAINING_BOOK', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EQUIPMENT', index=4, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_STAFF_CARD', index=5, number=21,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=552,
  serialized_end=715,
)
_sym_db.RegisterEnumDescriptor(_ITEMTYPE)

ItemType = enum_type_wrapper.EnumTypeWrapper(_ITEMTYPE)
ITEM_TRAINING_EXPENDABLE = 1
ITEM_SHOP_GOODS = 2
ITEM_BUILDING_CERTIFICATE = 3
ITEM_SKILL_TRAINING_BOOK = 4
ITEM_EQUIPMENT = 11
ITEM_STAFF_CARD = 21



_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='Dianjing.protocol.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='star', full_name='Dianjing.protocol.Attribute.star', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='luoji', full_name='Dianjing.protocol.Attribute.luoji', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minjie', full_name='Dianjing.protocol.Attribute.minjie', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lilun', full_name='Dianjing.protocol.Attribute.lilun', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wuxing', full_name='Dianjing.protocol.Attribute.wuxing', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meili', full_name='Dianjing.protocol.Attribute.meili', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caozuo', full_name='Dianjing.protocol.Attribute.caozuo', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jingying', full_name='Dianjing.protocol.Attribute.jingying', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baobing', full_name='Dianjing.protocol.Attribute.baobing', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zhanshu', full_name='Dianjing.protocol.Attribute.zhanshu', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biaoyan', full_name='Dianjing.protocol.Attribute.biaoyan', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yingxiao', full_name='Dianjing.protocol.Attribute.yingxiao', index=11,
      number=12, type=5, cpp_type=1, label=1,
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
  serialized_end=253,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Dianjing.protocol.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Item.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oid', full_name='Dianjing.protocol.Item.oid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Dianjing.protocol.Item.amount', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tp', full_name='Dianjing.protocol.Item.tp', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr', full_name='Dianjing.protocol.Item.attr', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=256,
  serialized_end=388,
)


_ITEMNOTIFY = _descriptor.Descriptor(
  name='ItemNotify',
  full_name='Dianjing.protocol.ItemNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ItemNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.ItemNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='Dianjing.protocol.ItemNotify.items', index=2,
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
  serialized_start=390,
  serialized_end=499,
)


_ITEMREMOVENOTIFY = _descriptor.Descriptor(
  name='ItemRemoveNotify',
  full_name='Dianjing.protocol.ItemRemoveNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ItemRemoveNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ids', full_name='Dianjing.protocol.ItemRemoveNotify.ids', index=1,
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
  serialized_start=501,
  serialized_end=549,
)

_ITEM.fields_by_name['tp'].enum_type = _ITEMTYPE
_ITEM.fields_by_name['attr'].message_type = _ATTRIBUTE
_ITEMNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_ITEMNOTIFY.fields_by_name['items'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Attribute'] = _ATTRIBUTE
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['ItemNotify'] = _ITEMNOTIFY
DESCRIPTOR.message_types_by_name['ItemRemoveNotify'] = _ITEMREMOVENOTIFY
DESCRIPTOR.enum_types_by_name['ItemType'] = _ITEMTYPE

Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTE,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Attribute)
  ))
_sym_db.RegisterMessage(Attribute)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Item)
  ))
_sym_db.RegisterMessage(Item)

ItemNotify = _reflection.GeneratedProtocolMessageType('ItemNotify', (_message.Message,), dict(
  DESCRIPTOR = _ITEMNOTIFY,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ItemNotify)
  ))
_sym_db.RegisterMessage(ItemNotify)

ItemRemoveNotify = _reflection.GeneratedProtocolMessageType('ItemRemoveNotify', (_message.Message,), dict(
  DESCRIPTOR = _ITEMREMOVENOTIFY,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ItemRemoveNotify)
  ))
_sym_db.RegisterMessage(ItemRemoveNotify)


# @@protoc_insertion_point(module_scope)
