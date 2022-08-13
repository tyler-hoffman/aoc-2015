from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import Sequence, Tuple


@dataclass
class Solver(ABC):
    boxes: Sequence[Box]

@dataclass
class Box:
    length: int
    width: int
    height: int

    @property
    def dimensions(self) -> Tuple[int, int, int]:
        return (self.length, self.width, self.height)
