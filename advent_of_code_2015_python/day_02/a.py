from advent_of_code_2015_python.day_02.parser import Parser
from advent_of_code_2015_python.day_02.solver import Box, Solver


class Day02PartASolver(Solver):
    def compute_amount(self, box: Box) -> int:
        return self.compute_wrapping_paper(box)

    @staticmethod
    def compute_wrapping_paper(box: Box) -> int:
        l, w, h = box.dimensions
        max_length = max(l, w, h)
        smallest_side = l * w * h // max_length
        area = 2 * l * w + 2 * w * h + 2 * h * l
        return area + smallest_side


def solve(input: str) -> int:
    parser = Parser()
    solver = Day02PartASolver(parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
