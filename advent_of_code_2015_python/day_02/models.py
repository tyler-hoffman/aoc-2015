from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Box:
    length: int
    width: int
    height: int

    @property
    def dimensions(self) -> Tuple[int, int, int]:
        return (self.length, self.width, self.height)
