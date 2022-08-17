from advent_of_code_2015_python.day_11.parser import Parser
from advent_of_code_2015_python.day_11.shared import Password


def solve(input: str) -> str:
    password = Password(Parser.parse(input))
    password = password.next()
    return password.value


def get_solution() -> str:
    with open("advent_of_code_2015_python/day_11/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
