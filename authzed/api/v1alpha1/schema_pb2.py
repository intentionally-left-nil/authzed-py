# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v1alpha1/schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='authzed/api/v1alpha1/schema.proto',
  package='authzed.api.v1alpha1',
  syntax='proto3',
  serialized_options=b'Z8github.com/authzed/authzed-go/proto/authzed/api/v1alpha1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!authzed/api/v1alpha1/schema.proto\x12\x14\x61uthzed.api.v1alpha1\x1a\x17validate/validate.proto\"\x9d\x01\n\x11ReadSchemaRequest\x12\x87\x01\n\x18object_definitions_names\x18\x01 \x03(\tBM\xfa\x42J\x92\x01G\"ErC(\x80\x01\x32>^([a-z][a-z0-9_]{2,62}[a-z0-9]/)?[a-z][a-z0-9_]{2,62}[a-z0-9]$R\x16objectDefinitionsNames\"C\n\x12ReadSchemaResponse\x12-\n\x12object_definitions\x18\x01 \x03(\tR\x11objectDefinitions\"7\n\x12WriteSchemaRequest\x12!\n\x06schema\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04(\x80\x80\x10R\x06schema\"O\n\x13WriteSchemaResponse\x12\x38\n\x18object_definitions_names\x18\x01 \x03(\tR\x16objectDefinitionsNames2\xd8\x01\n\rSchemaService\x12\x61\n\nReadSchema\x12\'.authzed.api.v1alpha1.ReadSchemaRequest\x1a(.authzed.api.v1alpha1.ReadSchemaResponse\"\x00\x12\x64\n\x0bWriteSchema\x12(.authzed.api.v1alpha1.WriteSchemaRequest\x1a).authzed.api.v1alpha1.WriteSchemaResponse\"\x00\x42:Z8github.com/authzed/authzed-go/proto/authzed/api/v1alpha1b\x06proto3'
  ,
  dependencies=[validate_dot_validate__pb2.DESCRIPTOR,])




_READSCHEMAREQUEST = _descriptor.Descriptor(
  name='ReadSchemaRequest',
  full_name='authzed.api.v1alpha1.ReadSchemaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_definitions_names', full_name='authzed.api.v1alpha1.ReadSchemaRequest.object_definitions_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372BJ\222\001G\"ErC(\200\0012>^([a-z][a-z0-9_]{2,62}[a-z0-9]/)?[a-z][a-z0-9_]{2,62}[a-z0-9]$', json_name='objectDefinitionsNames', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=85,
  serialized_end=242,
)


_READSCHEMARESPONSE = _descriptor.Descriptor(
  name='ReadSchemaResponse',
  full_name='authzed.api.v1alpha1.ReadSchemaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_definitions', full_name='authzed.api.v1alpha1.ReadSchemaResponse.object_definitions', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectDefinitions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=244,
  serialized_end=311,
)


_WRITESCHEMAREQUEST = _descriptor.Descriptor(
  name='WriteSchemaRequest',
  full_name='authzed.api.v1alpha1.WriteSchemaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='authzed.api.v1alpha1.WriteSchemaRequest.schema', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\006r\004(\200\200\020', json_name='schema', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=313,
  serialized_end=368,
)


_WRITESCHEMARESPONSE = _descriptor.Descriptor(
  name='WriteSchemaResponse',
  full_name='authzed.api.v1alpha1.WriteSchemaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_definitions_names', full_name='authzed.api.v1alpha1.WriteSchemaResponse.object_definitions_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectDefinitionsNames', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=370,
  serialized_end=449,
)

DESCRIPTOR.message_types_by_name['ReadSchemaRequest'] = _READSCHEMAREQUEST
DESCRIPTOR.message_types_by_name['ReadSchemaResponse'] = _READSCHEMARESPONSE
DESCRIPTOR.message_types_by_name['WriteSchemaRequest'] = _WRITESCHEMAREQUEST
DESCRIPTOR.message_types_by_name['WriteSchemaResponse'] = _WRITESCHEMARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadSchemaRequest = _reflection.GeneratedProtocolMessageType('ReadSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _READSCHEMAREQUEST,
  '__module__' : 'authzed.api.v1alpha1.schema_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v1alpha1.ReadSchemaRequest)
  })
_sym_db.RegisterMessage(ReadSchemaRequest)

ReadSchemaResponse = _reflection.GeneratedProtocolMessageType('ReadSchemaResponse', (_message.Message,), {
  'DESCRIPTOR' : _READSCHEMARESPONSE,
  '__module__' : 'authzed.api.v1alpha1.schema_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v1alpha1.ReadSchemaResponse)
  })
_sym_db.RegisterMessage(ReadSchemaResponse)

WriteSchemaRequest = _reflection.GeneratedProtocolMessageType('WriteSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITESCHEMAREQUEST,
  '__module__' : 'authzed.api.v1alpha1.schema_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v1alpha1.WriteSchemaRequest)
  })
_sym_db.RegisterMessage(WriteSchemaRequest)

WriteSchemaResponse = _reflection.GeneratedProtocolMessageType('WriteSchemaResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITESCHEMARESPONSE,
  '__module__' : 'authzed.api.v1alpha1.schema_pb2'
  # @@protoc_insertion_point(class_scope:authzed.api.v1alpha1.WriteSchemaResponse)
  })
_sym_db.RegisterMessage(WriteSchemaResponse)


DESCRIPTOR._options = None
_READSCHEMAREQUEST.fields_by_name['object_definitions_names']._options = None
_WRITESCHEMAREQUEST.fields_by_name['schema']._options = None

_SCHEMASERVICE = _descriptor.ServiceDescriptor(
  name='SchemaService',
  full_name='authzed.api.v1alpha1.SchemaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=452,
  serialized_end=668,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReadSchema',
    full_name='authzed.api.v1alpha1.SchemaService.ReadSchema',
    index=0,
    containing_service=None,
    input_type=_READSCHEMAREQUEST,
    output_type=_READSCHEMARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WriteSchema',
    full_name='authzed.api.v1alpha1.SchemaService.WriteSchema',
    index=1,
    containing_service=None,
    input_type=_WRITESCHEMAREQUEST,
    output_type=_WRITESCHEMARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEMASERVICE)

DESCRIPTOR.services_by_name['SchemaService'] = _SCHEMASERVICE

# @@protoc_insertion_point(module_scope)
