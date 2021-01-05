"""Day 24 Advent of code 2020"""
from collections import defaultdict

DIRECTIONS = {
    "e": (0, 2),
    "w": (0, -2),
    "se": (-1, 1),
    "nw": (1, -1),
    "sw": (-1, -1),
    "ne": (1, 1)
}


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def parse_instructions(input_):
    instructions = []
    for row in input_:
        instructions.append(parse_single_instruction(row))
    return instructions


def parse_single_instruction(row):
    instruction = (0, 0)
    for direction in directions(row):
        instruction = tuple(sum(x) for x in zip(instruction, direction))
    return instruction


def directions(row):
    direction = ""
    for char in row:
        direction += char
        if direction in DIRECTIONS:
            yield DIRECTIONS[direction]
            direction = ""


def tile_flip_counts(instructions):
    flip_counts = defaultdict(int)
    for tile in instructions:
        flip_counts[tile] += 1
    return flip_counts


def flipped_tiles(flip_counts):
    return sum([x for x in flip_counts.values() if x % 2 == 1])


if __name__ == '__main__':
    INPUT = read_input()
    INSTRUCTIONS = parse_instructions(INPUT)
    FLIPPED_TILES = flipped_tiles(tile_flip_counts(INSTRUCTIONS))
    print(f"Black tiles after executing instructions {FLIPPED_TILES}")
    assert(FLIPPED_TILES == 228)
