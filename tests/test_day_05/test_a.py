import pytest

from advent_of_code_2015_python.day_05.a import Day05PartASolver, get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_is_nice(input: str, expected: bool):
    solver = Day05PartASolver([])
    assert solver.is_nice(input) == expected


def test_my_solution():
    assert get_solution() == 236
