from dataclasses import dataclass
from enum import Enum
from typing import Union


class UnaryGateType(Enum):
    ASSIGN = 1
    NOT = 2


@dataclass(frozen=True)
class UnaryGate:
    gate_type: UnaryGateType
    wire: str
    value: Union[int, str]


class BinaryGateType(Enum):
    OR = 1
    AND = 2
    LSHIFT = 3
    RSHIFT = 4


@dataclass(frozen=True)
class BinaryGate:
    gate_type: BinaryGateType
    wire: str
    a: Union[int, str]
    b: Union[int, str]


LogicGate = Union[UnaryGate, BinaryGate]
