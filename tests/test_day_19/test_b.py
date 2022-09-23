import pytest

from advent_of_code_2015_python.day_19.b import get_solution, solve

HOH_SAMPLE_DATA = """
e => H
e => O
H => HO
H => OH
O => HH

HOH
"""
HOHOHO_SAMPLE_DATA = """
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
"""


@pytest.mark.parametrize(
    "input, expected",
    [
        (HOH_SAMPLE_DATA, 3),
        (HOHOHO_SAMPLE_DATA, 6),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 200
