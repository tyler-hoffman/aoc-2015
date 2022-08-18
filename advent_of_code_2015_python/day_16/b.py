from dataclasses import dataclass
from functools import cached_property
from typing import Callable, Optional

from advent_of_code_2015_python.day_16.parser import Parser
from advent_of_code_2015_python.day_16.shared import Sue


def eq(a: int, b: int) -> bool:
    return a == b


def lt(a: int, b: int) -> bool:
    return a < b


def gt(a: int, b: int) -> bool:
    return a > b


@dataclass(frozen=True)
class Day16PartBSolver:
    sues: set[Sue]

    @property
    def solution(self) -> int:
        filtered = [sue for sue in self.sues if self.matches(sue)]
        assert len(filtered) == 1
        return filtered[0].id

    def matches(self, sue: Sue) -> bool:
        return all(
            [
                self.matches_value(sue.children, self.known_properties.children),
                self.matches_value(sue.cats, self.known_properties.cats, compare=gt),
                self.matches_value(sue.samoyeds, self.known_properties.samoyeds),
                self.matches_value(
                    sue.pomeranians, self.known_properties.pomeranians, compare=lt
                ),
                self.matches_value(sue.akitas, self.known_properties.akitas),
                self.matches_value(sue.vizslas, self.known_properties.vizslas),
                self.matches_value(
                    sue.goldfish, self.known_properties.goldfish, compare=lt
                ),
                self.matches_value(sue.trees, self.known_properties.trees, compare=gt),
                self.matches_value(sue.cars, self.known_properties.cars),
                self.matches_value(sue.perfumes, self.known_properties.perfumes),
            ]
        )

    def matches_value(
        self,
        a: Optional[int],
        b: Optional[int],
        compare: Callable[[int, int], bool] = eq,
    ) -> bool:
        if a is None or b is None:
            return True
        else:
            return compare(a, b)

    @cached_property
    def known_properties(self) -> Sue:
        return Sue(
            id=-1,
            children=3,
            cats=7,
            samoyeds=2,
            pomeranians=3,
            akitas=0,
            vizslas=0,
            goldfish=5,
            trees=3,
            cars=2,
            perfumes=1,
        )


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day16PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_16/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
