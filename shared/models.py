from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def add(self, p: Point) -> Point:
        return Point(x=self.x + p.x, y=self.y + p.y)


LEFT = Point(x=-1)
RIGHT = Point(x=1)
UP = Point(y=1)
DOWN = Point(y=-1)
