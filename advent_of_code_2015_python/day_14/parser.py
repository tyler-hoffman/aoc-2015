import re

from advent_of_code_2015_python.day_14.shared import Reindeer


class Parser(object):
    regex_pattern = re.compile(
        r"(\w+) can fly (\d+) km/s for (\d+) seconds?, but then must rest for (\d+) seconds?."
    )

    @staticmethod
    def parse(input: str) -> set[Reindeer]:
        lines = input.strip().splitlines()
        return {Parser.parse_line(line) for line in lines}

    @staticmethod
    def parse_line(line: str) -> Reindeer:
        name, km_p_s, fly_time, rest_time = Parser.regex_pattern.findall(line)[0]
        return Reindeer(
            name=name,
            km_per_s=int(km_p_s),
            fly_time=int(fly_time),
            rest_time=int(rest_time),
        )
