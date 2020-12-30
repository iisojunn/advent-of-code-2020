"""Day 21 Advent of code 2020"""
import re
from collections import defaultdict, OrderedDict
from itertools import chain

FOOD_REGEX = r"(?P<ingredients>.*) \(contains (?P<allergens>.*)\)$"


def parse_row(row):
    match = re.match(FOOD_REGEX, row)
    ingredients = match.group("ingredients").split(" ")
    allergens = match.group("allergens").split(", ")
    return ingredients, allergens


def read_input():
    with open("input", "r") as input_file:
        return [parse_row(row) for row in input_file.read().splitlines()]


def count_components(foods):
    counts = defaultdict(int)
    for ingredients, allergens in foods:
        for component in chain(ingredients, allergens):
            counts[component] += 1
    return counts


def separate_components(foods):
    all_ingredients = set()
    all_allergens = set()
    for ingredients, allergens in foods:
        for ingredient in ingredients:
            all_ingredients.add(ingredient)
        for allergen in allergens:
            all_allergens.add(allergen)
    return all_ingredients, all_allergens


def find_suspicious_ingredients(foods):
    suspicious = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if not suspicious.get(allergen):
                suspicious[allergen] = set(ingredients)
            else:
                suspicious[allergen] = suspicious[allergen].intersection(
                    set(ingredients))
    return suspicious


def allergen_free_ingredients(ingredients, suspicious):
    return [free for free in ingredients if
            free not in set(chain(*suspicious.values()))]


def resolve_dangerous(suspicious):
    dangerous = {}
    while len(dangerous) != len(suspicious):
        resolved_ingredients = set().union(*dangerous.values())
        for allergen, ingredients in suspicious.items():
            possible_ingredients = ingredients - resolved_ingredients
            if len(possible_ingredients) == 1:
                dangerous[allergen] = possible_ingredients
    for allergen, ingredient in dangerous.items():
        dangerous[allergen] = ingredient.pop()
    return dangerous


def canonical_dangerous_ingredient_list(dangerous):
    ordered = OrderedDict(sorted(dangerous.items(), key=lambda x: x[0]))
    return ",".join([allergen for allergen in ordered.values()])


if __name__ == '__main__':
    FOODS = read_input()
    COUNTS = count_components(FOODS)
    INGREDIENTS, ALLERGENS = separate_components(FOODS)
    SUSPICIOUS = find_suspicious_ingredients(FOODS)
    ALLERGEN_FREE = allergen_free_ingredients(INGREDIENTS, SUSPICIOUS)
    APPEARANCE = sum([COUNTS[ingredient] for ingredient in ALLERGEN_FREE])
    print(f"Allergen free ingredients appear {APPEARANCE} times")

    DANGEROUS = resolve_dangerous(SUSPICIOUS)
    CANONICAL = canonical_dangerous_ingredient_list(DANGEROUS)
    print(f"Canonical dangerous ingredient list {CANONICAL}")
