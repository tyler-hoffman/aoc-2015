from advent_of_code_2015_python.day_23.a import get_solution, solve
from advent_of_code_2015_python.day_23.shared import Register

TEST_DATA = """
inc a
jio a, +2
tpl a
inc a
"""


def test_solve_sample():
    input = TEST_DATA
    assert solve(input, Register.A) == 2


def test_solve_sample_but_with_b():
    input = TEST_DATA.replace("a", "b")
    assert solve(input) == 2


def test_my_solution():
    assert get_solution() == 184
