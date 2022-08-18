from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Sequence

from advent_of_code_2015_python.day_17.parser import Parser


@dataclass
class Day17PartASolver:
    containers: Iterable[int]
    total_amount: int = 150

    @property
    def solution(self) -> int:
        return self.combination_count

    @cached_property
    def combination_count(self) -> int:
        return len([x for x in self.get_combinations([], 0)])

    def get_combinations(
        self, so_far: list[int], container_index: int
    ) -> Iterable[Iterable[int]]:
        sum_so_far = sum(so_far)
        if sum_so_far == self.total_amount:
            yield so_far
        elif (
            container_index < len(self.sorted_containers)
            and sum_so_far < self.total_amount
        ):
            # without
            yield from self.get_combinations(so_far, container_index + 1)

            # with
            so_far.append(self.sorted_containers[container_index])
            yield from self.get_combinations(so_far, container_index + 1)
            so_far.pop()

    @cached_property
    def sorted_containers(self) -> Sequence[int]:
        return sorted(self.containers)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day17PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
