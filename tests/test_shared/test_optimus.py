import pytest

from advent_of_code_2015_python.shared.optimus import Optimus


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
    ],
)
def test_is_prime(input: int, expected: bool):
    optimus = Optimus()
    assert optimus.is_prime(input) is expected
