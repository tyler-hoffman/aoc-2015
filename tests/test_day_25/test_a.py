import pytest

from advent_of_code_2015_python.day_25.a import Day25PartASolver, get_solution, solve


@pytest.mark.parametrize(
    "row, col, expected",
    [
        (1, 1, 1),
        (1, 2, 3),
        (1, 3, 6),
        (2, 2, 5),
        (2, 3, 9),
        (3, 4, 19),
        (4, 3, 18),
    ],
)
def test_position_to_index(row: int, col: int, expected: int):
    index = Day25PartASolver.position_to_index(row, col)
    assert index == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("1, 1", 20151125),
        ("1, 2", 18749137),
        ("2, 6", 4041754),
        ("6, 6", 27995004),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 9132360
