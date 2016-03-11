# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bag.proto

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
import package_pb2 as package__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bag.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\tbag.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\x1a\rpackage.proto\"\xc2\x01\n\tEquipment\x12\r\n\x05level\x18\x01 \x02(\x05\x12\x0e\n\x06\x61ttack\x18\x02 \x02(\x05\x12\x16\n\x0e\x61ttack_percent\x18\x03 \x02(\x02\x12\x0f\n\x07\x64\x65\x66\x65nse\x18\x04 \x02(\x05\x12\x17\n\x0f\x64\x65\x66\x65nse_percent\x18\x05 \x02(\x02\x12\x0e\n\x06manage\x18\x06 \x02(\x05\x12\x16\n\x0emanage_percent\x18\x07 \x02(\x02\x12\x11\n\toperation\x18\x08 \x02(\x05\x12\x19\n\x11operation_percent\x18\t \x02(\x02\"g\n\x04Slot\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0f\n\x07item_id\x18\x02 \x02(\x05\x12\x11\n\x06\x61mount\x18\x03 \x01(\x05:\x01\x31\x12/\n\tequipment\x18\x04 \x01(\x0b\x32\x1c.Dianjing.protocol.Equipment\"\xc6\x01\n\x0e\x42\x61gSlotsNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12&\n\x05slots\x18\x03 \x03(\x0b\x32\x17.Dianjing.protocol.Slot\x12\x1c\n\x14\x65quipment_max_amount\x18\x04 \x02(\x05\x12\x1b\n\x13\x66ragment_max_amount\x18\x05 \x02(\x05\x12\x18\n\x10other_max_amount\x18\x06 \x02(\x05\"8\n\x14\x42\x61gSlotsRemoveNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x03(\t\"5\n\x11\x42\x61gItemUseRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\t\"Y\n\x12\x42\x61gItemUseResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12%\n\x04\x64rop\x18\x03 \x01(\x0b\x32\x17.Dianjing.protocol.Drop\"7\n\x13\x42\x61gItemMergeRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\t\"4\n\x14\x42\x61gItemMergeResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"9\n\x15\x42\x61gItemDestroyRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\t\"6\n\x16\x42\x61gItemDestroyResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"Q\n\x1a\x42\x61gEquipmentDestroyRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\t\x12\x11\n\tuse_sycee\x18\x03 \x02(\x08\"b\n\x1b\x42\x61gEquipmentDestroyResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12%\n\x04\x64rop\x18\x03 \x01(\x0b\x32\x17.Dianjing.protocol.Drop\">\n\x1a\x42\x61gEquipmentLevelupRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\t\"l\n\x1b\x42\x61gEquipmentLevelupResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12/\n\tequipment\x18\x03 \x01(\x0b\x32\x1c.Dianjing.protocol.Equipment\"U\n!BagEquipmentLevelupConfirmRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\t\x12\x0e\n\x06single\x18\x03 \x02(\x08\"p\n\"BagEquipmentLevelupConfirmResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12,\n\x06levels\x18\x03 \x03(\x0b\x32\x1c.Dianjing.protocol.Equipment\"K\n\x15\x42\x61gEquipmentOnRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\t\x12\x10\n\x08staff_id\x18\x03 \x02(\x05\"6\n\x16\x42\x61gEquipmentOnResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c')
  ,
  dependencies=[common__pb2.DESCRIPTOR,package__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EQUIPMENT = _descriptor.Descriptor(
  name='Equipment',
  full_name='Dianjing.protocol.Equipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='Dianjing.protocol.Equipment.level', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attack', full_name='Dianjing.protocol.Equipment.attack', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attack_percent', full_name='Dianjing.protocol.Equipment.attack_percent', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defense', full_name='Dianjing.protocol.Equipment.defense', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defense_percent', full_name='Dianjing.protocol.Equipment.defense_percent', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manage', full_name='Dianjing.protocol.Equipment.manage', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manage_percent', full_name='Dianjing.protocol.Equipment.manage_percent', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='Dianjing.protocol.Equipment.operation', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation_percent', full_name='Dianjing.protocol.Equipment.operation_percent', index=8,
      number=9, type=2, cpp_type=6, label=2,
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
  serialized_start=62,
  serialized_end=256,
)


_SLOT = _descriptor.Descriptor(
  name='Slot',
  full_name='Dianjing.protocol.Slot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Slot.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='Dianjing.protocol.Slot.item_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Dianjing.protocol.Slot.amount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipment', full_name='Dianjing.protocol.Slot.equipment', index=3,
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
  serialized_start=258,
  serialized_end=361,
)


_BAGSLOTSNOTIFY = _descriptor.Descriptor(
  name='BagSlotsNotify',
  full_name='Dianjing.protocol.BagSlotsNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagSlotsNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.BagSlotsNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slots', full_name='Dianjing.protocol.BagSlotsNotify.slots', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipment_max_amount', full_name='Dianjing.protocol.BagSlotsNotify.equipment_max_amount', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fragment_max_amount', full_name='Dianjing.protocol.BagSlotsNotify.fragment_max_amount', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='other_max_amount', full_name='Dianjing.protocol.BagSlotsNotify.other_max_amount', index=5,
      number=6, type=5, cpp_type=1, label=2,
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
  serialized_start=364,
  serialized_end=562,
)


_BAGSLOTSREMOVENOTIFY = _descriptor.Descriptor(
  name='BagSlotsRemoveNotify',
  full_name='Dianjing.protocol.BagSlotsRemoveNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagSlotsRemoveNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.BagSlotsRemoveNotify.slot_id', index=1,
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
  serialized_start=564,
  serialized_end=620,
)


_BAGITEMUSEREQUEST = _descriptor.Descriptor(
  name='BagItemUseRequest',
  full_name='Dianjing.protocol.BagItemUseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagItemUseRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.BagItemUseRequest.slot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=622,
  serialized_end=675,
)


_BAGITEMUSERESPONSE = _descriptor.Descriptor(
  name='BagItemUseResponse',
  full_name='Dianjing.protocol.BagItemUseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.BagItemUseResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagItemUseResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.BagItemUseResponse.drop', index=2,
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
  serialized_start=677,
  serialized_end=766,
)


_BAGITEMMERGEREQUEST = _descriptor.Descriptor(
  name='BagItemMergeRequest',
  full_name='Dianjing.protocol.BagItemMergeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagItemMergeRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.BagItemMergeRequest.slot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=768,
  serialized_end=823,
)


_BAGITEMMERGERESPONSE = _descriptor.Descriptor(
  name='BagItemMergeResponse',
  full_name='Dianjing.protocol.BagItemMergeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.BagItemMergeResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagItemMergeResponse.session', index=1,
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
  serialized_start=825,
  serialized_end=877,
)


_BAGITEMDESTROYREQUEST = _descriptor.Descriptor(
  name='BagItemDestroyRequest',
  full_name='Dianjing.protocol.BagItemDestroyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagItemDestroyRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.BagItemDestroyRequest.slot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=879,
  serialized_end=936,
)


_BAGITEMDESTROYRESPONSE = _descriptor.Descriptor(
  name='BagItemDestroyResponse',
  full_name='Dianjing.protocol.BagItemDestroyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.BagItemDestroyResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagItemDestroyResponse.session', index=1,
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
  serialized_start=938,
  serialized_end=992,
)


_BAGEQUIPMENTDESTROYREQUEST = _descriptor.Descriptor(
  name='BagEquipmentDestroyRequest',
  full_name='Dianjing.protocol.BagEquipmentDestroyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagEquipmentDestroyRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.BagEquipmentDestroyRequest.slot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_sycee', full_name='Dianjing.protocol.BagEquipmentDestroyRequest.use_sycee', index=2,
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
  serialized_start=994,
  serialized_end=1075,
)


_BAGEQUIPMENTDESTROYRESPONSE = _descriptor.Descriptor(
  name='BagEquipmentDestroyResponse',
  full_name='Dianjing.protocol.BagEquipmentDestroyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.BagEquipmentDestroyResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagEquipmentDestroyResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.BagEquipmentDestroyResponse.drop', index=2,
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
  serialized_start=1077,
  serialized_end=1175,
)


_BAGEQUIPMENTLEVELUPREQUEST = _descriptor.Descriptor(
  name='BagEquipmentLevelupRequest',
  full_name='Dianjing.protocol.BagEquipmentLevelupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagEquipmentLevelupRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.BagEquipmentLevelupRequest.slot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1177,
  serialized_end=1239,
)


_BAGEQUIPMENTLEVELUPRESPONSE = _descriptor.Descriptor(
  name='BagEquipmentLevelupResponse',
  full_name='Dianjing.protocol.BagEquipmentLevelupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.BagEquipmentLevelupResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagEquipmentLevelupResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipment', full_name='Dianjing.protocol.BagEquipmentLevelupResponse.equipment', index=2,
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
  serialized_start=1241,
  serialized_end=1349,
)


_BAGEQUIPMENTLEVELUPCONFIRMREQUEST = _descriptor.Descriptor(
  name='BagEquipmentLevelupConfirmRequest',
  full_name='Dianjing.protocol.BagEquipmentLevelupConfirmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagEquipmentLevelupConfirmRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.BagEquipmentLevelupConfirmRequest.slot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='single', full_name='Dianjing.protocol.BagEquipmentLevelupConfirmRequest.single', index=2,
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
  serialized_start=1351,
  serialized_end=1436,
)


_BAGEQUIPMENTLEVELUPCONFIRMRESPONSE = _descriptor.Descriptor(
  name='BagEquipmentLevelupConfirmResponse',
  full_name='Dianjing.protocol.BagEquipmentLevelupConfirmResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.BagEquipmentLevelupConfirmResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagEquipmentLevelupConfirmResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='levels', full_name='Dianjing.protocol.BagEquipmentLevelupConfirmResponse.levels', index=2,
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
  serialized_start=1438,
  serialized_end=1550,
)


_BAGEQUIPMENTONREQUEST = _descriptor.Descriptor(
  name='BagEquipmentOnRequest',
  full_name='Dianjing.protocol.BagEquipmentOnRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagEquipmentOnRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.BagEquipmentOnRequest.slot_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_id', full_name='Dianjing.protocol.BagEquipmentOnRequest.staff_id', index=2,
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
  serialized_start=1552,
  serialized_end=1627,
)


_BAGEQUIPMENTONRESPONSE = _descriptor.Descriptor(
  name='BagEquipmentOnResponse',
  full_name='Dianjing.protocol.BagEquipmentOnResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.BagEquipmentOnResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.BagEquipmentOnResponse.session', index=1,
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
  serialized_start=1629,
  serialized_end=1683,
)

_SLOT.fields_by_name['equipment'].message_type = _EQUIPMENT
_BAGSLOTSNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_BAGSLOTSNOTIFY.fields_by_name['slots'].message_type = _SLOT
_BAGITEMUSERESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
_BAGEQUIPMENTDESTROYRESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
_BAGEQUIPMENTLEVELUPRESPONSE.fields_by_name['equipment'].message_type = _EQUIPMENT
_BAGEQUIPMENTLEVELUPCONFIRMRESPONSE.fields_by_name['levels'].message_type = _EQUIPMENT
DESCRIPTOR.message_types_by_name['Equipment'] = _EQUIPMENT
DESCRIPTOR.message_types_by_name['Slot'] = _SLOT
DESCRIPTOR.message_types_by_name['BagSlotsNotify'] = _BAGSLOTSNOTIFY
DESCRIPTOR.message_types_by_name['BagSlotsRemoveNotify'] = _BAGSLOTSREMOVENOTIFY
DESCRIPTOR.message_types_by_name['BagItemUseRequest'] = _BAGITEMUSEREQUEST
DESCRIPTOR.message_types_by_name['BagItemUseResponse'] = _BAGITEMUSERESPONSE
DESCRIPTOR.message_types_by_name['BagItemMergeRequest'] = _BAGITEMMERGEREQUEST
DESCRIPTOR.message_types_by_name['BagItemMergeResponse'] = _BAGITEMMERGERESPONSE
DESCRIPTOR.message_types_by_name['BagItemDestroyRequest'] = _BAGITEMDESTROYREQUEST
DESCRIPTOR.message_types_by_name['BagItemDestroyResponse'] = _BAGITEMDESTROYRESPONSE
DESCRIPTOR.message_types_by_name['BagEquipmentDestroyRequest'] = _BAGEQUIPMENTDESTROYREQUEST
DESCRIPTOR.message_types_by_name['BagEquipmentDestroyResponse'] = _BAGEQUIPMENTDESTROYRESPONSE
DESCRIPTOR.message_types_by_name['BagEquipmentLevelupRequest'] = _BAGEQUIPMENTLEVELUPREQUEST
DESCRIPTOR.message_types_by_name['BagEquipmentLevelupResponse'] = _BAGEQUIPMENTLEVELUPRESPONSE
DESCRIPTOR.message_types_by_name['BagEquipmentLevelupConfirmRequest'] = _BAGEQUIPMENTLEVELUPCONFIRMREQUEST
DESCRIPTOR.message_types_by_name['BagEquipmentLevelupConfirmResponse'] = _BAGEQUIPMENTLEVELUPCONFIRMRESPONSE
DESCRIPTOR.message_types_by_name['BagEquipmentOnRequest'] = _BAGEQUIPMENTONREQUEST
DESCRIPTOR.message_types_by_name['BagEquipmentOnResponse'] = _BAGEQUIPMENTONRESPONSE

Equipment = _reflection.GeneratedProtocolMessageType('Equipment', (_message.Message,), dict(
  DESCRIPTOR = _EQUIPMENT,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Equipment)
  ))
_sym_db.RegisterMessage(Equipment)

Slot = _reflection.GeneratedProtocolMessageType('Slot', (_message.Message,), dict(
  DESCRIPTOR = _SLOT,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Slot)
  ))
_sym_db.RegisterMessage(Slot)

BagSlotsNotify = _reflection.GeneratedProtocolMessageType('BagSlotsNotify', (_message.Message,), dict(
  DESCRIPTOR = _BAGSLOTSNOTIFY,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagSlotsNotify)
  ))
_sym_db.RegisterMessage(BagSlotsNotify)

BagSlotsRemoveNotify = _reflection.GeneratedProtocolMessageType('BagSlotsRemoveNotify', (_message.Message,), dict(
  DESCRIPTOR = _BAGSLOTSREMOVENOTIFY,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagSlotsRemoveNotify)
  ))
_sym_db.RegisterMessage(BagSlotsRemoveNotify)

BagItemUseRequest = _reflection.GeneratedProtocolMessageType('BagItemUseRequest', (_message.Message,), dict(
  DESCRIPTOR = _BAGITEMUSEREQUEST,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagItemUseRequest)
  ))
_sym_db.RegisterMessage(BagItemUseRequest)

BagItemUseResponse = _reflection.GeneratedProtocolMessageType('BagItemUseResponse', (_message.Message,), dict(
  DESCRIPTOR = _BAGITEMUSERESPONSE,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagItemUseResponse)
  ))
_sym_db.RegisterMessage(BagItemUseResponse)

BagItemMergeRequest = _reflection.GeneratedProtocolMessageType('BagItemMergeRequest', (_message.Message,), dict(
  DESCRIPTOR = _BAGITEMMERGEREQUEST,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagItemMergeRequest)
  ))
_sym_db.RegisterMessage(BagItemMergeRequest)

BagItemMergeResponse = _reflection.GeneratedProtocolMessageType('BagItemMergeResponse', (_message.Message,), dict(
  DESCRIPTOR = _BAGITEMMERGERESPONSE,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagItemMergeResponse)
  ))
_sym_db.RegisterMessage(BagItemMergeResponse)

BagItemDestroyRequest = _reflection.GeneratedProtocolMessageType('BagItemDestroyRequest', (_message.Message,), dict(
  DESCRIPTOR = _BAGITEMDESTROYREQUEST,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagItemDestroyRequest)
  ))
_sym_db.RegisterMessage(BagItemDestroyRequest)

BagItemDestroyResponse = _reflection.GeneratedProtocolMessageType('BagItemDestroyResponse', (_message.Message,), dict(
  DESCRIPTOR = _BAGITEMDESTROYRESPONSE,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagItemDestroyResponse)
  ))
_sym_db.RegisterMessage(BagItemDestroyResponse)

BagEquipmentDestroyRequest = _reflection.GeneratedProtocolMessageType('BagEquipmentDestroyRequest', (_message.Message,), dict(
  DESCRIPTOR = _BAGEQUIPMENTDESTROYREQUEST,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagEquipmentDestroyRequest)
  ))
_sym_db.RegisterMessage(BagEquipmentDestroyRequest)

BagEquipmentDestroyResponse = _reflection.GeneratedProtocolMessageType('BagEquipmentDestroyResponse', (_message.Message,), dict(
  DESCRIPTOR = _BAGEQUIPMENTDESTROYRESPONSE,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagEquipmentDestroyResponse)
  ))
_sym_db.RegisterMessage(BagEquipmentDestroyResponse)

BagEquipmentLevelupRequest = _reflection.GeneratedProtocolMessageType('BagEquipmentLevelupRequest', (_message.Message,), dict(
  DESCRIPTOR = _BAGEQUIPMENTLEVELUPREQUEST,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagEquipmentLevelupRequest)
  ))
_sym_db.RegisterMessage(BagEquipmentLevelupRequest)

BagEquipmentLevelupResponse = _reflection.GeneratedProtocolMessageType('BagEquipmentLevelupResponse', (_message.Message,), dict(
  DESCRIPTOR = _BAGEQUIPMENTLEVELUPRESPONSE,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagEquipmentLevelupResponse)
  ))
_sym_db.RegisterMessage(BagEquipmentLevelupResponse)

BagEquipmentLevelupConfirmRequest = _reflection.GeneratedProtocolMessageType('BagEquipmentLevelupConfirmRequest', (_message.Message,), dict(
  DESCRIPTOR = _BAGEQUIPMENTLEVELUPCONFIRMREQUEST,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagEquipmentLevelupConfirmRequest)
  ))
_sym_db.RegisterMessage(BagEquipmentLevelupConfirmRequest)

BagEquipmentLevelupConfirmResponse = _reflection.GeneratedProtocolMessageType('BagEquipmentLevelupConfirmResponse', (_message.Message,), dict(
  DESCRIPTOR = _BAGEQUIPMENTLEVELUPCONFIRMRESPONSE,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagEquipmentLevelupConfirmResponse)
  ))
_sym_db.RegisterMessage(BagEquipmentLevelupConfirmResponse)

BagEquipmentOnRequest = _reflection.GeneratedProtocolMessageType('BagEquipmentOnRequest', (_message.Message,), dict(
  DESCRIPTOR = _BAGEQUIPMENTONREQUEST,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagEquipmentOnRequest)
  ))
_sym_db.RegisterMessage(BagEquipmentOnRequest)

BagEquipmentOnResponse = _reflection.GeneratedProtocolMessageType('BagEquipmentOnResponse', (_message.Message,), dict(
  DESCRIPTOR = _BAGEQUIPMENTONRESPONSE,
  __module__ = 'bag_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.BagEquipmentOnResponse)
  ))
_sym_db.RegisterMessage(BagEquipmentOnResponse)


# @@protoc_insertion_point(module_scope)
