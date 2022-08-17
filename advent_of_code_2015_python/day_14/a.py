from dataclasses import dataclass
from functools import cached_property
from typing import Mapping

from advent_of_code_2015_python.day_14.parser import Parser
from advent_of_code_2015_python.day_14.shared import Reindeer


@dataclass
class Day14PartASolver:
    reindeer: set[Reindeer]
    total_seconds: int

    @property
    def solution(self) -> int:
        return max(self.reindeer_distance.values())

    @cached_property
    def reindeer_distance(self) -> Mapping[Reindeer, int]:
        output: dict[Reindeer, int] = dict()
        for r in self.reindeer:
            full_cycles = int(self.total_seconds / r.cycle_time)
            distance_for_full_cycles = r.km_per_cycle * full_cycles
            remaining_time = self.total_seconds % r.cycle_time
            full_distance = (
                distance_for_full_cycles + min(remaining_time, r.fly_time) * r.km_per_s
            )
            output[r] = full_distance
        return output


def solve(input: str, total_seconds=2503) -> int:
    data = Parser.parse(input)
    solver = Day14PartASolver(data, total_seconds)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_14/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
