import pytest

from advent_of_code_2015_python.day_03.a import get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 2081
