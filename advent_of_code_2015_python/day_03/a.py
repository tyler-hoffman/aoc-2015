from dataclasses import dataclass, field

from advent_of_code_2015_python.day_03.parser import Parser
from advent_of_code_2015_python.day_03.solver import Solver
from advent_of_code_2015_python.shared.models import Point


@dataclass
class Day03PartASolver(Solver):
    input: str
    pos: Point = field(init=False, default_factory=Point)

    def do_move(self, move: Point) -> None:
        self.pos = self.pos.add(move)
        self.visited.add(self.pos)


def solve(input: str) -> int:
    solver = Day03PartASolver(Parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_03/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
