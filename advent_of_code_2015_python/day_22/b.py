from typing import Iterable

from advent_of_code_2015_python.day_22.parser import Parser
from advent_of_code_2015_python.day_22.shared import Day22Solver, GameState


class Day22PartBSolver(Day22Solver):
    def get_player_turns(self, state: GameState) -> Iterable[GameState]:
        state.player.hp -= 1
        if not state.lost:
            yield from super().get_player_turns(state)


def solve(input: str) -> int:
    enemy = Parser.parse(input)
    solver = Day22PartBSolver(enemy)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
