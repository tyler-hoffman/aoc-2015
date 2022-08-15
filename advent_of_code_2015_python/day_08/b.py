from dataclasses import dataclass
from typing import Sequence

from advent_of_code_2015_python.day_08.parser import Parser


@dataclass
class Day08PartBSolver:
    lines: Sequence[str]

    @property
    def solution(self) -> int:
        return sum([self.get_line_difference(line) for line in self.lines])

    def get_line_difference(self, line) -> int:
        return self.get_respresentation_count(line) - len(line)

    def get_respresentation_count(self, line: str) -> int:
        length = len(line)
        count = 2
        index = 0
        while index < length:
            match line[index]:
                case '"':
                    count += 2
                    index += 1
                case "\\":
                    count += 2
                    index += 1
                case _:
                    count += 1
                    index += 1
        return count


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day08PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_08/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
