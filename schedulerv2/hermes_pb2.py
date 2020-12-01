# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hermes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hermes.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\007.;proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0chermes.proto\"1\n\x05Login\x12\r\n\x05token\x18\x01 \x01(\t\x12\r\n\x05\x65vent\x18\x02 \x01(\t\x12\n\n\x02tz\x18\x03 \x01(\t\"!\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\":\n\x06Player\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02tz\x18\x02 \x01(\t\x12\x16\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x06.Event\"?\n\tTimerange\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05start\x18\x02 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x05\x12\n\n\x02tz\x18\x04 \x01(\t\"J\n\nTimeranges\x12\x1e\n\ntimeranges\x18\x01 \x03(\x0b\x32\n.Timerange\x12\r\n\x05token\x18\x02 \x01(\t\x12\r\n\x05\x65vent\x18\x03 \x01(\t\"\x07\n\x05\x45mpty\",\n\x14GetMagicTokenRequest\x12\x14\n\x0cplayer_dc_id\x18\x01 \x01(\t\",\n\x15GetMagicTokenResponse\x12\x13\n\x0bmagic_token\x18\x01 \x01(\t\"m\n\tEventInfo\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x65vent_dc_id\x18\x02 \x01(\t\x12\x12\n\nevent_name\x18\x03 \x01(\t\x12\x13\n\x0bmin_players\x18\x04 \x01(\x05\x12\x10\n\x08min_time\x18\x05 \x01(\x02\"/\n\x11GetEventsResponse\x12\x1a\n\x06\x65vents\x18\x03 \x03(\x0b\x32\n.EventInfo\"*\n\x16GetEventPlayersRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\"J\n\x17GetEventPlayersResponse\x12/\n\x07players\x18\x01 \x03(\x0b\x32\x1e.GetEventPlayersResponsePlayer\"R\n\x1dGetEventPlayersResponsePlayer\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x1e\n\ntimeranges\x18\x02 \x03(\x0b\x32\n.Timerange\"T\n\x16SyncEventPlayerRequest\x12:\n\revent_players\x18\x02 \x03(\x0b\x32#.SyncEventPlayerRequestEventPlayers\"\x8a\x01\n\"SyncEventPlayerRequestEventPlayers\x12\x12\n\nguild_name\x18\x02 \x01(\t\x12\x12\n\nchannel_id\x18\x03 \x01(\t\x12\x14\n\x0c\x63hannel_name\x18\x04 \x01(\t\x12\x11\n\tplayer_id\x18\x05 \x01(\t\x12\x13\n\x0bplayer_name\x18\x06 \x01(\t2\xc7\x01\n\x07Gateway\x12\x1c\n\tGetPlayer\x12\x06.Login\x1a\x07.Player\x12$\n\rGetTimeranges\x12\x06.Login\x1a\x0b.Timeranges\x12)\n\rPutTimeranges\x12\x0b.Timeranges\x1a\x0b.Timeranges\x12$\n\rSetTimeranges\x12\x0b.Timeranges\x1a\x06.Empty\x12\'\n\x10\x44\x65leteTimeranges\x12\x0b.Timeranges\x1a\x06.Empty2,\n\tScheduler\x12\x1f\n\rNotifyUpdated\x12\x06.Event\x1a\x06.Empty2\xed\x01\n\x07\x45ventDb\x12>\n\rGetMagicToken\x12\x15.GetMagicTokenRequest\x1a\x16.GetMagicTokenResponse\x12\'\n\tGetEvents\x12\x06.Empty\x1a\x12.GetEventsResponse\x12\x44\n\x0fGetEventPlayers\x12\x17.GetEventPlayersRequest\x1a\x18.GetEventPlayersResponse\x12\x33\n\x10SyncEventPlayers\x12\x17.SyncEventPlayerRequest\x1a\x06.EmptyB\tZ\x07.;protob\x06proto3'
)




_LOGIN = _descriptor.Descriptor(
  name='Login',
  full_name='Login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='Login.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event', full_name='Login.event', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tz', full_name='Login.tz', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=65,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Event.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Event.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=100,
)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Player.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tz', full_name='Player.tz', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='events', full_name='Player.events', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=160,
)


_TIMERANGE = _descriptor.Descriptor(
  name='Timerange',
  full_name='Timerange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Timerange.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='Timerange.start', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='Timerange.end', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tz', full_name='Timerange.tz', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=225,
)


_TIMERANGES = _descriptor.Descriptor(
  name='Timeranges',
  full_name='Timeranges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeranges', full_name='Timeranges.timeranges', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='Timeranges.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event', full_name='Timeranges.event', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=301,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=310,
)


_GETMAGICTOKENREQUEST = _descriptor.Descriptor(
  name='GetMagicTokenRequest',
  full_name='GetMagicTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_dc_id', full_name='GetMagicTokenRequest.player_dc_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=356,
)


_GETMAGICTOKENRESPONSE = _descriptor.Descriptor(
  name='GetMagicTokenResponse',
  full_name='GetMagicTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='magic_token', full_name='GetMagicTokenResponse.magic_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=402,
)


_EVENTINFO = _descriptor.Descriptor(
  name='EventInfo',
  full_name='EventInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='EventInfo.event_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_dc_id', full_name='EventInfo.event_dc_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_name', full_name='EventInfo.event_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_players', full_name='EventInfo.min_players', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_time', full_name='EventInfo.min_time', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=404,
  serialized_end=513,
)


_GETEVENTSRESPONSE = _descriptor.Descriptor(
  name='GetEventsResponse',
  full_name='GetEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='GetEventsResponse.events', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=515,
  serialized_end=562,
)


_GETEVENTPLAYERSREQUEST = _descriptor.Descriptor(
  name='GetEventPlayersRequest',
  full_name='GetEventPlayersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='GetEventPlayersRequest.event_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=606,
)


_GETEVENTPLAYERSRESPONSE = _descriptor.Descriptor(
  name='GetEventPlayersResponse',
  full_name='GetEventPlayersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='players', full_name='GetEventPlayersResponse.players', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=608,
  serialized_end=682,
)


_GETEVENTPLAYERSRESPONSEPLAYER = _descriptor.Descriptor(
  name='GetEventPlayersResponsePlayer',
  full_name='GetEventPlayersResponsePlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='GetEventPlayersResponsePlayer.player_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeranges', full_name='GetEventPlayersResponsePlayer.timeranges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=684,
  serialized_end=766,
)


_SYNCEVENTPLAYERREQUEST = _descriptor.Descriptor(
  name='SyncEventPlayerRequest',
  full_name='SyncEventPlayerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_players', full_name='SyncEventPlayerRequest.event_players', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=768,
  serialized_end=852,
)


_SYNCEVENTPLAYERREQUESTEVENTPLAYERS = _descriptor.Descriptor(
  name='SyncEventPlayerRequestEventPlayers',
  full_name='SyncEventPlayerRequestEventPlayers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='guild_name', full_name='SyncEventPlayerRequestEventPlayers.guild_name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='SyncEventPlayerRequestEventPlayers.channel_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_name', full_name='SyncEventPlayerRequestEventPlayers.channel_name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='SyncEventPlayerRequestEventPlayers.player_id', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_name', full_name='SyncEventPlayerRequestEventPlayers.player_name', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=993,
)

_PLAYER.fields_by_name['events'].message_type = _EVENT
_TIMERANGES.fields_by_name['timeranges'].message_type = _TIMERANGE
_GETEVENTSRESPONSE.fields_by_name['events'].message_type = _EVENTINFO
_GETEVENTPLAYERSRESPONSE.fields_by_name['players'].message_type = _GETEVENTPLAYERSRESPONSEPLAYER
_GETEVENTPLAYERSRESPONSEPLAYER.fields_by_name['timeranges'].message_type = _TIMERANGE
_SYNCEVENTPLAYERREQUEST.fields_by_name['event_players'].message_type = _SYNCEVENTPLAYERREQUESTEVENTPLAYERS
DESCRIPTOR.message_types_by_name['Login'] = _LOGIN
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['Timerange'] = _TIMERANGE
DESCRIPTOR.message_types_by_name['Timeranges'] = _TIMERANGES
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['GetMagicTokenRequest'] = _GETMAGICTOKENREQUEST
DESCRIPTOR.message_types_by_name['GetMagicTokenResponse'] = _GETMAGICTOKENRESPONSE
DESCRIPTOR.message_types_by_name['EventInfo'] = _EVENTINFO
DESCRIPTOR.message_types_by_name['GetEventsResponse'] = _GETEVENTSRESPONSE
DESCRIPTOR.message_types_by_name['GetEventPlayersRequest'] = _GETEVENTPLAYERSREQUEST
DESCRIPTOR.message_types_by_name['GetEventPlayersResponse'] = _GETEVENTPLAYERSRESPONSE
DESCRIPTOR.message_types_by_name['GetEventPlayersResponsePlayer'] = _GETEVENTPLAYERSRESPONSEPLAYER
DESCRIPTOR.message_types_by_name['SyncEventPlayerRequest'] = _SYNCEVENTPLAYERREQUEST
DESCRIPTOR.message_types_by_name['SyncEventPlayerRequestEventPlayers'] = _SYNCEVENTPLAYERREQUESTEVENTPLAYERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Login = _reflection.GeneratedProtocolMessageType('Login', (_message.Message,), {
  'DESCRIPTOR' : _LOGIN,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:Login)
  })
_sym_db.RegisterMessage(Login)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:Event)
  })
_sym_db.RegisterMessage(Event)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:Player)
  })
_sym_db.RegisterMessage(Player)

Timerange = _reflection.GeneratedProtocolMessageType('Timerange', (_message.Message,), {
  'DESCRIPTOR' : _TIMERANGE,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:Timerange)
  })
_sym_db.RegisterMessage(Timerange)

Timeranges = _reflection.GeneratedProtocolMessageType('Timeranges', (_message.Message,), {
  'DESCRIPTOR' : _TIMERANGES,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:Timeranges)
  })
_sym_db.RegisterMessage(Timeranges)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

GetMagicTokenRequest = _reflection.GeneratedProtocolMessageType('GetMagicTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMAGICTOKENREQUEST,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:GetMagicTokenRequest)
  })
_sym_db.RegisterMessage(GetMagicTokenRequest)

GetMagicTokenResponse = _reflection.GeneratedProtocolMessageType('GetMagicTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMAGICTOKENRESPONSE,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:GetMagicTokenResponse)
  })
_sym_db.RegisterMessage(GetMagicTokenResponse)

EventInfo = _reflection.GeneratedProtocolMessageType('EventInfo', (_message.Message,), {
  'DESCRIPTOR' : _EVENTINFO,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:EventInfo)
  })
_sym_db.RegisterMessage(EventInfo)

GetEventsResponse = _reflection.GeneratedProtocolMessageType('GetEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTSRESPONSE,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:GetEventsResponse)
  })
_sym_db.RegisterMessage(GetEventsResponse)

GetEventPlayersRequest = _reflection.GeneratedProtocolMessageType('GetEventPlayersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTPLAYERSREQUEST,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:GetEventPlayersRequest)
  })
_sym_db.RegisterMessage(GetEventPlayersRequest)

GetEventPlayersResponse = _reflection.GeneratedProtocolMessageType('GetEventPlayersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTPLAYERSRESPONSE,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:GetEventPlayersResponse)
  })
_sym_db.RegisterMessage(GetEventPlayersResponse)

GetEventPlayersResponsePlayer = _reflection.GeneratedProtocolMessageType('GetEventPlayersResponsePlayer', (_message.Message,), {
  'DESCRIPTOR' : _GETEVENTPLAYERSRESPONSEPLAYER,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:GetEventPlayersResponsePlayer)
  })
_sym_db.RegisterMessage(GetEventPlayersResponsePlayer)

SyncEventPlayerRequest = _reflection.GeneratedProtocolMessageType('SyncEventPlayerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYNCEVENTPLAYERREQUEST,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:SyncEventPlayerRequest)
  })
_sym_db.RegisterMessage(SyncEventPlayerRequest)

SyncEventPlayerRequestEventPlayers = _reflection.GeneratedProtocolMessageType('SyncEventPlayerRequestEventPlayers', (_message.Message,), {
  'DESCRIPTOR' : _SYNCEVENTPLAYERREQUESTEVENTPLAYERS,
  '__module__' : 'hermes_pb2'
  # @@protoc_insertion_point(class_scope:SyncEventPlayerRequestEventPlayers)
  })
_sym_db.RegisterMessage(SyncEventPlayerRequestEventPlayers)


DESCRIPTOR._options = None

_GATEWAY = _descriptor.ServiceDescriptor(
  name='Gateway',
  full_name='Gateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=996,
  serialized_end=1195,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPlayer',
    full_name='Gateway.GetPlayer',
    index=0,
    containing_service=None,
    input_type=_LOGIN,
    output_type=_PLAYER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTimeranges',
    full_name='Gateway.GetTimeranges',
    index=1,
    containing_service=None,
    input_type=_LOGIN,
    output_type=_TIMERANGES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PutTimeranges',
    full_name='Gateway.PutTimeranges',
    index=2,
    containing_service=None,
    input_type=_TIMERANGES,
    output_type=_TIMERANGES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetTimeranges',
    full_name='Gateway.SetTimeranges',
    index=3,
    containing_service=None,
    input_type=_TIMERANGES,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTimeranges',
    full_name='Gateway.DeleteTimeranges',
    index=4,
    containing_service=None,
    input_type=_TIMERANGES,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAY)

DESCRIPTOR.services_by_name['Gateway'] = _GATEWAY


_SCHEDULER = _descriptor.ServiceDescriptor(
  name='Scheduler',
  full_name='Scheduler',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1197,
  serialized_end=1241,
  methods=[
  _descriptor.MethodDescriptor(
    name='NotifyUpdated',
    full_name='Scheduler.NotifyUpdated',
    index=0,
    containing_service=None,
    input_type=_EVENT,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEDULER)

DESCRIPTOR.services_by_name['Scheduler'] = _SCHEDULER


_EVENTDB = _descriptor.ServiceDescriptor(
  name='EventDb',
  full_name='EventDb',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1244,
  serialized_end=1481,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMagicToken',
    full_name='EventDb.GetMagicToken',
    index=0,
    containing_service=None,
    input_type=_GETMAGICTOKENREQUEST,
    output_type=_GETMAGICTOKENRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEvents',
    full_name='EventDb.GetEvents',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_GETEVENTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEventPlayers',
    full_name='EventDb.GetEventPlayers',
    index=2,
    containing_service=None,
    input_type=_GETEVENTPLAYERSREQUEST,
    output_type=_GETEVENTPLAYERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SyncEventPlayers',
    full_name='EventDb.SyncEventPlayers',
    index=3,
    containing_service=None,
    input_type=_SYNCEVENTPLAYERREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTDB)

DESCRIPTOR.services_by_name['EventDb'] = _EVENTDB

# @@protoc_insertion_point(module_scope)