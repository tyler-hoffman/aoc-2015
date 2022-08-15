from dataclasses import dataclass
from functools import cache, cached_property
from typing import Mapping, Sequence, Union

from advent_of_code_2015_python.day_07.parser import Parser
from advent_of_code_2015_python.day_07.shared import (
    BinaryGate,
    BinaryGateType,
    LogicGate,
    UnaryGate,
    UnaryGateType,
)

SIXTEEN_BITS = 65535


@dataclass(frozen=True)
class Day07PartASolver:
    gates: tuple[LogicGate, ...]

    @property
    def solution(self) -> int:
        return self.get_value("a")

    @cache
    def get_value(self, value: Union[str, int]) -> int:
        if isinstance(value, int):
            return value
        else:
            match self.wires_by_name[value]:
                case UnaryGate(UnaryGateType.ASSIGN, value=x):
                    return self.get_value(x)
                case UnaryGate(UnaryGateType.NOT, value=x):
                    return (~self.get_value(x)) & SIXTEEN_BITS
                case BinaryGate(BinaryGateType.AND, a=a, b=b):
                    return self.get_value(a) & self.get_value(b)
                case BinaryGate(BinaryGateType.OR, a=a, b=b):
                    return self.get_value(a) | self.get_value(b)
                case BinaryGate(BinaryGateType.LSHIFT, a=a, b=b):
                    return (self.get_value(a) << self.get_value(b)) & SIXTEEN_BITS
                case BinaryGate(BinaryGateType.RSHIFT, a=a, b=b):
                    return (self.get_value(a) >> self.get_value(b)) & SIXTEEN_BITS
                case _:
                    raise Exception("How'd we get here??")

    @cached_property
    def wires_by_name(self) -> Mapping[str, LogicGate]:
        output: dict[str, LogicGate] = dict()
        for gate in self.gates:
            output[gate.wire] = gate
        return output


def solve(input: str) -> int:
    parser = Parser()
    gates = tuple(parser.parse(input))
    solver = Day07PartASolver(gates)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_07/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
