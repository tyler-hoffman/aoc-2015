import re
from typing import Sequence


class Parser(object):
    int_regex_pattern = re.compile(r"(-?\d+)")

    @staticmethod
    def parse(input: str) -> str:
        return input.strip()

    @staticmethod
    def parse_ints(input: str) -> Sequence[int]:
        cleaned = Parser.parse(input)

        ints = Parser.int_regex_pattern.findall(cleaned)

        return [int(x) for x in ints]
