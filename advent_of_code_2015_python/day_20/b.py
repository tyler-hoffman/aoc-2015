from dataclasses import dataclass
from functools import cached_property

from advent_of_code_2015_python.day_20.parser import Parser
from advent_of_code_2015_python.day_20.shared import DivisorCalculator


@dataclass(frozen=True)
class Day20PartBSolver:
    target: int

    @property
    def solution(self) -> int:
        house: int = 0
        while True:
            house += 1

            divisors = self.divisor_calculator.divisors(house)
            valid_divisors = {x for x in divisors if x * 50 >= house}
            presents = 11 * sum(valid_divisors)

            if presents >= self.target:
                return house

    @cached_property
    def divisor_calculator(self) -> DivisorCalculator:
        return DivisorCalculator()


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day20PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_20/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
