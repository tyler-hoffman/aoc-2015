from advent_of_code_2015_python.day_24.parser import Parser
from advent_of_code_2015_python.day_24.shared import Day24Solver


def solve(input: str) -> int:
    values = Parser.parse(input)
    solver = Day24Solver(values, 4)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_24/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
