# @author Shelton Ngwenya, R00203947

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserChoiceRequest(_message.Message):
    __slots__ = ["letter"]
    LETTER_FIELD_NUMBER: _ClassVar[int]
    letter: str
    def __init__(self, letter: _Optional[str] = ...) -> None: ...

class UserChoiceResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
