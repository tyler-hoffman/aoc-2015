from advent_of_code_2015_python.day_17.parser import Parser
from advent_of_code_2015_python.day_17.shared import Day17Solver


class Day17PartASolver(Day17Solver):
    @property
    def solution(self) -> int:
        return len(self.combinations)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day17PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
