import re
from typing import Sequence

from advent_of_code_2015_python.day_15.shared import Ingredient


class Parser(object):
    regex_pattern = re.compile(
        r"(\w+):.+ (-?\d+).+ (-?\d+).+ (-?\d+).+ (-?\d+).+ (-?\d+)"
    )

    @staticmethod
    def parse(input: str) -> Sequence[Ingredient]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Ingredient:
        (
            name,
            capacity,
            durability,
            flavor,
            texture,
            calories,
        ) = Parser.regex_pattern.findall(line)[0]

        return Ingredient(
            name=name,
            capacity=int(capacity),
            durability=int(durability),
            flavor=int(flavor),
            texture=int(texture),
            calories=int(calories),
        )
