from advent_of_code_2015_python.day_01.parser import Parser
from advent_of_code_2015_python.day_01.solver import Solver


class Day01PartBSolver(Solver):
    @property
    def solution(self) -> int:
        floor = 0
        for i, char in enumerate(self.input):
            if char == "(":
                floor += 1
            else:
                floor -= 1

            if floor == -1:
                return i + 1

        raise Exception("No solution found!")


def solve(input: str) -> int:
    parser = Parser()
    solver = Day01PartBSolver(parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
