from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence, Tuple


@dataclass
class Solver(ABC):
    boxes: Sequence[Box]

    @property
    def solution(self) -> int:
        return sum((self.compute_amount(box) for box in self.boxes))

    @abstractmethod
    def compute_amount(self, box: Box) -> int:
        ...


@dataclass
class Box:
    length: int
    width: int
    height: int

    @property
    def dimensions(self) -> Tuple[int, int, int]:
        return (self.length, self.width, self.height)
