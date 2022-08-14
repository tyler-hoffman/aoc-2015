import pytest

from advent_of_code_2015_python.day_03.b import get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        ("^v", 3),
        ("^>v<", 3),
        ("^v^v^v^v^v", 11),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 2341
