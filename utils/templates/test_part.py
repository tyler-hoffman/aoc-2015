def create_part_test_stub(day_string: str, part: str) -> str:
    src = "advent_of_code_2015_python"
    return _TEST_PART_TEMPLATE.format(
        day_string=day_string,
        part=part,
        part_upper=part.upper(),
        src=src,
    )


_TEST_PART_TEMPLATE = """
import unittest

from .sample_data import SAMPLE_DATA
from {src}.day_{day_string}.{part} import solve


class TestDay{day_string}{part_upper}(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1)

"""
