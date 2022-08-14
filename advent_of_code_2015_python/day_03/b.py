from dataclasses import dataclass, field
from advent_of_code_2015_python.day_03.parser import Parser
from advent_of_code_2015_python.day_03.solver import Solver
from shared.models import Point


@dataclass
class Day03PartBSolver(Solver):
    input: str

    santa: Point = field(init=False, default_factory=Point)
    robo_santa: Point = field(init=False, default_factory=Point)
    santas_turn: bool = field(init=False, default=True)

    def do_move(self, move: Point) -> None:
        if self.santas_turn:
            self.santa = self.santa.add(move)
            self.visited.add(self.santa)
        else:
            self.robo_santa = self.robo_santa.add(move)
            self.visited.add(self.robo_santa)
        self.santas_turn = not self.santas_turn


def solve(input: str) -> int:
    parser = Parser()
    solver = Day03PartBSolver(parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_03/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
