from dataclasses import dataclass
from functools import cached_property
from math import prod
from typing import Optional
from advent_of_code_2015_python.day_24.parser import Parser
from advent_of_code_2015_python.day_24.shared import SubsetGetter


@dataclass
class Day24PartASolver:
    values: set[int]
    compartment_count: int

    @property
    def solution(self) -> int:
        best: Optional[int] = None
        for values in self.passenger_compartment_variations:
            if len(values) == self.shortest_length_for_passenger_compartment:
                the_sum = prod(values)
                if best is None or the_sum < best:
                    best = the_sum
        assert best is not None
        return best

    @cached_property
    def per_compartment(self) -> int:
        the_sum = sum(self.values)
        assert the_sum % self.compartment_count == 0
        return the_sum // self.compartment_count

    @cached_property
    def passenger_compartment_variations(self) -> set[frozenset[int]]:
        subset_getter = SubsetGetter(self.values, self.per_compartment)
        return set(subset_getter.values_for_target)

    @cached_property
    def shortest_length_for_passenger_compartment(self) -> int:
        return min(len(s) for s in self.passenger_compartment_variations)


def solve(input: str) -> int:
    values = Parser.parse(input)
    solver = Day24PartASolver(values, 3)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_24/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
