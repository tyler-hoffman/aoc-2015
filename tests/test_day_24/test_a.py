import pytest

from advent_of_code_2015_python.day_24.a import get_solution, solve

SAMPLE = """
1
2
3
4
5
7
8
9
10
11
"""


@pytest.mark.parametrize(
    "input, expected",
    [
        (SAMPLE, 99),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 10439961859
