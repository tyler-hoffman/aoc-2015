import pytest

from advent_of_code_2015_python.day_01.a import get_solution, solve


# class TestDay01A(unittest.TestCase):
@pytest.mark.parametrize(
    "input, expected",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 74
