import pytest

from advent_of_code_2015_python.day_14.a import get_solution, solve

SAMPLE_DATA = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip()


@pytest.mark.parametrize(
    "input, expected",
    [
        (SAMPLE_DATA.splitlines()[0], 1120),
        (SAMPLE_DATA.splitlines()[1], 1056),
        (SAMPLE_DATA, 1120),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input, 1000) == expected


def test_my_solution():
    assert get_solution() == 2655
