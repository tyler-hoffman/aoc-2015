from dataclasses import dataclass
from typing import Callable, Iterable, Mapping, Sequence, Tuple
from advent_of_code_2015_python.day_05.parser import Parser


@dataclass
class Day05PartBSolver:
    strings: Sequence[str]

    @property
    def solution(self) -> int:
        nice_words = [word for word in self.strings if self.is_nice(word)]
        return len(nice_words)

    def is_nice(self, word: str) -> bool:
        return all((rule(word) for rule in self.rules))

    def has_sandwhich(self, word: str) -> bool:
        for a, _, b in self.triples(word):
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

        for i, double in enumerate(self.doubles(word)):
            if double not in output:
                output[double] = []
            output[double].append(i)

        return output

    def doubles(self, word: str) -> Iterable[Tuple[str, str]]:
        for i in range(len(word) - 1):
            yield word[i], word[i + 1]

    def triples(self, word: str) -> Iterable[Tuple[str, str, str]]:
        for i in range(len(word) - 2):
            yield word[i], word[i + 1], word[i + 2]

    @property
    def rules(self) -> Callable[[str], bool]:
        return [
            self.has_sandwhich,
            self.has_non_overlapping_matching_double_chard,
        ]


def solve(input: str) -> int:
    parser = Parser()
    solver = Day05PartBSolver(parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
