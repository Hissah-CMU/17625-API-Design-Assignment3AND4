from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Author(_message.Message):
    __slots__ = ["biography", "name", "writings"]
    BIOGRAPHY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WRITINGS_FIELD_NUMBER: _ClassVar[int]
    biography: str
    name: str
    writings: _containers.RepeatedCompositeFieldContainer[Book]
    def __init__(self, name: _Optional[str] = ..., biography: _Optional[str] = ..., writings: _Optional[_Iterable[_Union[Book, _Mapping]]] = ...) -> None: ...

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "publishingYear", "title"]
    class GenreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    Fiction: Book.GenreType
    GENRE_FIELD_NUMBER: _ClassVar[int]
    History: Book.GenreType
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    NonFiction: Book.GenreType
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    Philosophy: Book.GenreType
    SocialScience: Book.GenreType
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Book.GenreType
    publishingYear: int
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.GenreType, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: Book
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = ["confirmationMessage"]
    CONFIRMATIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    confirmationMessage: str
    def __init__(self, confirmationMessage: _Optional[str] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: Book
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "inventoryNumber", "status"]
    class ItemStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    Available: InventoryItem.ItemStatus
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    Taken: InventoryItem.ItemStatus
    book: Book
    inventoryNumber: str
    status: InventoryItem.ItemStatus
    def __init__(self, inventoryNumber: _Optional[str] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[InventoryItem.ItemStatus, str]] = ...) -> None: ...
