import pytest

from advent_of_code_2015_python.day_20.shared import DivisorCalculator


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, {1}),
        (2, {1, 2}),
        (3, {1, 3}),
        (4, {1, 2, 4}),
        (120, {1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120}),
    ],
)
def test_divisor_calculator(input: int, expected: set[int]):
    divisor_calculator = DivisorCalculator()
    output = divisor_calculator.divisors(input)
    assert output == expected
