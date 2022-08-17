from __future__ import annotations

import string
from dataclasses import dataclass
from functools import cached_property
from typing import Mapping, Optional, Sequence

from advent_of_code_2015_python.shared.functions import sliding_window

LETTER_TO_INDEX_MAP: Mapping[str, int] = {
    char: index for index, char in enumerate(string.ascii_lowercase)
}
INDEX_TO_LETTER_MAP: Mapping[int, str] = {
    index: char for char, index in LETTER_TO_INDEX_MAP.items()
}


@dataclass(frozen=True)
class Password:
    value: str

    def next(self) -> Password:
        password = self.increment()
        while not password.is_valid:
            index_to_increment: Optional[int] = None
            if password.has_prohibited_chars:
                index_to_increment = password.prohibited_char_indexes[-1]
            password = password.increment(index_to_increment)
        return password

    def increment(self, first_index: int = None) -> Password:
        if first_index is None:
            first_index = len(self.value) - 1
        output_chars: list[str] = ["a" for _ in self.value]
        keep_incrementing = True
        for i in range(first_index, -1, -1):
            if keep_incrementing:
                current_index = LETTER_TO_INDEX_MAP[self.value[i]]
                next_index = current_index + 1
                if next_index == 26:
                    output_chars[i] = "a"
                else:
                    output_chars[i] = INDEX_TO_LETTER_MAP[next_index]
                    keep_incrementing = False
            else:
                output_chars[i] = self.value[i]
        return Password("".join(output_chars))

    @cached_property
    def is_valid(self) -> bool:
        return (
            self.has_run
            and self.has_non_overlapping_pair
            and not self.has_prohibited_chars
        )

    @cached_property
    def has_run(self) -> bool:
        ints = self.as_ints
        for i in range(len(self.value) - 2):
            a, b, c = [ints[i + j] for j in [0, 1, 2]]
            if b == a + 1 and c == b + 1:
                return True
        return False

    @cached_property
    def has_non_overlapping_pair(self) -> bool:
        pair_indexes: list[int] = []
        for i, (a, b) in enumerate(sliding_window(self.value, 2)):
            if a == b:
                pair_indexes.append(i)

        length = len(pair_indexes)
        return length > 2 or length > 1 and pair_indexes[1] > pair_indexes[0] + 1

    @cached_property
    def has_prohibited_chars(self) -> bool:
        return bool(self.prohibited_char_indexes)

    @cached_property
    def prohibited_char_indexes(self) -> Sequence[int]:
        output: list[int] = []
        for i, char in enumerate(self.value):
            if char in self.prohibited_chars:
                output.append(i)
        return output

    @cached_property
    def prohibited_chars(self) -> frozenset[str]:
        return frozenset(["i", "o", "l"])

    @cached_property
    def contains_run(self) -> frozenset[str]:
        return frozenset(["i", "o", "l"])

    @cached_property
    def as_ints(self) -> Sequence[int]:
        return [LETTER_TO_INDEX_MAP[char] for char in self.value]
