import pytest

from advent_of_code_2015_python.day_08.a import Day08PartASolver, get_solution, solve
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
        ('""', 0),
        ('"abc"', 3),
        ('"aaa\\"aaa"', 7),
        ('"\\x27"', 1),
    ],
)
def test_representation_count(input: str, expected: int):
    solver = Day08PartASolver([])
    assert solver.get_respresentation_count(input) == expected


def test_solve():
    data = Parser.parse(SAMPLE_DATA)
    solver = Day08PartASolver(data)
    assert solver.solution == 12


def test_my_solution():
    assert get_solution() == 1333
