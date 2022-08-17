from typing import Iterable, Sequence, TypeVar

_T = TypeVar("_T")


def sliding_window(items: Sequence[_T], count: int) -> Iterable[tuple[_T, ...]]:
    for i in range(len(items) - (count - 1)):
        yield tuple((items[i + j] for j in range(count)))
