import itertools
from dataclasses import dataclass
from functools import cached_property
from typing import Mapping


@dataclass
class Day13Solver:
    data: Mapping[tuple[str, str], int]

    @property
    def solution(self) -> int:
        best_happiness = 0
        for names in itertools.permutations(self.all_names):
            best_happiness = max(best_happiness, self.compute_happiness(names))
        return best_happiness

    def compute_happiness(self, names: tuple[str, ...]) -> int:
        output = 0
        for i, name in enumerate(names):
            output += self.data[(name, names[(i - 1) % len(names)])]
            output += self.data[(name, names[(i + 1) % len(names)])]
        return output

    @cached_property
    def all_names(self) -> frozenset[str]:
        names = {a for a, b in self.data.keys()}
        return frozenset(names)
