import pytest

from advent_of_code_2015_python.day_04.a import get_solution, solve


def test_solve():
    assert solve("abcdef") == 609043


def test_my_solution():
    assert get_solution() == 117946
