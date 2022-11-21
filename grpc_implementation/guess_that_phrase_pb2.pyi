from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LetterRequest(_message.Message):
    __slots__ = ["letter"]
    LETTER_FIELD_NUMBER: _ClassVar[int]
    letter: str
    def __init__(self, letter: _Optional[str] = ...) -> None: ...

class LetterResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class PhraseRequest(_message.Message):
    __slots__ = ["phrase"]
    PHRASE_FIELD_NUMBER: _ClassVar[int]
    phrase: str
    def __init__(self, phrase: _Optional[str] = ...) -> None: ...

class PhraseResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
