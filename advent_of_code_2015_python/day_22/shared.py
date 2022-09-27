from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import total_ordering
from queue import PriorityQueue
from typing import Any, Iterable, Type


@dataclass
class Player:
    hp: int = 50
    mp: int = 500
    armor: int = 0

    def copy(self) -> Player:
        return Player(
            hp=self.hp,
            mp=self.mp,
            armor=self.armor,
        )


@dataclass
class Enemy:
    hp: int
    dmg: int

    def copy(self) -> Enemy:
        return Enemy(
            hp=self.hp,
            dmg=self.dmg,
        )


@total_ordering
@dataclass
class GameState:
    player: Player
    enemy: Enemy
    mana_used: int = 0
    is_player_turn: bool = False
    status_effects: set[StatusEffect] = field(default_factory=set)

    def __lt__(self, _) -> bool:
        return False

    def copy(self) -> GameState:
        return GameState(
            player=self.player.copy(),
            enemy=self.enemy.copy(),
            mana_used=self.mana_used,
            is_player_turn=self.is_player_turn,
            status_effects={s.copy() for s in self.status_effects},
        )

    @property
    def won(self) -> bool:
        return self.enemy.hp <= 0

    @property
    def lost(self) -> bool:
        return self.player.hp <= 0

    @property
    def key_stats(self) -> tuple[Any, ...]:
        """We're mutating state, and want something hashable"""
        return (
            self.player.hp,
            self.player.mp,
            self.player.armor,
            self.enemy.hp,
            # self.mana_used,
            frozenset({(s.__class__, s.remaining) for s in self.status_effects}),
        )


class StatusEffect(ABC):
    def __init__(self, remaining: int) -> None:
        self.remaining = remaining

    def start(self, state: GameState) -> None:
        ...

    def end(self, state: GameState) -> None:
        ...

    def on_turn(self, state: GameState) -> None:
        ...

    def copy(self) -> StatusEffect:
        return self.__class__(self.remaining)


class ShieldStatus(StatusEffect):
    def start(self, state: GameState) -> None:
        state.player.armor += 7

    def end(self, state: GameState) -> None:
        state.player.armor -= 7


class PoisonStatus(StatusEffect):
    def on_turn(self, state: GameState) -> None:
        state.enemy.hp -= 3


class RechargeStatus(StatusEffect):
    def on_turn(self, state: GameState) -> None:
        state.player.mp += 101


class Ability(ABC):
    @property
    @abstractmethod
    def cost(self) -> int:
        ...

    def can_do(self, state: GameState) -> bool:
        return state.player.mp >= self.cost

    @abstractmethod
    def update_state(self, state: GameState) -> None:
        ...


class StatusAbility(Ability):
    @property
    @abstractmethod
    def status_effect_type(self) -> Type[StatusEffect]:
        ...

    @property
    @abstractmethod
    def status_effect_turns(self) -> int:
        ...

    def get_status_effect(self) -> StatusEffect:
        return self.status_effect_type(self.status_effect_turns)

    def can_do(self, state: GameState) -> bool:
        already_exists = any(
            [s for s in state.status_effects if isinstance(s, self.status_effect_type)]
        )
        return super().can_do(state) and not already_exists

    def update_state(self, state: GameState) -> None:
        status_effect = self.get_status_effect()
        state.status_effects.add(status_effect)
        status_effect.start(state)


class MagicMissile(Ability):
    @property
    def cost(self) -> int:
        return 53

    def update_state(self, state: GameState) -> None:
        state.enemy.hp -= 4


class Drain(Ability):
    @property
    def cost(self) -> int:
        return 73

    def update_state(self, state: GameState) -> None:
        state.enemy.hp -= 2
        state.player.hp += 2


class Shield(StatusAbility):
    @property
    def cost(self) -> int:
        return 113

    @property
    def status_effect_type(self) -> Type[StatusEffect]:
        return ShieldStatus

    @property
    def status_effect_turns(self) -> int:
        return 6


class Poison(StatusAbility):
    @property
    def cost(self) -> int:
        return 173

    @property
    def status_effect_type(self) -> Type[StatusEffect]:
        return PoisonStatus

    @property
    def status_effect_turns(self) -> int:
        return 6


class Recharge(StatusAbility):
    @property
    def cost(self) -> int:
        return 229

    @property
    def status_effect_type(self) -> Type[StatusEffect]:
        return RechargeStatus

    @property
    def status_effect_turns(self) -> int:
        return 5


ALL_ABILITIES: set[Ability] = {
    MagicMissile(),
    Drain(),
    Shield(),
    Poison(),
    Recharge(),
}


@dataclass(frozen=True)
class Day22Solver:
    enemy: Enemy

    @property
    def solution(self) -> int:
        added_to_queue = set()
        queue: PriorityQueue[tuple[int, GameState]] = PriorityQueue()
        queue.put((0, GameState(player=Player(), enemy=self.enemy)))

        while True:
            _, state = queue.get()

            if state.won:
                return state.mana_used

            for next_state in self.next_states(state):
                if not next_state.lost and next_state.key_stats not in added_to_queue:
                    queue.put((next_state.mana_used, next_state))
                    added_to_queue.add(next_state.key_stats)

    def next_states(self, state: GameState) -> Iterable[GameState]:
        next_state = state.copy()
        next_state.is_player_turn = not next_state.is_player_turn

        if next_state.is_player_turn:
            yield from self.get_player_turns(next_state)
        else:
            yield from self.get_enemy_turns(next_state)

    def get_player_turns(self, state: GameState) -> Iterable[GameState]:
        self.perform_statuses(state)
        for ability in [a for a in ALL_ABILITIES if a.can_do(state)]:
            next_state = state.copy()
            ability.update_state(next_state)
            next_state.player.mp -= ability.cost
            next_state.mana_used += ability.cost
            yield next_state

    def get_enemy_turns(self, state: GameState) -> Iterable[GameState]:
        self.perform_statuses(state)
        dmg = max(1, state.enemy.dmg - state.player.armor)
        state.player.hp -= dmg
        yield state

    def perform_statuses(self, state: GameState) -> None:
        for status in state.status_effects:
            status.on_turn(state)
            status.remaining -= 1
            if status.remaining == 0:
                status.end(state)
        state.status_effects = {s for s in state.status_effects if s.remaining > 0}
