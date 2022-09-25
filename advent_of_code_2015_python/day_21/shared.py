from abc import ABC
from dataclasses import dataclass
from enum import Enum, auto
from math import ceil
from typing import Iterable, Optional


class ItemCategory(Enum):
    WEAPON = auto()
    ARMOR = auto()
    RING = auto()


@dataclass(frozen=True)
class Item:
    name: str
    cost: int
    damage: int
    armor: int


@dataclass(frozen=True)
class Gear:
    weapon: Item
    armor: Optional[Item]
    ring_1: Optional[Item]
    ring_2: Optional[Item]

    @property
    def total_armor(self) -> int:
        return sum([item.armor for item in self.items])

    @property
    def total_cost(self) -> int:
        return sum([item.cost for item in self.items])

    @property
    def total_damage(self) -> int:
        return sum([item.damage for item in self.items])

    @property
    def items(self) -> set[Item]:
        all_slots = {
            self.weapon,
            self.armor,
            self.ring_1,
            self.ring_2,
        }
        return {x for x in all_slots if x is not None}


@dataclass(frozen=True)
class Enemy:
    hp: int
    damage: int
    armor: int


@dataclass(frozen=True)
class Shop:
    weapons: set[Item]
    armor: set[Item]
    rings: set[Item]


@dataclass
class Day21Solver(ABC):
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
