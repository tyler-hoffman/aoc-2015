from dataclasses import dataclass
from math import ceil
from typing import Iterable, Optional

from advent_of_code_2015_python.day_21.parser import Parser
from advent_of_code_2015_python.day_21.shared import Enemy, Gear, Item, Shop


@dataclass
class Day21PartASolver:
    enemy: Enemy
    shop: Shop

    @property
    def solution(self) -> int:
        lowest: Optional[int] = None
        for gear in self.get_combinations():
            if self.can_win(gear) and (lowest is None or gear.total_cost < lowest):
                lowest = gear.total_cost

        assert lowest is not None
        return lowest

    def can_win(self, gear: Gear) -> bool:
        dmg_to_enemy = max(1, gear.total_damage - self.enemy.armor)
        dmg_to_player = max(1, self.enemy.damage - gear.total_armor)

        turns_to_kill_enemy = ceil(self.enemy.hp / dmg_to_enemy)
        turns_to_kill_player = ceil(100 / dmg_to_player)

        return turns_to_kill_enemy <= turns_to_kill_player

    def get_combinations(self) -> Iterable[Gear]:
        weapons: set[Item] = self.shop.weapons.copy()
        armors: set[Optional[Item]] = {None} | self.shop.armor
        rings: set[Optional[Item]] = {None} | self.shop.rings

        for weapon in weapons:
            for armor in armors:
                for ring_1 in rings:
                    for ring_2 in rings:
                        if ring_2 is None or ring_2 is not ring_1:
                            yield Gear(
                                weapon=weapon,
                                armor=armor,
                                ring_1=ring_1,
                                ring_2=ring_2,
                            )


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
