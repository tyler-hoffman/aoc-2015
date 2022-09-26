from typing import Optional

from advent_of_code_2015_python.day_21.parser import Parser
from advent_of_code_2015_python.day_21.shared import Day21Solver


class Day21PartASolver(Day21Solver):
    @property
    def solution(self) -> int:
        lowest: Optional[int] = None
        for gear in self.get_combinations():
            if self.can_win(gear) and (lowest is None or gear.total_cost < lowest):
                lowest = gear.total_cost

        assert lowest is not None
        return lowest


def solve(input: str) -> int:
    shop_data: str
    with open("advent_of_code_2015_python/day_21/shop_data.txt", "r") as f:
        shop_data = f.read()
    enemy = Parser.parse_enemy(input)
    shop = Parser.parse_shop(shop_data)
    solver = Day21PartASolver(enemy=enemy, shop=shop)
    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_21/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
