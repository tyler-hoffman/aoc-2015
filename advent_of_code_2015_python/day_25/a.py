from dataclasses import dataclass
from advent_of_code_2015_python.day_25.parser import Parser


@dataclass
class Day25PartASolver:
    row: int
    col: int

    @property
    def solution(self) -> int:
        return -1

    @staticmethod
    def position_to_index(row: int, col: int) -> int:
        index = 0
        for i in range(1, col + 1):
            index += i
        for j in range(0, row - 1):
            index += col + j
        return index


def solve(input: str) -> int:
    row, col = Parser.parse(input)
    solver = Day25PartASolver(row, col)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_25/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
