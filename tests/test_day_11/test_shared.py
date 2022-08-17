import pytest

from advent_of_code_2015_python.day_11.shared import Password


@pytest.mark.parametrize(
    "input, expected",
    [
        ("xx", "xy"),
        ("xy", "xz"),
        ("xz", "ya"),
        ("ya", "yb"),
    ],
)
def test_next(input: str, expected: str):
    assert Password(input).increment() == Password(expected)
