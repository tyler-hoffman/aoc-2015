from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Sequence

from advent_of_code_2015_python.day_06.parser import Parser
from advent_of_code_2015_python.day_06.shared import Instruction, InstructionType


@dataclass
class Day06PartASolver:
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
        return self.get_on_light_count()

    def turn_on(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        for point in self.get_points(start, end):
            self.lights[point] = True

    def turn_off(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        for point in self.get_points(start, end):
            self.lights[point] = False

    def toggle(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        for point in self.get_points(start, end):
            self.lights[point] = not self.lights[point]

    def get_points(
        self, start: tuple[int, int], end: tuple[int, int]
    ) -> Iterable[tuple[int, int]]:
        x1, y1 = start
        x2, y2 = end

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                yield (x, y)

    @cached_property
    def lights(self) -> dict[tuple[int, int], bool]:
        output = dict()
        for i in range(1000):
            for j in range(1000):
                output[(i, j)] = False
        return output

    def get_on_light_count(self) -> int:
        count = 0
        for value in self.lights.values():
            if value is True:
                count += 1
        return count


def solve(input: str) -> int:
    parser = Parser()
    solver = Day06PartASolver(parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_06/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
