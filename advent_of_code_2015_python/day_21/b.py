from typing import Optional

from advent_of_code_2015_python.day_21.parser import Parser
from advent_of_code_2015_python.day_21.shared import Day21Solver


class Day21PartBSolver(Day21Solver):
    @property
    def solution(self) -> int:
        highest: Optional[int] = None
        for gear in self.get_combinations():
            if not self.can_win(gear) and (
                highest is None or gear.total_cost > highest
            ):
                highest = gear.total_cost

        assert highest is not None
        return highest


def solve(input: str) -> int:
    shop_data: str
    with open("advent_of_code_2015_python/day_21/shop_data.txt", "r") as f:
        shop_data = f.read()
    enemy = Parser.parse_enemy(input)
    shop = Parser.parse_shop(shop_data)
    solver = Day21PartBSolver(enemy=enemy, shop=shop)
    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_21/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
