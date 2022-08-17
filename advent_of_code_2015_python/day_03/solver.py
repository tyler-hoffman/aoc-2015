from abc import ABC, abstractmethod
from functools import cached_property
from typing import Sequence

from advent_of_code_2015_python.shared.models import DOWN, LEFT, RIGHT, UP, Point


class Solver(ABC):
    input: str

    @abstractmethod
    def do_move(self, move: Point) -> None:
        ...

    @property
    def solution(self) -> int:
        for move in self.moves:
            self.do_move(move)

        return len(self.visited)

    @cached_property
    def moves(self) -> Sequence[Point]:
        return [self.character_to_point(char) for char in self.input]

    @cached_property
    def visited(self) -> set[Point]:
        return set([Point()])

    @staticmethod
    def character_to_point(char: str) -> Point:
        match char:
            case "<":
                return LEFT
            case ">":
                return RIGHT
            case "^":
                return UP
            case "v":
                return DOWN
            case _:
                raise Exception(f"Unknown direction: {char}")
