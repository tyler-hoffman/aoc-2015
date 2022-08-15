import pytest

from advent_of_code_2015_python.day_08.b import Day08PartBSolver, get_solution, solve
from advent_of_code_2015_python.day_08.parser import Parser

SAMPLE_DATA = """
""
"abc"
"aaa\\\"aaa"
"\\x27"
"""


@pytest.mark.parametrize(
    "input, expected",
    [
        ('""', 6),
        ('"abc"', 9),
        ('"aaa\\"aaa"', 16),
        ('"\\x27"', 11),
    ],
)
def test_representation_count(input: str, expected: int):
    solver = Day08PartBSolver([])
    assert solver.get_respresentation_count(input) == expected


def test_solve():
    data = Parser.parse(SAMPLE_DATA)
    solver = Day08PartBSolver(data)
    assert solver.solution == 19


def test_my_solution():
    assert get_solution() == 2046
