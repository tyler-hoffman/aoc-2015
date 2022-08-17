from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterable, Mapping, Sequence

from advent_of_code_2015_python.day_15.parser import Parser
from advent_of_code_2015_python.day_15.shared import Ingredient


@dataclass(frozen=True)
class Day15PartASolver:
    data: Sequence[Ingredient]
    teaspoons: int = 100

    @property
    def solution(self) -> int:
        best_so_far = 0
        for recipe in self.get_recipes():
            recipe_score = self.compute_score(recipe)
            best_so_far = max(best_so_far, recipe_score)

        return best_so_far

    def compute_score(self, recipe: Mapping[Ingredient, int]) -> int:
        capacity = 0
        durability = 0
        texture = 0
        flavor = 0

        for ingredient, count in recipe.items():
            capacity += ingredient.capacity * count
            durability += ingredient.durability * count
            texture += ingredient.texture * count
            flavor += ingredient.flavor * count
        capacity = max(0, capacity)
        durability = max(0, durability)
        texture = max(0, texture)
        flavor = max(0, flavor)

        return capacity * durability * texture * flavor

    def get_recipes(self) -> Iterable[Mapping[Ingredient, int]]:
        yield from self._get_ingredient_amounts({}, list(self.data), self.teaspoons)

    def _get_ingredient_amounts(
        self,
        so_far: Mapping[Ingredient, int],
        ingredients_left: list[Ingredient],
        amount_left: int,
    ) -> Iterable[Mapping[Ingredient, int]]:
        ingredient = ingredients_left[0]
        if len(ingredients_left) == 1:
            yield so_far | {ingredient: amount_left}
        else:
            for count in range(amount_left + 1):
                yield from self._get_ingredient_amounts(
                    so_far={ingredient: count} | so_far,
                    ingredients_left=ingredients_left[1:],
                    amount_left=amount_left - count,
                )


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day15PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("advent_of_code_2015_python/day_15/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
