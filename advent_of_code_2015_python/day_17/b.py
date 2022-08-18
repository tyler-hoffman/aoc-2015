from functools import cached_property

from advent_of_code_2015_python.day_17.parser import Parser
from advent_of_code_2015_python.day_17.shared import Day17Solver


class Day17PartBSolver(Day17Solver):
    @property
    def solution(self) -> int:
        return len(
            [c for c in self.combinations if len(c) == self.min_combination_count]
        )

    @cached_property
    def min_combination_count(self) -> int:
        return min([len(c) for c in self.combinations])


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day17PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
