from dataclasses import dataclass
from typing import Sequence

from advent_of_code_2015_python.day_02.models import Box
from advent_of_code_2015_python.day_02.parser import Parser


@dataclass
class Day02PartASolver:
    boxes: Sequence[Box]

    @property
    def solution(self) -> int:
        return sum((self.compute_wrapping_paper(box) for box in self.boxes))

    @staticmethod
    def compute_wrapping_paper(box: Box) -> int:
        l, w, h = box.dimensions
        max_length = max(l, w, h)
        smallest_side = l * w * h // max_length
        area = 2 * l * w + 2 * w * h + 2 * h * l
        return area + smallest_side


def solve(input: str) -> int:
    solver = Day02PartASolver(Parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
