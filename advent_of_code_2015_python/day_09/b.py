from dataclasses import dataclass
from typing import Callable, Sequence

from advent_of_code_2015_python.day_09.parser import Parser
from advent_of_code_2015_python.day_09.shared import Segment, Solver


@dataclass
class Day09PartBSolver(Solver):
    segments: Sequence[Segment]
    is_better: Callable[[int, int], bool] = lambda a, b: a > b


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
