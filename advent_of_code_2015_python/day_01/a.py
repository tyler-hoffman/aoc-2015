from advent_of_code_2015_python.day_01.parser import Parser
from advent_of_code_2015_python.day_01.solver import Solver


class Day01PartASolver(Solver):
    @property
    def solution(self) -> int:
        output = 0
        for char in self.input:
            if char == "(":
                output += 1
            else:
                output -= 1
        return output


def solve(input: str) -> int:
    parser = Parser()
    solver = Day01PartASolver(parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
