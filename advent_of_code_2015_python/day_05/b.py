from dataclasses import dataclass
from typing import Callable, Iterable, Mapping, Sequence, Tuple

from advent_of_code_2015_python.day_05.parser import Parser
from advent_of_code_2015_python.day_05.solver import Solver, sliding_window


@dataclass
class Day05PartBSolver(Solver):
    strings: Sequence[str]

    @property
    def rules(self) -> Iterable[Callable[[str], bool]]:
        return [
            self.has_sandwhich,
            self.has_non_overlapping_matching_double_chard,
        ]

    def has_sandwhich(self, word: str) -> bool:
        for a, _, b in sliding_window(word, 3):
            if a == b:
                return True
        return False

    def has_non_overlapping_matching_double_chard(self, word: str) -> bool:
        for index_list in self.pairs_to_indicies(word).values():
            first_index = index_list[0]
            length = len(index_list)
            if length > 2 or length > 1 and index_list[1] > first_index + 1:
                return True
        return False

    def pairs_to_indicies(self, word: str) -> Mapping[Tuple[str, str], list[int]]:
        output: dict[Tuple[str, str], list[int]] = dict()

        for i, (a, b) in enumerate(sliding_window(word, 2)):
            key = (a, b)
            if key not in output:
                output[key] = []
            output[key].append(i)

        return output


def solve(input: str) -> int:
    solver = Day05PartBSolver(Parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
