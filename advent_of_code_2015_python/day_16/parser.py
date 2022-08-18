import re

from advent_of_code_2015_python.day_16.shared import Sue


class Parser(object):
    regex_pattern = re.compile(r"(\w+).+?(\d+)")

    @staticmethod
    def parse(input: str) -> set[Sue]:
        lines = input.strip().splitlines()
        return {Parser.parse_line(line) for line in lines}

    @staticmethod
    def parse_line(line: str) -> Sue:
        parts = Parser.regex_pattern.findall(line)
        _, id = parts[0]
        attributes = {name: int(count) for name, count in parts[1:]}
        return Sue(id=int(id), **attributes)
