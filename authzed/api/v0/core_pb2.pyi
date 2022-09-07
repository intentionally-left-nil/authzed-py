"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class RelationTuple(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OBJECT_AND_RELATION_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int

    @property
    def object_and_relation(self) -> global___ObjectAndRelation: ...

    @property
    def user(self) -> global___User: ...

    def __init__(self,
        *,
        object_and_relation : typing.Optional[global___ObjectAndRelation] = ...,
        user : typing.Optional[global___User] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"object_and_relation",b"object_and_relation",u"user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"object_and_relation",b"object_and_relation",u"user",b"user"]) -> None: ...
global___RelationTuple = RelationTuple

class ObjectAndRelation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMESPACE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    namespace: typing.Text = ...
    object_id: typing.Text = ...
    relation: typing.Text = ...

    def __init__(self,
        *,
        namespace : typing.Text = ...,
        object_id : typing.Text = ...,
        relation : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"namespace",b"namespace",u"object_id",b"object_id",u"relation",b"relation"]) -> None: ...
global___ObjectAndRelation = ObjectAndRelation

class RelationReference(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMESPACE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    namespace: typing.Text = ...
    relation: typing.Text = ...

    def __init__(self,
        *,
        namespace : typing.Text = ...,
        relation : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"namespace",b"namespace",u"relation",b"relation"]) -> None: ...
global___RelationReference = RelationReference

class User(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USERSET_FIELD_NUMBER: builtins.int

    @property
    def userset(self) -> global___ObjectAndRelation: ...

    def __init__(self,
        *,
        userset : typing.Optional[global___ObjectAndRelation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"user_oneof",b"user_oneof",u"userset",b"userset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"user_oneof",b"user_oneof",u"userset",b"userset"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"user_oneof",b"user_oneof"]) -> typing.Optional[typing_extensions.Literal["userset"]]: ...
global___User = User
