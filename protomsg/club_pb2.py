# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: club.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='club.proto',
  package='Dianjing.protocol',
  serialized_pb='\n\nclub.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\"\xf3\x01\n\x04\x43lub\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0f\n\x07manager\x18\x03 \x02(\t\x12\x0c\n\x04\x66lag\x18\x04 \x02(\x05\x12\r\n\x05level\x18\x05 \x02(\x05\x12\x0e\n\x06renown\x18\x06 \x02(\x05\x12\x0b\n\x03vip\x18\x07 \x02(\x05\x12\x0b\n\x03\x65xp\x18\x08 \x02(\x05\x12\x0c\n\x04gold\x18\t \x02(\x05\x12\x0f\n\x07\x64iamond\x18\n \x02(\x05\x12\x12\n\nmax_renown\x18\x0b \x02(\x05\x12\x36\n\x0cmatch_staffs\x18\x0c \x03(\x0b\x32 .Dianjing.protocol.StaffBaseInfo\x12\x0e\n\x06policy\x18\r \x01(\x05\"D\n\nClubNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12%\n\x04\x63lub\x18\x02 \x02(\x0b\x32\x17.Dianjing.protocol.Club\"@\n\x11\x43reateClubRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04\x66lag\x18\x03 \x02(\x05\"2\n\x12\x43reateClubResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\":\n\x14\x43lubSetPolicyRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x11\n\tpolicy_id\x18\x02 \x02(\x05\"5\n\x15\x43lubSetPolicyResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\">\n\x18\x43lubSetMatchStaffRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x11\n\tstaff_ids\x18\x02 \x03(\x05\"9\n\x19\x43lubSetMatchStaffResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c')




_CLUB = _descriptor.Descriptor(
  name='Club',
  full_name='Dianjing.protocol.Club',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Club.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dianjing.protocol.Club.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manager', full_name='Dianjing.protocol.Club.manager', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='Dianjing.protocol.Club.flag', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Dianjing.protocol.Club.level', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='renown', full_name='Dianjing.protocol.Club.renown', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip', full_name='Dianjing.protocol.Club.vip', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='Dianjing.protocol.Club.exp', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='Dianjing.protocol.Club.gold', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diamond', full_name='Dianjing.protocol.Club.diamond', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_renown', full_name='Dianjing.protocol.Club.max_renown', index=10,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_staffs', full_name='Dianjing.protocol.Club.match_staffs', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy', full_name='Dianjing.protocol.Club.policy', index=12,
      number=13, type=5, cpp_type=1, label=1,
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
  extension_ranges=[],
  serialized_start=48,
  serialized_end=291,
)


_CLUBNOTIFY = _descriptor.Descriptor(
  name='ClubNotify',
  full_name='Dianjing.protocol.ClubNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ClubNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club', full_name='Dianjing.protocol.ClubNotify.club', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=293,
  serialized_end=361,
)


_CREATECLUBREQUEST = _descriptor.Descriptor(
  name='CreateClubRequest',
  full_name='Dianjing.protocol.CreateClubRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.CreateClubRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dianjing.protocol.CreateClubRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='Dianjing.protocol.CreateClubRequest.flag', index=2,
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
  extension_ranges=[],
  serialized_start=363,
  serialized_end=427,
)


_CREATECLUBRESPONSE = _descriptor.Descriptor(
  name='CreateClubResponse',
  full_name='Dianjing.protocol.CreateClubResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.CreateClubResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.CreateClubResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=429,
  serialized_end=479,
)


_CLUBSETPOLICYREQUEST = _descriptor.Descriptor(
  name='ClubSetPolicyRequest',
  full_name='Dianjing.protocol.ClubSetPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ClubSetPolicyRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy_id', full_name='Dianjing.protocol.ClubSetPolicyRequest.policy_id', index=1,
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
  extension_ranges=[],
  serialized_start=481,
  serialized_end=539,
)


_CLUBSETPOLICYRESPONSE = _descriptor.Descriptor(
  name='ClubSetPolicyResponse',
  full_name='Dianjing.protocol.ClubSetPolicyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.ClubSetPolicyResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ClubSetPolicyResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=541,
  serialized_end=594,
)


_CLUBSETMATCHSTAFFREQUEST = _descriptor.Descriptor(
  name='ClubSetMatchStaffRequest',
  full_name='Dianjing.protocol.ClubSetMatchStaffRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ClubSetMatchStaffRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_ids', full_name='Dianjing.protocol.ClubSetMatchStaffRequest.staff_ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  extension_ranges=[],
  serialized_start=596,
  serialized_end=658,
)


_CLUBSETMATCHSTAFFRESPONSE = _descriptor.Descriptor(
  name='ClubSetMatchStaffResponse',
  full_name='Dianjing.protocol.ClubSetMatchStaffResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.ClubSetMatchStaffResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ClubSetMatchStaffResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=660,
  serialized_end=717,
)

_CLUB.fields_by_name['match_staffs'].message_type = common_pb2._STAFFBASEINFO
_CLUBNOTIFY.fields_by_name['club'].message_type = _CLUB
DESCRIPTOR.message_types_by_name['Club'] = _CLUB
DESCRIPTOR.message_types_by_name['ClubNotify'] = _CLUBNOTIFY
DESCRIPTOR.message_types_by_name['CreateClubRequest'] = _CREATECLUBREQUEST
DESCRIPTOR.message_types_by_name['CreateClubResponse'] = _CREATECLUBRESPONSE
DESCRIPTOR.message_types_by_name['ClubSetPolicyRequest'] = _CLUBSETPOLICYREQUEST
DESCRIPTOR.message_types_by_name['ClubSetPolicyResponse'] = _CLUBSETPOLICYRESPONSE
DESCRIPTOR.message_types_by_name['ClubSetMatchStaffRequest'] = _CLUBSETMATCHSTAFFREQUEST
DESCRIPTOR.message_types_by_name['ClubSetMatchStaffResponse'] = _CLUBSETMATCHSTAFFRESPONSE

class Club(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUB

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Club)

class ClubNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUBNOTIFY

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubNotify)

class CreateClubRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATECLUBREQUEST

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.CreateClubRequest)

class CreateClubResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATECLUBRESPONSE

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.CreateClubResponse)

class ClubSetPolicyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUBSETPOLICYREQUEST

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubSetPolicyRequest)

class ClubSetPolicyResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUBSETPOLICYRESPONSE

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubSetPolicyResponse)

class ClubSetMatchStaffRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUBSETMATCHSTAFFREQUEST

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubSetMatchStaffRequest)

class ClubSetMatchStaffResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUBSETMATCHSTAFFRESPONSE

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubSetMatchStaffResponse)


# @@protoc_insertion_point(module_scope)
