from typing import Sequence


class Parser(object):
    @staticmethod
    def parse(input: str) -> Sequence[Sequence[bool]]:
        lines = input.strip().splitlines()
        return [[c == "#" for c in line] for line in lines]
