import pytest

from advent_of_code_2015_python.day_11.a import get_solution, solve
from advent_of_code_2015_python.day_11.shared import Password


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abcdefgh", "abcdffaa"),
        ("ghijklmn", "ghjaabcc"),
    ],
)
def test_solve(input: str, expected: str):
    assert solve(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("hijklmmn", True),
        ("abbceffg", False),
    ],
)
def test_has_run(input: str, expected: bool):
    assert Password(input).has_run == expected


def test_has_prohibited_char():
    assert Password("hijklmmn").has_prohibited_chars == True


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abbceffg", True),
        ("abbcegjk", False),
    ],
)
def test_has_non_overlapping_pair(input: str, expected: bool):
    assert Password(input).has_non_overlapping_pair == expected


def test_my_solution():
    assert get_solution() == "cqjxxyzz"
