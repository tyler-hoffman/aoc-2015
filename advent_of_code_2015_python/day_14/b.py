from dataclasses import dataclass
from functools import cache, cached_property
from typing import Mapping

from advent_of_code_2015_python.day_14.parser import Parser
from advent_of_code_2015_python.day_14.shared import Reindeer


@dataclass(frozen=True)
class Day14PartBSolver:
    reindeer: set[Reindeer]
    total_seconds: int

    @property
    def solution(self) -> int:
        return max(self.scores.values())

    @cached_property
    def scores(self) -> Mapping[Reindeer, int]:
        output: dict[Reindeer, int] = {r: 0 for r in self.reindeer}
        for second in range(self.total_seconds):
            for winner in self.best_at_second(second):
                output[winner] += 1
        return output

    def best_at_second(self, second: int) -> set[Reindeer]:
        best_distance = 0
        winners_so_far: set[Reindeer] = set()
        for r in self.reindeer:
            dist = self.distances_at_seconds[(r, second)]
            if dist == best_distance:
                winners_so_far.add(r)
            elif dist > best_distance:
                best_distance = dist
                winners_so_far = set([r])
        return winners_so_far

    @cached_property
    def distances_at_seconds(self) -> Mapping[tuple[Reindeer, int], int]:
        output: dict[tuple[Reindeer, int], int] = dict()
        for r in self.reindeer:
            position = 0
            for second in range(self.total_seconds):
                if second % r.cycle_time < r.fly_time:
                    position += r.km_per_s
                output[(r, second)] = position
        return output


def solve(input: str, total_seconds=2503) -> int:
    data = Parser.parse(input)
    solver = Day14PartBSolver(data, total_seconds)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_14/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
