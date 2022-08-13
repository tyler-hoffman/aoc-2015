def create_parser_stub() -> str:
    return _PARSER_TEMPLATE


_PARSER_TEMPLATE = """
from typing import List


class Parser(object):
    @staticmethod
    def parse(input: str) -> List[str]:
        raise NotImplementedError()

"""
