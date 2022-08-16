import pytest

from advent_of_code_2015_python.day_10.solver import Solver


@pytest.mark.parametrize(
    "input, expected",
    [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211"),
    ],
)
def test_next(input: str, expected: int):
    assert Solver.next(input) == expected
