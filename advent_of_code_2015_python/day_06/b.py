from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterable, Sequence

from advent_of_code_2015_python.day_06.parser import Parser
from advent_of_code_2015_python.day_06.shared import Instruction, InstructionType


@dataclass
class Day06PartBSolver:
    instructions: Sequence[Instruction]

    @property
    def solution(self) -> int:
        for instruction in self.instructions:
            match instruction.instruction_type:
                case InstructionType.ON:
                    self.turn_on(instruction.start, instruction.end)
                case InstructionType.OFF:
                    self.turn_off(instruction.start, instruction.end)
                case InstructionType.TOGGLE:
                    self.toggle(instruction.start, instruction.end)
                case _:
                    raise Exception(
                        f"Unexpected instruction type: {instruction.instruction_type}"
                    )
        return self.brightness()

    def turn_on(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        for point in self.get_points(start, end):
            self.lights[point] += 1

    def turn_off(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        for point in self.get_points(start, end):
            self.lights[point] -= 1
            if self.lights[point] < 0:
                self.lights[point] = 0

    def toggle(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        for point in self.get_points(start, end):
            self.lights[point] += 2

    def get_points(
        self, start: tuple[int, int], end: tuple[int, int]
    ) -> Iterable[tuple[int, int]]:
        x1, y1 = start
        x2, y2 = end

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                yield (x, y)

    @cached_property
    def lights(self) -> dict[tuple[int, int], int]:
        output = dict()
        for i in range(1000):
            for j in range(1000):
                output[(i, j)] = 0
        return output

    def brightness(self) -> int:
        return sum(self.lights.values())


def solve(input: str) -> int:
    solver = Day06PartBSolver(Parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_06/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
