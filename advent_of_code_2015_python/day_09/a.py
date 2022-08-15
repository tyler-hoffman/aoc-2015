import itertools
from dataclasses import dataclass
from typing import Iterable, Mapping, Optional, Sequence

from pyparsing import cached_property
from advent_of_code_2015_python.day_09.parser import Parser
from advent_of_code_2015_python.day_09.shared import Segment


@dataclass
class Day09PartASolver:
    segments: Sequence[Segment]

    @property
    def solution(self) -> int:
        min_length: Optional[int] = None
        for length in self.compute_lengths():
            if min_length is None or length < min_length:
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
    def all_locations(self) -> str:
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


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
