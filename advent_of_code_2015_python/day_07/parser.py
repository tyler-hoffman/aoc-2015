from typing import Sequence, Union

from advent_of_code_2015_python.day_07.shared import (
    BinaryGate,
    BinaryGateType,
    LogicGate,
    UnaryGate,
    UnaryGateType,
)


class Parser(object):
    @staticmethod
    def parse(input: str) -> Sequence[LogicGate]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> LogicGate:
        fields = line.split()
        match fields:
            case a, "->", b:
                return UnaryGate(
                    UnaryGateType.ASSIGN, wire=b, value=Parser.parse_value(a)
                )
            case "NOT", a, "->", b:
                return UnaryGate(UnaryGateType.NOT, wire=b, value=Parser.parse_value(a))
            case a, "AND", b, "->", c:
                return BinaryGate(
                    BinaryGateType.AND,
                    wire=c,
                    a=Parser.parse_value(a),
                    b=Parser.parse_value(b),
                )
            case a, "OR", b, "->", c:
                return BinaryGate(
                    BinaryGateType.OR,
                    wire=c,
                    a=Parser.parse_value(a),
                    b=Parser.parse_value(b),
                )
            case a, "LSHIFT", b, "->", c:
                return BinaryGate(
                    BinaryGateType.LSHIFT,
                    wire=c,
                    a=Parser.parse_value(a),
                    b=Parser.parse_value(b),
                )
            case a, "RSHIFT", b, "->", c:
                return BinaryGate(
                    BinaryGateType.RSHIFT,
                    wire=c,
                    a=Parser.parse_value(a),
                    b=Parser.parse_value(b),
                )
            case _:
                raise Exception("Unhandled instruction: {line}")

    @staticmethod
    def parse_value(value: str) -> Union[str, int]:
        if value.isdigit():
            return int(value)
        else:
            return value
