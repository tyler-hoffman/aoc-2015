from advent_of_code_2015_python.day_17.a import Day17PartASolver, get_solution


def test_solve():
    containers = [20, 15, 10, 5, 5]
    total_amount = 25
    assert Day17PartASolver(containers, total_amount).solution == 4


def test_my_solution():
    assert get_solution() == 654
