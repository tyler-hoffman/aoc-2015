from advent_of_code_2015_python.day_15.b import get_solution, solve

SAMPLE_DATA = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


def test_solve():
    assert solve(SAMPLE_DATA) == 57600000


def test_my_solution():
    assert get_solution() == 11171160
