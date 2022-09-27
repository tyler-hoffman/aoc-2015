from dataclasses import dataclass, field
from functools import cached_property
from math import prod
from typing import Iterable, Optional


@dataclass
class SubsetGetter:
    values: set[int]
    target: int
    max_needed: Optional[int] = field(init=False, default=None)

    @cached_property
    def values_as_list(self) -> list[int]:
        return sorted(list(self.values), reverse=True)

    @cached_property
    def values_for_target(self) -> set[frozenset[int]]:
        return set(self._get_values_for_target(index=0, so_far=set()))

    def _get_values_for_target(
        self,
        index: int,
        so_far: set[int],
    ) -> Iterable[frozenset[int]]:
        global max_needed
        if self.max_needed is not None and len(so_far) > self.max_needed:
            return
        elif index < len(self.values_as_list):
            value = self.values_as_list[index]
            yield from self._get_values_for_target(index + 1, so_far)
            so_far.add(value)
            the_sum = sum(so_far)
            length = len(so_far)
            if the_sum == self.target:
                if self.max_needed is None or length < self.max_needed:
                    self.max_needed = length
                yield frozenset(so_far)
            elif the_sum < self.target:
                yield from self._get_values_for_target(index + 1, so_far)
            so_far.remove(value)


@dataclass
class Day24Solver:
    values: set[int]
    compartment_count: int

    @property
    def solution(self) -> int:
        best: Optional[int] = None
        for values in self.passenger_compartment_variations:
            if len(values) == self.shortest_length_for_passenger_compartment:
                the_sum = prod(values)
                if best is None or the_sum < best:
                    best = the_sum
        assert best is not None
        return best

    @cached_property
    def per_compartment(self) -> int:
        the_sum = sum(self.values)
        assert the_sum % self.compartment_count == 0
        return the_sum // self.compartment_count

    @cached_property
    def passenger_compartment_variations(self) -> set[frozenset[int]]:
        subset_getter = SubsetGetter(self.values, self.per_compartment)
        return set(subset_getter.values_for_target)

    @cached_property
    def shortest_length_for_passenger_compartment(self) -> int:
        return min(len(s) for s in self.passenger_compartment_variations)
