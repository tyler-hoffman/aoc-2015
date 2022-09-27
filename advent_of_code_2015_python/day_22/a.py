from advent_of_code_2015_python.day_22.parser import Parser
from advent_of_code_2015_python.day_22.shared import Day22Solver


def solve(input: str) -> int:
    enemy = Parser.parse(input)
    solver = Day22Solver(enemy)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
