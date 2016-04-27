# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: match.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import club_pb2 as club__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='match.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\x0bmatch.proto\x12\x11\x44ianjing.protocol\x1a\nclub.proto\"\xf7\x01\n\tClubMatch\x12\x38\n\x08\x63lub_one\x18\x01 \x02(\x0b\x32&.Dianjing.protocol.ClubMatch.ClubTroop\x12\x38\n\x08\x63lub_two\x18\x02 \x02(\x0b\x32&.Dianjing.protocol.ClubMatch.ClubTroop\x12\x0c\n\x04seed\x18\x03 \x02(\x05\x12\x0b\n\x03key\x18\x04 \x02(\t\x1a[\n\tClubTroop\x12%\n\x04\x63lub\x18\x01 \x02(\x0b\x32\x17.Dianjing.protocol.Club\x12\'\n\x05troop\x18\x02 \x03(\x0b\x32\x18.Dianjing.protocol.Troop\"O\n\x10StaffMatchResult\x12\x11\n\tstaff_one\x18\x01 \x02(\x05\x12\x11\n\tstaff_two\x18\x02 \x02(\x05\x12\x15\n\rstaff_one_win\x18\x03 \x02(\x08\"\xa3\x07\n\x05Troop\x12+\n\x04hero\x18\x01 \x02(\x0b\x32\x1d.Dianjing.protocol.Troop.Hero\x12+\n\x04\x61rmy\x18\x02 \x02(\x0b\x32\x1d.Dianjing.protocol.Troop.Army\x1a\xe3\x01\n\x04Hero\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0b\n\x03oid\x18\x02 \x02(\x05\x12\x10\n\x08position\x18\x03 \x02(\x05\x12\x0e\n\x06\x61ttack\x18\x04 \x02(\x05\x12\x15\n\rattackPercent\x18\x05 \x02(\x02\x12\x0f\n\x07\x64\x65\x66\x65nse\x18\x06 \x02(\x05\x12\x16\n\x0e\x64\x65\x66\x65nsePercent\x18\x07 \x02(\x02\x12\x0e\n\x06manage\x18\x08 \x02(\x05\x12\x15\n\rmanagePercent\x18\t \x02(\x02\x12\x11\n\toperation\x18\n \x02(\x05\x12\x18\n\x10operationPercent\x18\x0b \x02(\x02\x12\x0c\n\x04star\x18\x0c \x02(\x05\x1a\xd9\x04\n\x04\x41rmy\x12\n\n\x02id\x18\x01 \x02(\x05\x12\n\n\x02hp\x18\x02 \x02(\x05\x12\x11\n\thpPercent\x18\x03 \x02(\x02\x12\x0e\n\x06\x61ttack\x18\x04 \x02(\x05\x12\x15\n\rattackPercent\x18\x05 \x02(\x02\x12\x0f\n\x07\x64\x65\x66\x65nse\x18\x06 \x02(\x05\x12\x16\n\x0e\x64\x65\x66\x65nsePercent\x18\x07 \x02(\x02\x12\x13\n\x0b\x61ttackSpeed\x18\x08 \x02(\x02\x12\x1a\n\x12\x61ttackSpeedPercent\x18\t \x02(\x02\x12\x16\n\x0e\x61ttackDistance\x18\n \x02(\x02\x12\x1d\n\x15\x61ttackDistancePercent\x18\x0b \x02(\x02\x12\x11\n\tmoveSpeed\x18\x0c \x02(\x02\x12\x18\n\x10moveSpeedPercent\x18\r \x02(\x02\x12\x0f\n\x07hitRate\x18\x0e \x02(\x02\x12\x11\n\tdodgeRate\x18\x0f \x02(\x02\x12\x10\n\x08\x63ritRate\x18\x10 \x02(\x02\x12\x11\n\tcritMulti\x18\x11 \x02(\x02\x12\x14\n\x0c\x63ritAntiRate\x18\x12 \x02(\x02\x12\x1a\n\x12\x61ppendAttackTerran\x18\x13 \x02(\x02\x12\x1b\n\x13\x61ppendAttackProtoss\x18\x14 \x02(\x02\x12\x18\n\x10\x61ppendAttackZerg\x18\x15 \x02(\x02\x12\x1e\n\x16\x61ppendAttackedByTerran\x18\x16 \x02(\x02\x12\x1f\n\x17\x61ppendAttackedByProtoss\x18\x17 \x02(\x02\x12\x1c\n\x14\x61ppendAttackedByZerg\x18\x18 \x02(\x02\x12\x17\n\x0f\x66inalHurtAppend\x18\x19 \x02(\x05\x12\x17\n\x0f\x66inalHurtReduce\x18\x1a \x02(\x05')
  ,
  dependencies=[club__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CLUBMATCH_CLUBTROOP = _descriptor.Descriptor(
  name='ClubTroop',
  full_name='Dianjing.protocol.ClubMatch.ClubTroop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='club', full_name='Dianjing.protocol.ClubMatch.ClubTroop.club', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='troop', full_name='Dianjing.protocol.ClubMatch.ClubTroop.troop', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=203,
  serialized_end=294,
)

_CLUBMATCH = _descriptor.Descriptor(
  name='ClubMatch',
  full_name='Dianjing.protocol.ClubMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='club_one', full_name='Dianjing.protocol.ClubMatch.club_one', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club_two', full_name='Dianjing.protocol.ClubMatch.club_two', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed', full_name='Dianjing.protocol.ClubMatch.seed', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='Dianjing.protocol.ClubMatch.key', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CLUBMATCH_CLUBTROOP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=294,
)


_STAFFMATCHRESULT = _descriptor.Descriptor(
  name='StaffMatchResult',
  full_name='Dianjing.protocol.StaffMatchResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staff_one', full_name='Dianjing.protocol.StaffMatchResult.staff_one', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_two', full_name='Dianjing.protocol.StaffMatchResult.staff_two', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_one_win', full_name='Dianjing.protocol.StaffMatchResult.staff_one_win', index=2,
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
  serialized_start=296,
  serialized_end=375,
)


_TROOP_HERO = _descriptor.Descriptor(
  name='Hero',
  full_name='Dianjing.protocol.Troop.Hero',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Troop.Hero.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oid', full_name='Dianjing.protocol.Troop.Hero.oid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='Dianjing.protocol.Troop.Hero.position', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attack', full_name='Dianjing.protocol.Troop.Hero.attack', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attackPercent', full_name='Dianjing.protocol.Troop.Hero.attackPercent', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defense', full_name='Dianjing.protocol.Troop.Hero.defense', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defensePercent', full_name='Dianjing.protocol.Troop.Hero.defensePercent', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manage', full_name='Dianjing.protocol.Troop.Hero.manage', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='managePercent', full_name='Dianjing.protocol.Troop.Hero.managePercent', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='Dianjing.protocol.Troop.Hero.operation', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operationPercent', full_name='Dianjing.protocol.Troop.Hero.operationPercent', index=10,
      number=11, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='star', full_name='Dianjing.protocol.Troop.Hero.star', index=11,
      number=12, type=5, cpp_type=1, label=2,
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
  serialized_start=478,
  serialized_end=705,
)

_TROOP_ARMY = _descriptor.Descriptor(
  name='Army',
  full_name='Dianjing.protocol.Troop.Army',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Troop.Army.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp', full_name='Dianjing.protocol.Troop.Army.hp', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hpPercent', full_name='Dianjing.protocol.Troop.Army.hpPercent', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attack', full_name='Dianjing.protocol.Troop.Army.attack', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attackPercent', full_name='Dianjing.protocol.Troop.Army.attackPercent', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defense', full_name='Dianjing.protocol.Troop.Army.defense', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defensePercent', full_name='Dianjing.protocol.Troop.Army.defensePercent', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attackSpeed', full_name='Dianjing.protocol.Troop.Army.attackSpeed', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attackSpeedPercent', full_name='Dianjing.protocol.Troop.Army.attackSpeedPercent', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attackDistance', full_name='Dianjing.protocol.Troop.Army.attackDistance', index=9,
      number=10, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attackDistancePercent', full_name='Dianjing.protocol.Troop.Army.attackDistancePercent', index=10,
      number=11, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moveSpeed', full_name='Dianjing.protocol.Troop.Army.moveSpeed', index=11,
      number=12, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moveSpeedPercent', full_name='Dianjing.protocol.Troop.Army.moveSpeedPercent', index=12,
      number=13, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hitRate', full_name='Dianjing.protocol.Troop.Army.hitRate', index=13,
      number=14, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dodgeRate', full_name='Dianjing.protocol.Troop.Army.dodgeRate', index=14,
      number=15, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='critRate', full_name='Dianjing.protocol.Troop.Army.critRate', index=15,
      number=16, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='critMulti', full_name='Dianjing.protocol.Troop.Army.critMulti', index=16,
      number=17, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='critAntiRate', full_name='Dianjing.protocol.Troop.Army.critAntiRate', index=17,
      number=18, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appendAttackTerran', full_name='Dianjing.protocol.Troop.Army.appendAttackTerran', index=18,
      number=19, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appendAttackProtoss', full_name='Dianjing.protocol.Troop.Army.appendAttackProtoss', index=19,
      number=20, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appendAttackZerg', full_name='Dianjing.protocol.Troop.Army.appendAttackZerg', index=20,
      number=21, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appendAttackedByTerran', full_name='Dianjing.protocol.Troop.Army.appendAttackedByTerran', index=21,
      number=22, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appendAttackedByProtoss', full_name='Dianjing.protocol.Troop.Army.appendAttackedByProtoss', index=22,
      number=23, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appendAttackedByZerg', full_name='Dianjing.protocol.Troop.Army.appendAttackedByZerg', index=23,
      number=24, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finalHurtAppend', full_name='Dianjing.protocol.Troop.Army.finalHurtAppend', index=24,
      number=25, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finalHurtReduce', full_name='Dianjing.protocol.Troop.Army.finalHurtReduce', index=25,
      number=26, type=5, cpp_type=1, label=2,
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
  serialized_start=708,
  serialized_end=1309,
)

_TROOP = _descriptor.Descriptor(
  name='Troop',
  full_name='Dianjing.protocol.Troop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero', full_name='Dianjing.protocol.Troop.hero', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='army', full_name='Dianjing.protocol.Troop.army', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TROOP_HERO, _TROOP_ARMY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=378,
  serialized_end=1309,
)

_CLUBMATCH_CLUBTROOP.fields_by_name['club'].message_type = club__pb2._CLUB
_CLUBMATCH_CLUBTROOP.fields_by_name['troop'].message_type = _TROOP
_CLUBMATCH_CLUBTROOP.containing_type = _CLUBMATCH
_CLUBMATCH.fields_by_name['club_one'].message_type = _CLUBMATCH_CLUBTROOP
_CLUBMATCH.fields_by_name['club_two'].message_type = _CLUBMATCH_CLUBTROOP
_TROOP_HERO.containing_type = _TROOP
_TROOP_ARMY.containing_type = _TROOP
_TROOP.fields_by_name['hero'].message_type = _TROOP_HERO
_TROOP.fields_by_name['army'].message_type = _TROOP_ARMY
DESCRIPTOR.message_types_by_name['ClubMatch'] = _CLUBMATCH
DESCRIPTOR.message_types_by_name['StaffMatchResult'] = _STAFFMATCHRESULT
DESCRIPTOR.message_types_by_name['Troop'] = _TROOP

ClubMatch = _reflection.GeneratedProtocolMessageType('ClubMatch', (_message.Message,), dict(

  ClubTroop = _reflection.GeneratedProtocolMessageType('ClubTroop', (_message.Message,), dict(
    DESCRIPTOR = _CLUBMATCH_CLUBTROOP,
    __module__ = 'match_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubMatch.ClubTroop)
    ))
  ,
  DESCRIPTOR = _CLUBMATCH,
  __module__ = 'match_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubMatch)
  ))
_sym_db.RegisterMessage(ClubMatch)
_sym_db.RegisterMessage(ClubMatch.ClubTroop)

StaffMatchResult = _reflection.GeneratedProtocolMessageType('StaffMatchResult', (_message.Message,), dict(
  DESCRIPTOR = _STAFFMATCHRESULT,
  __module__ = 'match_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.StaffMatchResult)
  ))
_sym_db.RegisterMessage(StaffMatchResult)

Troop = _reflection.GeneratedProtocolMessageType('Troop', (_message.Message,), dict(

  Hero = _reflection.GeneratedProtocolMessageType('Hero', (_message.Message,), dict(
    DESCRIPTOR = _TROOP_HERO,
    __module__ = 'match_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.Troop.Hero)
    ))
  ,

  Army = _reflection.GeneratedProtocolMessageType('Army', (_message.Message,), dict(
    DESCRIPTOR = _TROOP_ARMY,
    __module__ = 'match_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.Troop.Army)
    ))
  ,
  DESCRIPTOR = _TROOP,
  __module__ = 'match_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Troop)
  ))
_sym_db.RegisterMessage(Troop)
_sym_db.RegisterMessage(Troop.Hero)
_sym_db.RegisterMessage(Troop.Army)


# @@protoc_insertion_point(module_scope)
