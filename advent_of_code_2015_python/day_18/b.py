from dataclasses import dataclass
from typing import Sequence

from advent_of_code_2015_python.day_18.parser import Parser
from advent_of_code_2015_python.day_18.shared import Grid


@dataclass
class Day18PartBSolver:
    data: Sequence[Sequence[bool]]
    iterations: int

    @property
    def solution(self) -> int:
        grid = Grid.from_2d_array(self.data)
        self.force_corners_on(grid)
        for _ in range(self.iterations):
            grid = grid.next()
            self.force_corners_on(grid)
        return grid.on_cell_count

    def force_corners_on(self, grid: Grid) -> None:
        big_x = grid.width - 1
        big_y = grid.height - 1
        grid.on_cells.add((0, 0))
        grid.on_cells.add((0, big_y))
        grid.on_cells.add((big_x, 0))
        grid.on_cells.add((big_x, big_y))


def solve(input: str, iterations: int = 100) -> int:
    data = Parser.parse(input)
    solver = Day18PartBSolver(data, iterations)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_18/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
