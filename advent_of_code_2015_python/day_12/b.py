from dataclasses import dataclass
from typing import Union

from advent_of_code_2015_python.day_12.parser import Parser


@dataclass
class Day12PartBSolver:
    data: Union[dict, list]

    @property
    def solution(self) -> int:
        return self.count_thing(self.data)

    def count_thing(self, thing: Union[list, dict, int]) -> int:
        match thing:
            case int() as my_int:
                return my_int
            case str():
                return 0
            case list() as my_list:
                return self.count_list(my_list)
            case dict() as my_dict:
                return self.count_dict(my_dict)

    def count_list(self, thing: list) -> int:
        return sum([self.count_thing(x) for x in thing])

    def count_dict(self, thing: dict) -> int:
        vals = thing.values()
        if "red" in vals:
            return 0
        else:
            return sum([self.count_thing(x) for x in vals])


def solve(input: str) -> int:
    data = Parser.parse_json(input)
    solver = Day12PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_12/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
