from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


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
