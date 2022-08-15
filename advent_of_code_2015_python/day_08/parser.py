from typing import Sequence


class Parser(object):
    @staticmethod
    def parse(input: str) -> Sequence[str]:
        return input.strip().splitlines()
