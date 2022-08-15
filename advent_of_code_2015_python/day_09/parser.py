from typing import Sequence

from advent_of_code_2015_python.day_09.shared import Segment


class Parser(object):
    @staticmethod
    def parse(input: str) -> Sequence[Segment]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Segment:
        a, _, b, _, distance = line.split()
        return Segment(a=a, b=b, distance=int(distance))
