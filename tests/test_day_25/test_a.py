import pytest

from advent_of_code_2015_python.day_25.a import get_solution, Day25PartASolver


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


def test_my_solution():
    assert get_solution() == "NOT THIS"
