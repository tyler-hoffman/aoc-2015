from dataclasses import dataclass

from advent_of_code_2015_python.day_19.parser import Parser
from advent_of_code_2015_python.day_19.shared import StrReplacement


@dataclass
class Day19PartASolver:
    molecule: str
    replacements: set[StrReplacement]

    @property
    def solution(self) -> int:
        new_words: set[str] = set()
        for replacement in self.replacements:
            for i in self.find_occurrences(replacement.original):
                new_words.add(
                    self.molecule[:i]
                    + replacement.replacement
                    + self.molecule[i + len(replacement.original) :]
                )
        return len(new_words)

    def find_occurrences(self, word: str) -> set[int]:
        output: set[int] = set()
        index = 0
        while index < len(self.molecule):
            next_index = self.molecule.find(word, index)
            if next_index < 0:
                break
            else:
                output.add(next_index)
                index = next_index + 1
        return output


def solve(input: str) -> int:
    molecule, replacements = Parser.parse(input)
    solver = Day19PartASolver(molecule, replacements)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_19/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
