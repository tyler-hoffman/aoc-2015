import pytest

from advent_of_code_2015_python.day_01.b import get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        (")", 1),
        ("()())", 5),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 1795
