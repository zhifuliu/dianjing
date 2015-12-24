# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: match.proto

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
  serialized_pb=b'\n\x0bmatch.proto\x12\x11\x44ianjing.protocol\x1a\nclub.proto\"\xd5\x01\n\nStaffMatch\x12\x36\n\tstaff_one\x18\x01 \x02(\x0b\x32#.Dianjing.protocol.StaffMatch.Staff\x12\x36\n\tstaff_two\x18\x02 \x02(\x0b\x32#.Dianjing.protocol.StaffMatch.Staff\x1aW\n\x05Staff\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06\x63\x61ozuo\x18\x02 \x02(\x05\x12\x10\n\x08jingying\x18\x03 \x02(\x05\x12\x0f\n\x07\x62\x61obing\x18\x04 \x02(\x05\x12\x0f\n\x07zhanshu\x18\x05 \x02(\x05\"\x9d\x01\n\tClubMatch\x12)\n\x08\x63lub_one\x18\x01 \x02(\x0b\x32\x17.Dianjing.protocol.Club\x12)\n\x08\x63lub_two\x18\x02 \x02(\x0b\x32\x17.Dianjing.protocol.Club\x12,\n\x05match\x18\x03 \x03(\x0b\x32\x1d.Dianjing.protocol.StaffMatch\x12\x0c\n\x04seed\x18\x04 \x01(\x05'
  ,
  dependencies=[club__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STAFFMATCH_STAFF = _descriptor.Descriptor(
  name='Staff',
  full_name='Dianjing.protocol.StaffMatch.Staff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.StaffMatch.Staff.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caozuo', full_name='Dianjing.protocol.StaffMatch.Staff.caozuo', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jingying', full_name='Dianjing.protocol.StaffMatch.Staff.jingying', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baobing', full_name='Dianjing.protocol.StaffMatch.Staff.baobing', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zhanshu', full_name='Dianjing.protocol.StaffMatch.Staff.zhanshu', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=173,
  serialized_end=260,
)

_STAFFMATCH = _descriptor.Descriptor(
  name='StaffMatch',
  full_name='Dianjing.protocol.StaffMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staff_one', full_name='Dianjing.protocol.StaffMatch.staff_one', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_two', full_name='Dianjing.protocol.StaffMatch.staff_two', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STAFFMATCH_STAFF, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=260,
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
      name='match', full_name='Dianjing.protocol.ClubMatch.match', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed', full_name='Dianjing.protocol.ClubMatch.seed', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=263,
  serialized_end=420,
)

_STAFFMATCH_STAFF.containing_type = _STAFFMATCH
_STAFFMATCH.fields_by_name['staff_one'].message_type = _STAFFMATCH_STAFF
_STAFFMATCH.fields_by_name['staff_two'].message_type = _STAFFMATCH_STAFF
_CLUBMATCH.fields_by_name['club_one'].message_type = club__pb2._CLUB
_CLUBMATCH.fields_by_name['club_two'].message_type = club__pb2._CLUB
_CLUBMATCH.fields_by_name['match'].message_type = _STAFFMATCH
DESCRIPTOR.message_types_by_name['StaffMatch'] = _STAFFMATCH
DESCRIPTOR.message_types_by_name['ClubMatch'] = _CLUBMATCH

StaffMatch = _reflection.GeneratedProtocolMessageType('StaffMatch', (_message.Message,), dict(

  Staff = _reflection.GeneratedProtocolMessageType('Staff', (_message.Message,), dict(
    DESCRIPTOR = _STAFFMATCH_STAFF,
    __module__ = 'match_pb2'
    # @@protoc_insertion_point(class_scope:Dianjing.protocol.StaffMatch.Staff)
    ))
  ,
  DESCRIPTOR = _STAFFMATCH,
  __module__ = 'match_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.StaffMatch)
  ))
_sym_db.RegisterMessage(StaffMatch)
_sym_db.RegisterMessage(StaffMatch.Staff)

ClubMatch = _reflection.GeneratedProtocolMessageType('ClubMatch', (_message.Message,), dict(
  DESCRIPTOR = _CLUBMATCH,
  __module__ = 'match_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubMatch)
  ))
_sym_db.RegisterMessage(ClubMatch)


# @@protoc_insertion_point(module_scope)
