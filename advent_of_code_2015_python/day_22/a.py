from dataclasses import dataclass
from queue import PriorityQueue
from typing import Iterable
from advent_of_code_2015_python.day_22.parser import Parser
from advent_of_code_2015_python.day_22.shared import (
    ALL_ABILITIES,
    Ability,
    Enemy,
    GameState,
    Player,
)


@dataclass(frozen=True)
class Day22PartASolver:
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

    def next_states(self, old_state: GameState) -> Iterable[GameState]:
        state = old_state.copy()

        self.perform_statuses(state)
        if state.is_player_turn:
            usable_abilities = [a for a in ALL_ABILITIES if a.can_do(state)]
            if not usable_abilities:
                next_state = state.copy()
                next_state.player_had_no_move = True
                next_state.is_player_turn = not next_state.is_player_turn
                yield next_state
            for ability in usable_abilities:
                next_state = state.copy()
                self.do_player_turn(next_state, ability)
                next_state.is_player_turn = not next_state.is_player_turn
                yield next_state
        else:
            next_state = state.copy()
            self.do_enemy_turn(next_state)
            next_state.is_player_turn = not next_state.is_player_turn
            yield next_state


    def do_player_turn(self, state: GameState, ability: Ability) -> None:
        ability.update_state(state)
        state.player.mp -= ability.cost
        state.mana_used += ability.cost

    def do_enemy_turn(self, state: GameState) -> None:
        dmg = max(1, state.enemy.dmg - state.player.armor)
        state.player.hp -= dmg

    def perform_statuses(self, state: GameState) -> None:
        for status in state.status_effects:
            status.on_turn(state)
            status.remaining -= 1
            if status.remaining == 0:
                status.end(state)
        state.status_effects = {s for s in state.status_effects if s.remaining > 0}


def solve(input: str) -> int:
    enemy = Parser.parse(input)
    solver = Day22PartASolver(enemy)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
