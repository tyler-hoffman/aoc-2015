from typing import Iterable


class Parser(object):
    @staticmethod
    def parse(input: str) -> Iterable[int]:
        lines = input.strip().splitlines()
        return [int(x) for x in lines]
