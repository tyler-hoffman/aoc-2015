import pytest

from advent_of_code_2015_python.day_09.a import get_solution, solve

SAMPLE_DATA = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 605


def test_my_solution():
    assert get_solution() == 117
