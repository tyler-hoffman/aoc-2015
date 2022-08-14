from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Iterable, Sequence, Tuple
from advent_of_code_2015_python.day_05.parser import Parser


@dataclass
class Day05PartASolver:
    strings: Sequence[str]

    @property
    def solution(self) -> int:
        nice_words = [word for word in self.strings if self.is_nice(word)]
        return len(nice_words)

    def is_nice(self, word: str) -> bool:
        return all((rule(word) for rule in self.rules))

    def has_three_vowels(self, word: str) -> bool:
        VOWELS = "aeiou"
        vowles_in_word = [x for x in word if x in VOWELS]
        return len(vowles_in_word) >= 3

    def has_double_char(self, word: str) -> bool:
        for a, b in self.pairs(word):
            if a == b:
                return True
        return False

    def no_prohibited_pairs(self, word: str) -> bool:
        prohibited = ["ab", "cd", "pq", "xy"]
        for p in prohibited:
            if p in word:
                return False
        return True

    def pairs(self, word: str) -> Iterable[Tuple[str, str]]:
        for i in range(len(word) - 1):
            yield word[i], word[i + 1]

    @property
    def rules(self) -> Callable[[str], bool]:
        return [
            self.has_three_vowels,
            self.has_double_char,
            self.no_prohibited_pairs,
        ]


def solve(input: str) -> int:
    parser = Parser()
    solver = Day05PartASolver(parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
