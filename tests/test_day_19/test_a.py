from advent_of_code_2015_python.day_19.a import get_solution, solve

SAMPLE_DATA = """
H => HO
H => OH
O => HH

HOH
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 4


def test_my_solution():
    assert get_solution() == 518
