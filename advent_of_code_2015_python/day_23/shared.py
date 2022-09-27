from dataclasses import dataclass, field
from enum import Enum


class Register(Enum):
    A = "A"
    B = "B"


@dataclass(frozen=True)
class Instruction:
    ...


@dataclass(frozen=True)
class Half(Instruction):
    register: Register


@dataclass(frozen=True)
class Triple(Instruction):
    register: Register


@dataclass(frozen=True)
class Increment(Instruction):
    register: Register


@dataclass(frozen=True)
class Jump(Instruction):
    amount: int


@dataclass(frozen=True)
class JumpIfEven(Instruction):
    register: Register
    amount: int


@dataclass(frozen=True)
class JumpIfOne(Instruction):
    register: Register
    amount: int


@dataclass
class Computer:
    instructions: list[Instruction]
    registers: dict[Register, int] = field(
        default_factory=lambda: {r: 0 for r in {Register.A, Register.B}}
    )
    index: int = field(init=False, default=0)

    def run(self) -> None:
        while self.index < len(self.instructions):
            self.do_instruction()

    def do_instruction(self) -> None:
        match self.instructions[self.index]:
            case Half(register):
                assert self.registers[register] % 2 == 0
                self.registers[register] //= 2
            case Triple(register):
                self.registers[register] *= 3
            case Increment(register):
                self.registers[register] += 1
            case Jump(offset):
                self.index += offset - 1
            case JumpIfEven(register, offset):
                if self.registers[register] % 2 == 0:
                    self.index += offset - 1
            case JumpIfOne(register, offset):
                if self.registers[register] == 1:
                    self.index += offset - 1
            case _:
                raise Exception("Invalid instruction")
        self.index += 1
