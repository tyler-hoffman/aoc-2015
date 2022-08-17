from dataclasses import dataclass
from typing import Callable, Iterable, Mapping, Sequence


@dataclass(frozen=True)
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


TEASPOON_COUNT = 100

Recipe = Mapping[Ingredient, int]


@dataclass(frozen=True)
class Day15Solver:
    data: Sequence[Ingredient]
    build_recipes: Callable[[Recipe, list[Ingredient], int], Iterable[Recipe]]

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
        yield from self.build_recipes({}, list(self.data), TEASPOON_COUNT)
