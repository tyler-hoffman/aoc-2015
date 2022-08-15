import itertools
from dataclasses import dataclass
from functools import cached_property
from typing import Callable, Iterable, Mapping, Optional, Sequence


@dataclass(frozen=True)
class Segment:
    a: str
    b: str
    distance: int


@dataclass
class Solver:
    segments: Sequence[Segment]
    is_better: Callable[[int, int], bool]

    @property
    def solution(self) -> int:
        min_length: Optional[int] = None
        for length in self.compute_lengths():
            if min_length is None or self.is_better(length, min_length):
                min_length = length
        assert min_length is not None
        return min_length

    def compute_lengths(self) -> Iterable[int]:
        for permutation in itertools.permutations(self.all_locations):
            yield self.compute_length(permutation)

    def compute_length(self, destinations: Sequence[str]) -> int:
        output = 0
        for i in range(len(destinations) - 1):
            output += self.segment_lengths[(destinations[i], destinations[i + 1])]
        return output

    @cached_property
    def all_locations(self) -> set[str]:
        all_as = {segment.a for segment in self.segments}
        all_bs = {segment.b for segment in self.segments}
        return all_as | all_bs

    @cached_property
    def segment_lengths(self) -> Mapping[tuple[str, str], int]:
        output = dict()
        for segment in self.segments:
            output[(segment.a, segment.b)] = segment.distance
            output[(segment.b, segment.a)] = segment.distance
        return output
