import re


class Parser(object):
    regex_pattern = re.compile(r"(\d+)")

    @staticmethod
    def parse(input: str) -> tuple[int, int]:
        line = input.strip()
        row, col = (int(x) for x in Parser.regex_pattern.findall(line))
        return row, col
