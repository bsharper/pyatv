"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SetArtworkMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    JPEGDATA_FIELD_NUMBER: builtins.int
    jpegData: builtins.bytes = ...
    def __init__(self,
        *,
        jpegData : typing.Optional[builtins.bytes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["jpegData",b"jpegData"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["jpegData",b"jpegData"]) -> None: ...
global___SetArtworkMessage = SetArtworkMessage

setArtworkMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___SetArtworkMessage] = ...
