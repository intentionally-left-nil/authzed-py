# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v1/debug.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from authzed.api.v1 import core_pb2 as authzed_dot_api_dot_v1_dot_core__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61uthzed/api/v1/debug.proto\x12\x0e\x61uthzed.api.v1\x1a\x19\x61uthzed/api/v1/core.proto\x1a\x17validate/validate.proto\"j\n\x10\x44\x65\x62ugInformation\x12\x35\n\x05\x63heck\x18\x01 \x01(\x0b\x32\x1f.authzed.api.v1.CheckDebugTraceR\x05\x63heck\x12\x1f\n\x0bschema_used\x18\x02 \x01(\tR\nschemaUsed\"\xba\x06\n\x0f\x43heckDebugTrace\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x08resource\x12\x1e\n\npermission\x18\x02 \x01(\tR\npermission\x12\x63\n\x0fpermission_type\x18\x03 \x01(\x0e\x32..authzed.api.v1.CheckDebugTrace.PermissionTypeB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x0epermissionType\x12\x44\n\x07subject\x18\x04 \x01(\x0b\x32 .authzed.api.v1.SubjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\x12R\n\x06result\x18\x05 \x01(\x0e\x32..authzed.api.v1.CheckDebugTrace.PermissionshipB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x06result\x12,\n\x11was_cached_result\x18\x06 \x01(\x08H\x00R\x0fwasCachedResult\x12P\n\x0csub_problems\x18\x07 \x01(\x0b\x32+.authzed.api.v1.CheckDebugTrace.SubProblemsH\x00R\x0bsubProblems\x1a\x46\n\x0bSubProblems\x12\x37\n\x06traces\x18\x01 \x03(\x0b\x32\x1f.authzed.api.v1.CheckDebugTraceR\x06traces\"o\n\x0ePermissionType\x12\x1f\n\x1bPERMISSION_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18PERMISSION_TYPE_RELATION\x10\x01\x12\x1e\n\x1aPERMISSION_TYPE_PERMISSION\x10\x02\"u\n\x0ePermissionship\x12\x1e\n\x1aPERMISSIONSHIP_UNSPECIFIED\x10\x00\x12 \n\x1cPERMISSIONSHIP_NO_PERMISSION\x10\x01\x12!\n\x1dPERMISSIONSHIP_HAS_PERMISSION\x10\x02\x42\x11\n\nresolution\x12\x03\xf8\x42\x01\x42H\n\x12\x63om.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1.debug_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1'
  _CHECKDEBUGTRACE.oneofs_by_name['resolution']._options = None
  _CHECKDEBUGTRACE.oneofs_by_name['resolution']._serialized_options = b'\370B\001'
  _CHECKDEBUGTRACE.fields_by_name['resource']._options = None
  _CHECKDEBUGTRACE.fields_by_name['resource']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CHECKDEBUGTRACE.fields_by_name['permission_type']._options = None
  _CHECKDEBUGTRACE.fields_by_name['permission_type']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _CHECKDEBUGTRACE.fields_by_name['subject']._options = None
  _CHECKDEBUGTRACE.fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CHECKDEBUGTRACE.fields_by_name['result']._options = None
  _CHECKDEBUGTRACE.fields_by_name['result']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _DEBUGINFORMATION._serialized_start=98
  _DEBUGINFORMATION._serialized_end=204
  _CHECKDEBUGTRACE._serialized_start=207
  _CHECKDEBUGTRACE._serialized_end=1033
  _CHECKDEBUGTRACE_SUBPROBLEMS._serialized_start=712
  _CHECKDEBUGTRACE_SUBPROBLEMS._serialized_end=782
  _CHECKDEBUGTRACE_PERMISSIONTYPE._serialized_start=784
  _CHECKDEBUGTRACE_PERMISSIONTYPE._serialized_end=895
  _CHECKDEBUGTRACE_PERMISSIONSHIP._serialized_start=897
  _CHECKDEBUGTRACE_PERMISSIONSHIP._serialized_end=1014
# @@protoc_insertion_point(module_scope)