from dataclasses import dataclass
from typing import Sequence

from advent_of_code_2015_python.day_18.parser import Parser
from advent_of_code_2015_python.day_18.shared import Grid


@dataclass
class Day18PartASolver:
    data: Sequence[Sequence[bool]]
    iterations: int

    @property
    def solution(self) -> int:
        grid = Grid.from_2d_array(self.data)
        for _ in range(self.iterations):
            grid = grid.next()
        return grid.on_cell_count


def solve(input: str, iterations: int = 100) -> int:
    data = Parser.parse(input)
    solver = Day18PartASolver(data, iterations)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_18/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
