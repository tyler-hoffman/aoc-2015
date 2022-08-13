import pytest

from advent_of_code_2015_python.day_02.a import Day02PartASolver
from advent_of_code_2015_python.day_02.b import (Day02PartBSolver,
                                                 get_solution, solve)
from advent_of_code_2015_python.day_02.parser import Parser

SAMPLE_INPUT = """
2x3x4
1x1x10
"""


@pytest.mark.parametrize(
    "input, expected",
    [
        ("2x3x4", 34),
        ("1x1x10", 14),
    ],
)
def test_compute_ribben(input: str, expected: int):
    box = Parser.parse_line(input)
    assert Day02PartBSolver.compute_ribbon(box) == expected


def test_solve():
    assert solve(SAMPLE_INPUT) == 34 + 14


def test_my_solution():
    assert get_solution() == 3737498
