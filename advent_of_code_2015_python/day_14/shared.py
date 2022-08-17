from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True)
class Reindeer:
    name: str
    km_per_s: int
    fly_time: int
    rest_time: int

    @cached_property
    def cycle_time(self) -> int:
        return self.fly_time + self.rest_time

    @cached_property
    def km_per_cycle(self) -> int:
        return self.fly_time * self.km_per_s
