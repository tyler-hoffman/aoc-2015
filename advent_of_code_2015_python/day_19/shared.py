from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, Iterable, Optional, TypeVar

_T = TypeVar("_T")
_U = TypeVar("_U")


@dataclass(frozen=True)
class Replacement(Generic[_T, _U]):
    original: _T
    replacement: _U
    steps: int = 1

    def __repr__(self) -> str:
        return f"{self.original} => {self.replacement}"


@dataclass(frozen=True)
class StrReplacement(Replacement[str, str]):
    ...


@dataclass
class DoublyLinkedList:
    _head: Optional[DoublyLinkedList] = field(init=False, default=None)
    _tail: Optional[DoublyLinkedList] = field(init=False, default=None)
    _current: Optional[DoublyLinkedList] = field(init=False, default=None)
    _size: int = field(init=False, default=0)

    @property
    def size(self) -> int:
        return self._size

    @property
    def is_iterating(self) -> bool:
        return self._current is not None

    def add(self, items: Iterable[int]) -> None:
        first: Optional[Node] = None
        prev: Optional[Node] = None
        for item in items:
            new_node = Node(item)
            if prev is None:
                first = new_node
            else:
                new_node.prev_node = prev
                prev.next_node = new_node
            prev = new_node
        assert False, "didn't finish this thought"


@dataclass
class Node:
    value: int
    prev_node: Optional[Node] = None
    next_node: Optional[Node] = None
