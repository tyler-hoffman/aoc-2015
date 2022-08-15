from dataclasses import dataclass
from enum import Enum


class InstructionType(Enum):
    ON = 1
    OFF = 2
    TOGGLE = 3


@dataclass
class Instruction:
    instruction_type: InstructionType
    start: tuple[int, int]
    end: tuple[int, int]
