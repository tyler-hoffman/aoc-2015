from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Sequence, Tuple

from advent_of_code_2015_python.day_05.parser import Parser
from advent_of_code_2015_python.day_05.solver import Solver, sliding_window


@dataclass
class Day05PartASolver(Solver):
    strings: Sequence[str]

    @property
    def rules(self) -> Iterable[Callable[[str], bool]]:
        return [
            self.has_three_vowels,
            self.has_double_char,
            self.no_prohibited_pairs,
        ]

    def has_three_vowels(self, word: str) -> bool:
        VOWELS = "aeiou"
        vowles_in_word = [x for x in word if x in VOWELS]
        return len(vowles_in_word) >= 3

    def has_double_char(self, word: str) -> bool:
        for a, b in sliding_window(word, 2):
            if a == b:
                return True
        return False

    def no_prohibited_pairs(self, word: str) -> bool:
        prohibited = ["ab", "cd", "pq", "xy"]
        for p in prohibited:
            if p in word:
                return False
        return True


def solve(input: str) -> int:
    solver = Day05PartASolver(Parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
