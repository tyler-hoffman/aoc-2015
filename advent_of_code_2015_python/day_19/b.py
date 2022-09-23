from dataclasses import dataclass
from functools import cache, cached_property
from typing import Optional

from advent_of_code_2015_python.day_19.parser import Parser
from advent_of_code_2015_python.day_19.shared import Replacement, StrReplacement


@dataclass(frozen=True)
class TokenReplacement(Replacement[str, tuple[str, ...]]):
    ...


@dataclass(frozen=True)
class Mutation:
    steps: int
    value: tuple[int, ...]


@dataclass(frozen=True)
class SolvedPortion:
    target_left: int
    target_right: int
    steps: int


@dataclass(frozen=True)
class Day19PartBSolver:
    """Solver for Day 19 pt. b

    Notes on the approach:
    There is a case where a given production (e.g. `A -> AB`) can
    result in a sort of infinite production (ABBBB...).

    If you imagine the applying productions to different parts of
    a sequence of tokens as creating a tree, we can prevent
    the infinite productions by capping it at a max depth.
    However, I don't know how to figure out what that max depth
    should be, so we're just starting arbitrarily small
    and increasing it until we find the solution.
    The results seem much better doing this than when
    I arbitrarily guessed a max depth.
    """

    molecule: str
    replacements: frozenset[StrReplacement]

    @property
    def solution(self) -> int:
        max_depth = 0
        while True:
            if output := self.solve_with_max_depth(max_depth):
                return output
            else:
                max_depth += 1

    def solve_with_max_depth(self, max_depth: int) -> Optional[int]:
        minimum_steps: Optional[int] = None
        for portion in self.expand_tokens(self.start_tokens, 0, max_depth):
            completed = portion.target_right == self.target_len
            should_update = minimum_steps is None or portion.steps < minimum_steps
            if completed and should_update:
                minimum_steps = portion.steps
        return minimum_steps

    @cache
    def expand_token(
        self, token: str, target_left: int, remaining_depth: int
    ) -> set[SolvedPortion]:
        if target_left >= self.target_len:
            return set()

        output: set[SolvedPortion] = set()

        # if we already have the right token in place we can consider just skipping it
        if token == self.target_tokens[target_left]:
            output.add(
                SolvedPortion(
                    target_left=target_left,
                    target_right=target_left + 1,
                    steps=0,
                )
            )

        # also check all possible replacements
        for tr in self.token_replacements_by_origin[token]:
            for solved_portion in self.expand_tokens(
                tr.replacement, target_left, remaining_depth - 1
            ):
                output.add(
                    SolvedPortion(
                        target_left=target_left,
                        target_right=solved_portion.target_right,
                        steps=1 + solved_portion.steps,
                    )
                )

        return output

    @cache
    def expand_tokens(
        self, tokens: tuple[str, ...], target_left: int, remaining_depth: int
    ) -> set[SolvedPortion]:
        if remaining_depth <= 0:
            return set()

        head = tokens[0]
        tail = tokens[1:]
        start_expansions = self.expand_token(head, target_left, remaining_depth)

        if not tail:
            return start_expansions
        else:
            output: set[SolvedPortion] = set()
            for p in start_expansions:
                for q in self.expand_tokens(tail, p.target_right, remaining_depth):
                    output.add(
                        SolvedPortion(
                            target_left=target_left,
                            target_right=q.target_right,
                            steps=p.steps + q.steps,
                        )
                    )
            return output

    @cached_property
    def start_tokens(self) -> tuple[str, ...]:
        return self.str_to_tokens("e")

    @cached_property
    def target_tokens(self) -> tuple[str, ...]:
        return self.str_to_tokens(self.molecule)

    @cached_property
    def target_len(self) -> int:
        return len(self.target_tokens)

    @cached_property
    def token_replacements_by_origin(self) -> dict[str, set[TokenReplacement]]:
        output: dict[str, set[TokenReplacement]] = {t: set() for t in self.all_tokens}
        for r in self.token_replacements:
            output[r.original].add(r)
        return output

    @cached_property
    def token_replacements(self) -> set[TokenReplacement]:
        return {
            TokenReplacement(
                self.str_to_tokens(r.original)[0],
                self.str_to_tokens(r.replacement),
            )
            for r in self.replacements
        }

    @cached_property
    def all_tokens(self) -> set[str]:
        output: set[str] = set()
        for r in self.replacements:
            output.update(self.str_to_tokens(r.original))
            output.update(self.str_to_tokens(r.replacement))
        return output

    def str_to_tokens(self, word: str) -> tuple[str, ...]:
        output: list[str] = []
        current: Optional[str] = None
        for ch in word:
            if ch == "e":
                output.append(ch)
            elif ch.islower():
                assert current is not None
                current += ch
            else:
                if current:
                    output.append(current)
                current = ch
        if current:
            output.append(current)
        return tuple(output)


def solve(input: str) -> int:
    molecule, replacements = Parser.parse(input)
    solver = Day19PartBSolver(molecule, frozenset(replacements))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_19/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
