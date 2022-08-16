from advent_of_code_2015_python.day_10.parser import Parser
from advent_of_code_2015_python.day_10.solver import Solver


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Solver(data, 50)
    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_10/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
