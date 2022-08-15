from functools import cache
from typing import Union

from advent_of_code_2015_python.day_07.a import Day07PartASolver
from advent_of_code_2015_python.day_07.parser import Parser


class Day07PartBSolver(Day07PartASolver):
    @cache
    def get_value(self, value: Union[str, int]) -> int:
        if value == "b":
            return Day07PartASolver(self.gates).solution
        else:
            return super().get_value(value)


def solve(input: str) -> int:
    gates = tuple(Parser.parse(input))
    solver = Day07PartBSolver(gates)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_07/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
