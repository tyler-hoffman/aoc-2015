import pytest

from advent_of_code_2015_python.day_05.b import Day05PartBSolver, get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_is_nice(input: str, expected: bool):
    solver = Day05PartBSolver([])
    assert solver.is_nice(input) == expected


def test_my_solution():
    assert get_solution() == 51
