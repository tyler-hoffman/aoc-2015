from advent_of_code_2015_python.day_23.shared import (
    Half,
    Increment,
    Instruction,
    Jump,
    JumpIfEven,
    JumpIfOne,
    Register,
    Triple,
)


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Instruction]:
        lines = input.strip().replace(",", "").splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Instruction:
        parts = line.split()
        cmd_label = parts[0]
        match cmd_label:
            case "hlf":
                return Half(Parser.parse_register(parts[1]))
            case "tpl":
                return Triple(Parser.parse_register(parts[1]))
            case "inc":
                return Increment(Parser.parse_register(parts[1]))
            case "jmp":
                return Jump(int(parts[1]))
            case "jie":
                return JumpIfEven(Parser.parse_register(parts[1]), int(parts[2]))
            case "jio":
                return JumpIfOne(Parser.parse_register(parts[1]), int(parts[2]))
            case _:
                raise Exception(f"Invalid command: {cmd_label}")

    @staticmethod
    def parse_register(char: str) -> Register:
        match char:
            case "a":
                return Register.A
            case "b":
                return Register.B
            case _:
                raise Exception(f"Invalid register: {char}")
