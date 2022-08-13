import pytest

from advent_of_code_2015_python.day_02.a import Day02PartASolver, get_solution, solve
from advent_of_code_2015_python.day_02.parser import Parser


SAMPLE_INPUT = """
2x3x4
1x1x10
"""

@pytest.mark.parametrize(
    "input, expected",
    [
        ("2x3x4", 58),
        ("1x1x10", 43),
    ],
)
def test_compute_wrapping_paper(input: str, expected: int):
    box = Parser.parse_line(input)
    assert Day02PartASolver.compute_wrapping_paper(box) == expected

def test_solve():
    assert solve(SAMPLE_INPUT) == 58 + 43


def test_my_solution():
    assert get_solution() == 1586300
