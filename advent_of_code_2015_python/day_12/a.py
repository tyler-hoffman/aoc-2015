from advent_of_code_2015_python.day_12.parser import Parser


def solve(input: str) -> int:
    ints = Parser.parse_ints(input)
    return sum(ints)


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_12/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
