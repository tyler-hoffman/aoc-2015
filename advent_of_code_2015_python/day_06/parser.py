import re
from functools import cached_property
from typing import Sequence

from advent_of_code_2015_python.day_06.shared import Instruction, InstructionType


class Parser(object):
    regex_pattern = re.compile(r"(.+) (\d+),(\d+) through (\d+),(\d+)")

    @staticmethod
    def parse(input: str) -> Sequence[Instruction]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Instruction:
        instruction_type, x1_str, y1_str, x2_str, y2_str = Parser.regex_pattern.findall(
            line
        )[0]
        x1, y1, x2, y2 = map(int, (x1_str, y1_str, x2_str, y2_str))

        return Instruction(
            instruction_type=Parser.parse_instruction_type(instruction_type),
            start=(min(x1, x2), min(y1, y2)),
            end=(max(x1, x2), max(y1, y2)),
        )

    @staticmethod
    def parse_instruction_type(instruction_type: str) -> InstructionType:
        match instruction_type:
            case "turn on":
                return InstructionType.ON
            case "turn off":
                return InstructionType.OFF
            case "toggle":
                return InstructionType.TOGGLE
            case _:
                raise Exception(f"Unexpected instruction type: {instruction_type}")
