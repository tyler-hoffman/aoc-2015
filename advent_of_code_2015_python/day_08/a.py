from advent_of_code_2015_python.day_08.parser import Parser


class Day08PartASolver:
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    solver = Day08PartASolver(Parser.parse(input))

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_08/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
