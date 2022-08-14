from dataclasses import dataclass, field

from advent_of_code_2015_python.day_04.parser import Parser
from advent_of_code_2015_python.day_04.solver import Solver


@dataclass
class Day04PartASolver(Solver):
    prefix: str = field(init=False, default="00000")


def solve(input: str) -> int:
    parser = Parser()
    solver = Day04PartASolver(parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_04/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
