from typing import Iterable, Mapping

from advent_of_code_2015_python.day_15.parser import Parser
from advent_of_code_2015_python.day_15.shared import Day15Solver, Ingredient, Recipe

TOTAL_CALORIES = 500


def build_recipes(
    so_far: Mapping[Ingredient, int],
    ingredients_left: list[Ingredient],
    amount_left: int,
) -> Iterable[Mapping[Ingredient, int]]:
    calories_so_far = count_calories(so_far)
    ingredient = ingredients_left[0]
    if len(ingredients_left) == 1:
        if amount_left * ingredient.calories + calories_so_far == TOTAL_CALORIES:
            yield so_far | {ingredient: amount_left}
    else:
        for count in range(amount_left + 1):
            if count * ingredient.calories + calories_so_far > TOTAL_CALORIES:
                break
            yield from build_recipes(
                so_far={ingredient: count} | so_far,
                ingredients_left=ingredients_left[1:],
                amount_left=amount_left - count,
            )


def count_calories(recipe: Recipe) -> int:
    return sum([ingredient.calories * count for ingredient, count in recipe.items()])


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day15Solver(
        data=data,
        build_recipes=build_recipes,
    )

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_15/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
