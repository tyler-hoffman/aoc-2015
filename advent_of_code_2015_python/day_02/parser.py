from typing import Sequence

from advent_of_code_2015_python.day_02.models import Box


class Parser(object):
    @staticmethod
    def parse(input: str) -> Sequence[Box]:
        lines = input.strip().split()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Box:
        length, width, height = (int(x) for x in line.split("x"))
        return Box(length=length, width=width, height=height)
