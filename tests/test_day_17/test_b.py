import pytest

from advent_of_code_2015_python.day_17.b import Day17PartBSolver, get_solution


def test_solve():
    containers = [20, 15, 10, 5, 5]
    total_amount = 25
    assert Day17PartBSolver(containers, total_amount).solution == 3


def test_my_solution():
    assert get_solution() == 57
