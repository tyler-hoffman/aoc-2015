def create_part_stub(day_string: str, part: str) -> str:
    src = "advent_of_code_2015_python"
    return _PART_TEMPLATE.format(
        day_string=day_string,
        part_upper=part.upper(),
        src=src,
    )


_PART_TEMPLATE = """
from {src}.day_{day_string}.parser import Parser


class Day{day_string}Part{part_upper}Solver:
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day{day_string}Part{part_upper}Solver(parser.parse(input))

    return solver.solution

def get_solution() -> int:
    with open("advent_of_code_2015_python/day_{day_string}/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

"""
