from typing import Mapping

from advent_of_code_2015_python.day_13.parser import Parser
from advent_of_code_2015_python.day_13.solver import Day13Solver


def solve(input: str) -> int:
    data = Parser.parse(input)
    data = add_me_to_data(data)

    solver = Day13Solver(data)

    return solver.solution


def add_me_to_data(data: Mapping[tuple[str, str], int]):
    new_data = dict(data)
    names = Day13Solver(data).all_names
    for name in names:
        new_data[("me", name)] = 0
        new_data[(name, "me")] = 0
    return new_data


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_13/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
