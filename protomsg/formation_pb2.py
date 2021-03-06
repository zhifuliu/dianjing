# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: formation.proto

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
  name='formation.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x66ormation.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\"-\n\rSkillSequence\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08staff_id\x18\x02 \x03(\t\"`\n\x1cSkillSequenceSetStaffRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0e\n\x06seq_id\x18\x02 \x02(\x05\x12\r\n\x05index\x18\x03 \x02(\x05\x12\x10\n\x08staff_id\x18\x04 \x02(\t\"=\n\x1dSkillSequenceSetStaffResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"\xb0\x01\n\rFormationSlot\x12\x0f\n\x07slot_id\x18\x01 \x02(\x05\x12\x36\n\x06status\x18\x02 \x02(\x0e\x32&.Dianjing.protocol.FormationSlotStatus\x12\x10\n\x08position\x18\x03 \x01(\x05\x12\x10\n\x08staff_id\x18\x04 \x01(\t\x12\x0f\n\x07unit_id\x18\x05 \x01(\x05\x12\x11\n\tstaff_oid\x18\x06 \x01(\x05\x12\x0e\n\x06policy\x18\x07 \x01(\x05\"\xb9\x01\n\x13\x46ormationSlotNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12/\n\x05slots\x18\x03 \x03(\x0b\x32 .Dianjing.protocol.FormationSlot\x12\x38\n\x0eskill_sequence\x18\x04 \x03(\x0b\x32 .Dianjing.protocol.SkillSequence\"\xcc\x01\n\x0f\x46ormationNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12?\n\tformation\x18\x03 \x03(\x0b\x32,.Dianjing.protocol.FormationNotify.Formation\x12\x17\n\x0fusing_formation\x18\x04 \x02(\x05\x1a&\n\tFormation\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05level\x18\x02 \x02(\x05\"N\n\x18\x46ormationSetStaffRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\x05\x12\x10\n\x08staff_id\x18\x03 \x02(\t\"9\n\x19\x46ormationSetStaffResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"L\n\x17\x46ormationSetUnitRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\x05\x12\x0f\n\x07unit_id\x18\x03 \x02(\x05\"8\n\x18\x46ormationSetUnitResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\">\n\x11SyncFormationSlot\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05index\x18\x02 \x02(\x05\x12\x0e\n\x06policy\x18\x03 \x02(\x05\"5\n\x16\x46ormationActiveRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"7\n\x17\x46ormationActiveResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"6\n\x17\x46ormationLevelUpRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"8\n\x18\x46ormationLevelUpResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"2\n\x13\x46ormationUseRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"4\n\x14\x46ormationUseResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c*d\n\x13\x46ormationSlotStatus\x12\x1b\n\x17\x46ORMATION_SLOT_NOT_OPEN\x10\x00\x12\x18\n\x14\x46ORMATION_SLOT_EMPTY\x10\x01\x12\x16\n\x12\x46ORMATION_SLOT_USE\x10\x02')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FORMATIONSLOTSTATUS = _descriptor.EnumDescriptor(
  name='FormationSlotStatus',
  full_name='Dianjing.protocol.FormationSlotStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORMATION_SLOT_NOT_OPEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMATION_SLOT_EMPTY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMATION_SLOT_USE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1505,
  serialized_end=1605,
)
_sym_db.RegisterEnumDescriptor(_FORMATIONSLOTSTATUS)

FormationSlotStatus = enum_type_wrapper.EnumTypeWrapper(_FORMATIONSLOTSTATUS)
FORMATION_SLOT_NOT_OPEN = 0
FORMATION_SLOT_EMPTY = 1
FORMATION_SLOT_USE = 2



_SKILLSEQUENCE = _descriptor.Descriptor(
  name='SkillSequence',
  full_name='Dianjing.protocol.SkillSequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.SkillSequence.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_id', full_name='Dianjing.protocol.SkillSequence.staff_id', index=1,
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
  serialized_start=52,
  serialized_end=97,
)


_SKILLSEQUENCESETSTAFFREQUEST = _descriptor.Descriptor(
  name='SkillSequenceSetStaffRequest',
  full_name='Dianjing.protocol.SkillSequenceSetStaffRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.SkillSequenceSetStaffRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq_id', full_name='Dianjing.protocol.SkillSequenceSetStaffRequest.seq_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='Dianjing.protocol.SkillSequenceSetStaffRequest.index', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_id', full_name='Dianjing.protocol.SkillSequenceSetStaffRequest.staff_id', index=3,
      number=4, type=9, cpp_type=9, label=2,
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
  serialized_start=99,
  serialized_end=195,
)


_SKILLSEQUENCESETSTAFFRESPONSE = _descriptor.Descriptor(
  name='SkillSequenceSetStaffResponse',
  full_name='Dianjing.protocol.SkillSequenceSetStaffResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.SkillSequenceSetStaffResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.SkillSequenceSetStaffResponse.session', index=1,
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
  serialized_start=197,
  serialized_end=258,
)


_FORMATIONSLOT = _descriptor.Descriptor(
  name='FormationSlot',
  full_name='Dianjing.protocol.FormationSlot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.FormationSlot.slot_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Dianjing.protocol.FormationSlot.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='Dianjing.protocol.FormationSlot.position', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_id', full_name='Dianjing.protocol.FormationSlot.staff_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='Dianjing.protocol.FormationSlot.unit_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_oid', full_name='Dianjing.protocol.FormationSlot.staff_oid', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy', full_name='Dianjing.protocol.FormationSlot.policy', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=261,
  serialized_end=437,
)


_FORMATIONSLOTNOTIFY = _descriptor.Descriptor(
  name='FormationSlotNotify',
  full_name='Dianjing.protocol.FormationSlotNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationSlotNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.FormationSlotNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slots', full_name='Dianjing.protocol.FormationSlotNotify.slots', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill_sequence', full_name='Dianjing.protocol.FormationSlotNotify.skill_sequence', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=440,
  serialized_end=625,
)


_FORMATIONNOTIFY_FORMATION = _descriptor.Descriptor(
  name='Formation',
  full_name='Dianjing.protocol.FormationNotify.Formation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.FormationNotify.Formation.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Dianjing.protocol.FormationNotify.Formation.level', index=1,
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
  serialized_start=794,
  serialized_end=832,
)

_FORMATIONNOTIFY = _descriptor.Descriptor(
  name='FormationNotify',
  full_name='Dianjing.protocol.FormationNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.FormationNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='formation', full_name='Dianjing.protocol.FormationNotify.formation', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='using_formation', full_name='Dianjing.protocol.FormationNotify.using_formation', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FORMATIONNOTIFY_FORMATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=832,
)


_FORMATIONSETSTAFFREQUEST = _descriptor.Descriptor(
  name='FormationSetStaffRequest',
  full_name='Dianjing.protocol.FormationSetStaffRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationSetStaffRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.FormationSetStaffRequest.slot_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_id', full_name='Dianjing.protocol.FormationSetStaffRequest.staff_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=834,
  serialized_end=912,
)


_FORMATIONSETSTAFFRESPONSE = _descriptor.Descriptor(
  name='FormationSetStaffResponse',
  full_name='Dianjing.protocol.FormationSetStaffResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FormationSetStaffResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationSetStaffResponse.session', index=1,
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
  serialized_start=914,
  serialized_end=971,
)


_FORMATIONSETUNITREQUEST = _descriptor.Descriptor(
  name='FormationSetUnitRequest',
  full_name='Dianjing.protocol.FormationSetUnitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationSetUnitRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.FormationSetUnitRequest.slot_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='Dianjing.protocol.FormationSetUnitRequest.unit_id', index=2,
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
  serialized_start=973,
  serialized_end=1049,
)


_FORMATIONSETUNITRESPONSE = _descriptor.Descriptor(
  name='FormationSetUnitResponse',
  full_name='Dianjing.protocol.FormationSetUnitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FormationSetUnitResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationSetUnitResponse.session', index=1,
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
  serialized_start=1051,
  serialized_end=1107,
)


_SYNCFORMATIONSLOT = _descriptor.Descriptor(
  name='SyncFormationSlot',
  full_name='Dianjing.protocol.SyncFormationSlot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.SyncFormationSlot.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='Dianjing.protocol.SyncFormationSlot.index', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy', full_name='Dianjing.protocol.SyncFormationSlot.policy', index=2,
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
  serialized_start=1109,
  serialized_end=1171,
)


_FORMATIONACTIVEREQUEST = _descriptor.Descriptor(
  name='FormationActiveRequest',
  full_name='Dianjing.protocol.FormationActiveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationActiveRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.FormationActiveRequest.id', index=1,
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
  serialized_start=1173,
  serialized_end=1226,
)


_FORMATIONACTIVERESPONSE = _descriptor.Descriptor(
  name='FormationActiveResponse',
  full_name='Dianjing.protocol.FormationActiveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FormationActiveResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationActiveResponse.session', index=1,
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
  serialized_start=1228,
  serialized_end=1283,
)


_FORMATIONLEVELUPREQUEST = _descriptor.Descriptor(
  name='FormationLevelUpRequest',
  full_name='Dianjing.protocol.FormationLevelUpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationLevelUpRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.FormationLevelUpRequest.id', index=1,
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
  serialized_start=1285,
  serialized_end=1339,
)


_FORMATIONLEVELUPRESPONSE = _descriptor.Descriptor(
  name='FormationLevelUpResponse',
  full_name='Dianjing.protocol.FormationLevelUpResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FormationLevelUpResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationLevelUpResponse.session', index=1,
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
  serialized_start=1341,
  serialized_end=1397,
)


_FORMATIONUSEREQUEST = _descriptor.Descriptor(
  name='FormationUseRequest',
  full_name='Dianjing.protocol.FormationUseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationUseRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.FormationUseRequest.id', index=1,
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
  serialized_start=1399,
  serialized_end=1449,
)


_FORMATIONUSERESPONSE = _descriptor.Descriptor(
  name='FormationUseResponse',
  full_name='Dianjing.protocol.FormationUseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FormationUseResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationUseResponse.session', index=1,
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
  serialized_start=1451,
  serialized_end=1503,
)

_FORMATIONSLOT.fields_by_name['status'].enum_type = _FORMATIONSLOTSTATUS
_FORMATIONSLOTNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_FORMATIONSLOTNOTIFY.fields_by_name['slots'].message_type = _FORMATIONSLOT
_FORMATIONSLOTNOTIFY.fields_by_name['skill_sequence'].message_type = _SKILLSEQUENCE
_FORMATIONNOTIFY_FORMATION.containing_type = _FORMATIONNOTIFY
_FORMATIONNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_FORMATIONNOTIFY.fields_by_name['formation'].message_type = _FORMATIONNOTIFY_FORMATION
DESCRIPTOR.message_types_by_name['SkillSequence'] = _SKILLSEQUENCE
DESCRIPTOR.message_types_by_name['SkillSequenceSetStaffRequest'] = _SKILLSEQUENCESETSTAFFREQUEST
DESCRIPTOR.message_types_by_name['SkillSequenceSetStaffResponse'] = _SKILLSEQUENCESETSTAFFRESPONSE
DESCRIPTOR.message_types_by_name['FormationSlot'] = _FORMATIONSLOT
DESCRIPTOR.message_types_by_name['FormationSlotNotify'] = _FORMATIONSLOTNOTIFY
DESCRIPTOR.message_types_by_name['FormationNotify'] = _FORMATIONNOTIFY
DESCRIPTOR.message_types_by_name['FormationSetStaffRequest'] = _FORMATIONSETSTAFFREQUEST
DESCRIPTOR.message_types_by_name['FormationSetStaffResponse'] = _FORMATIONSETSTAFFRESPONSE
DESCRIPTOR.message_types_by_name['FormationSetUnitRequest'] = _FORMATIONSETUNITREQUEST
DESCRIPTOR.message_types_by_name['FormationSetUnitResponse'] = _FORMATIONSETUNITRESPONSE
DESCRIPTOR.message_types_by_name['SyncFormationSlot'] = _SYNCFORMATIONSLOT
DESCRIPTOR.message_types_by_name['FormationActiveRequest'] = _FORMATIONACTIVEREQUEST
DESCRIPTOR.message_types_by_name['FormationActiveResponse'] = _FORMATIONACTIVERESPONSE
DESCRIPTOR.message_types_by_name['FormationLevelUpRequest'] = _FORMATIONLEVELUPREQUEST
DESCRIPTOR.message_types_by_name['FormationLevelUpResponse'] = _FORMATIONLEVELUPRESPONSE
DESCRIPTOR.message_types_by_name['FormationUseRequest'] = _FORMATIONUSEREQUEST
DESCRIPTOR.message_types_by_name['FormationUseResponse'] = _FORMATIONUSERESPONSE
DESCRIPTOR.enum_types_by_name['FormationSlotStatus'] = _FORMATIONSLOTSTATUS

SkillSequence = _reflection.GeneratedProtocolMessageType('SkillSequence', (_message.Message,), dict(
  DESCRIPTOR = _SKILLSEQUENCE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.SkillSequence)
  ))
_sym_db.RegisterMessage(SkillSequence)

SkillSequenceSetStaffRequest = _reflection.GeneratedProtocolMessageType('SkillSequenceSetStaffRequest', (_message.Message,), dict(
  DESCRIPTOR = _SKILLSEQUENCESETSTAFFREQUEST,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.SkillSequenceSetStaffRequest)
  ))
_sym_db.RegisterMessage(SkillSequenceSetStaffRequest)

SkillSequenceSetStaffResponse = _reflection.GeneratedProtocolMessageType('SkillSequenceSetStaffResponse', (_message.Message,), dict(
  DESCRIPTOR = _SKILLSEQUENCESETSTAFFRESPONSE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.SkillSequenceSetStaffResponse)
  ))
_sym_db.RegisterMessage(SkillSequenceSetStaffResponse)

FormationSlot = _reflection.GeneratedProtocolMessageType('FormationSlot', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSLOT,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSlot)
  ))
_sym_db.RegisterMessage(FormationSlot)

FormationSlotNotify = _reflection.GeneratedProtocolMessageType('FormationSlotNotify', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSLOTNOTIFY,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSlotNotify)
  ))
_sym_db.RegisterMessage(FormationSlotNotify)

FormationNotify = _reflection.GeneratedProtocolMessageType('FormationNotify', (_message.Message,), dict(

  Formation = _reflection.GeneratedProtocolMessageType('Formation', (_message.Message,), dict(
    DESCRIPTOR = _FORMATIONNOTIFY_FORMATION,
    __module__ = 'formation_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationNotify.Formation)
    ))
  ,
  DESCRIPTOR = _FORMATIONNOTIFY,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationNotify)
  ))
_sym_db.RegisterMessage(FormationNotify)
_sym_db.RegisterMessage(FormationNotify.Formation)

FormationSetStaffRequest = _reflection.GeneratedProtocolMessageType('FormationSetStaffRequest', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSETSTAFFREQUEST,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSetStaffRequest)
  ))
_sym_db.RegisterMessage(FormationSetStaffRequest)

FormationSetStaffResponse = _reflection.GeneratedProtocolMessageType('FormationSetStaffResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSETSTAFFRESPONSE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSetStaffResponse)
  ))
_sym_db.RegisterMessage(FormationSetStaffResponse)

FormationSetUnitRequest = _reflection.GeneratedProtocolMessageType('FormationSetUnitRequest', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSETUNITREQUEST,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSetUnitRequest)
  ))
_sym_db.RegisterMessage(FormationSetUnitRequest)

FormationSetUnitResponse = _reflection.GeneratedProtocolMessageType('FormationSetUnitResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSETUNITRESPONSE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSetUnitResponse)
  ))
_sym_db.RegisterMessage(FormationSetUnitResponse)

SyncFormationSlot = _reflection.GeneratedProtocolMessageType('SyncFormationSlot', (_message.Message,), dict(
  DESCRIPTOR = _SYNCFORMATIONSLOT,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.SyncFormationSlot)
  ))
_sym_db.RegisterMessage(SyncFormationSlot)

FormationActiveRequest = _reflection.GeneratedProtocolMessageType('FormationActiveRequest', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONACTIVEREQUEST,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationActiveRequest)
  ))
_sym_db.RegisterMessage(FormationActiveRequest)

FormationActiveResponse = _reflection.GeneratedProtocolMessageType('FormationActiveResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONACTIVERESPONSE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationActiveResponse)
  ))
_sym_db.RegisterMessage(FormationActiveResponse)

FormationLevelUpRequest = _reflection.GeneratedProtocolMessageType('FormationLevelUpRequest', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONLEVELUPREQUEST,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationLevelUpRequest)
  ))
_sym_db.RegisterMessage(FormationLevelUpRequest)

FormationLevelUpResponse = _reflection.GeneratedProtocolMessageType('FormationLevelUpResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONLEVELUPRESPONSE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationLevelUpResponse)
  ))
_sym_db.RegisterMessage(FormationLevelUpResponse)

FormationUseRequest = _reflection.GeneratedProtocolMessageType('FormationUseRequest', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONUSEREQUEST,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationUseRequest)
  ))
_sym_db.RegisterMessage(FormationUseRequest)

FormationUseResponse = _reflection.GeneratedProtocolMessageType('FormationUseResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONUSERESPONSE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationUseResponse)
  ))
_sym_db.RegisterMessage(FormationUseResponse)


# @@protoc_insertion_point(module_scope)
