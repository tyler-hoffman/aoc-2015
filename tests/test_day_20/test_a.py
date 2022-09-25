import pytest

from advent_of_code_2015_python.day_20.a import get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        ("9", 1),
        ("10", 1),
        ("11", 2),
        ("120", 6),
        ("130", 8),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 776160
