from typing import Sequence


class Parser(object):
    @staticmethod
    def parse(input: str) -> Sequence[str]:
        return [x for x in input.strip()]
