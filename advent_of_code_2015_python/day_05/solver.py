from abc import ABC, abstractproperty
from dataclasses import dataclass
from typing import Callable, Iterable, Sequence, Tuple, TypeVar


class Solver(ABC):
    strings: Sequence[str]

    @abstractproperty
    def rules(self) -> Iterable[Callable[[str], bool]]:
        ...

    @property
    def solution(self) -> int:
        nice_words = [word for word in self.strings if self.is_nice(word)]
        return len(nice_words)

    def is_nice(self, word: str) -> bool:
        return all((rule(word) for rule in self.rules))


_T = TypeVar("_T")


def sliding_window(items: Sequence[_T], count: int) -> Iterable[Tuple[_T, ...]]:
    for i in range(len(items) - (count - 1)):
        yield tuple((items[i + j] for j in range(count)))
