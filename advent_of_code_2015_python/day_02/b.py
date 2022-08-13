from advent_of_code_2015_python.day_02.parser import Parser
from advent_of_code_2015_python.day_02.solver import Box, Solver


class Day02PartBSolver(Solver):
    def compute_amount(self, box: Box) -> int:
        return self.compute_ribbon(box)

    @staticmethod
    def compute_ribbon(box: Box) -> int:
        a, b, c = sorted(box.dimensions)
        volume = a * b * c
        smallest_perimiter = 2 * (a + b)
        return volume + smallest_perimiter


def solve(input: str) -> int:
    parser = Parser()
    solver = Day02PartBSolver(parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
