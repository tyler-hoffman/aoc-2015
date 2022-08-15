import pytest

from advent_of_code_2015_python.day_07.a import Day07PartASolver, get_solution, solve
from advent_of_code_2015_python.day_07.parser import Parser

SAMPLE_DATA = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""


@pytest.mark.parametrize(
    "wire, expected",
    [
        ("d", 72),
        ("e", 507),
        ("f", 492),
        ("g", 114),
        ("h", 65412),
        ("i", 65079),
        ("x", 123),
        ("y", 456),
    ],
)
def test_solve(wire: str, expected: int):
    data = tuple(Parser.parse(SAMPLE_DATA))
    solver = Day07PartASolver(data)
    assert solver.get_value(wire) == expected


def test_my_solution():
    assert get_solution() == 956
