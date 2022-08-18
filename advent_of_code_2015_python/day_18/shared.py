from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Sequence


@dataclass
class Grid:
    width: int
    height: int
    on_cells: set[tuple[int, int]]

    def next(self) -> Grid:
        next_on_cells: set[tuple[int, int]] = set()
        for point in self.cells_to_check:
            neighbor_count = self.count_neighbors(point)
            is_on = point in self.on_cells
            if is_on and neighbor_count in (2, 3):
                next_on_cells.add(point)
            elif neighbor_count == 3 and not is_on:
                next_on_cells.add(point)
        return Grid(self.width, self.height, next_on_cells)

    @cached_property
    def cells_to_check(self) -> set[tuple[int, int]]:
        output: set[tuple[int, int]] = set()
        for x in range(self.width):
            for y in range(self.height):
                output.add((x, y))
        return output

    def count_neighbors(self, point: tuple[int, int]) -> int:
        output = 0
        for neighbor in self.get_neighbors(point):
            i, j = neighbor
            if (i, j) in self.on_cells:
                output += 1
        return output

    def get_neighbors(self, point: tuple[int, int]) -> set[tuple[int, int]]:
        x, y = point
        output: set[tuple[int, int]] = set()
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                is_middle = i == x and j == y
                if not is_middle:
                    output.add((i, j))
        return output

    @cached_property
    def on_cell_count(self) -> int:
        return len(self.on_cells)

    @staticmethod
    def from_2d_array(grid: Sequence[Sequence[bool]]) -> Grid:
        on_cells: set[tuple[int, int]] = set()
        for y, line in enumerate(grid):
            for x, val in enumerate(line):
                if val:
                    on_cells.add((x, y))
        return Grid(
            len(grid[0]),
            len(grid),
            on_cells,
        )
