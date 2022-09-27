from dataclasses import dataclass

from advent_of_code_2015_python.day_23.parser import Parser
from advent_of_code_2015_python.day_23.shared import Computer, Instruction, Register


@dataclass
class Day23PartASolver:
    instructions: list[Instruction]
    target_register: Register = Register.B

    @property
    def solution(self) -> int:
        computer = Computer(self.instructions)
        computer.run()
        return computer.registers[self.target_register]


def solve(input: str, target_register: Register = Register.B) -> int:
    instructions = Parser.parse(input)
    solver = Day23PartASolver(instructions, target_register)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_23/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
