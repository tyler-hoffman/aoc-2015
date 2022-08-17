import re
from typing import Mapping


class Parser(object):
    regex_pattern = re.compile(
        r"(\w+) would (gain|lose) (-?\d+) happiness units? by sitting next to (\w+)."
    )

    @staticmethod
    def parse(input: str) -> Mapping[tuple[str, str], int]:
        output: dict[tuple[str, str], int] = dict()
        lines = input.strip().splitlines()
        for line in lines:
            a, b, happiness = Parser.parse_line(line)
            output[(a, b)] = happiness
        return output

    @staticmethod
    def parse_line(line: str) -> tuple[str, str, int]:
        a, gain_or_lose, happiness, b = Parser.regex_pattern.findall(line)[0]
        multiplier = 1 if gain_or_lose == "gain" else -1
        return a, b, int(happiness) * multiplier
