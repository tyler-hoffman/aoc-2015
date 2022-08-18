from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Sequence


@dataclass
class Day17Solver:
    containers: Iterable[int]
    total_amount: int = 150

    @cached_property
    def combinations(self) -> Sequence[Sequence[int]]:
        return [x for x in self.get_combinations([], 0)]

    def get_combinations(
        self, so_far: list[int], container_index: int
    ) -> Iterable[Sequence[int]]:
        sum_so_far = sum(so_far)
        if sum_so_far == self.total_amount:
            yield list(so_far)
        elif (
            container_index < len(self.sorted_containers)
            and sum_so_far < self.total_amount
        ):
            # without
            yield from self.get_combinations(so_far, container_index + 1)

            # with
            so_far.append(self.sorted_containers[container_index])
            yield from self.get_combinations(so_far, container_index + 1)
            so_far.pop()

    @cached_property
    def sorted_containers(self) -> Sequence[int]:
        return sorted(self.containers)
