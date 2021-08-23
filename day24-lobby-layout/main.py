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
    return [parse_single_instruction(row) for row in input_]


def parse_single_instruction(row):
    coordinates = (0, 0)
    for direction in directions(row):
        coordinates = tuple(sum(x) for x in zip(coordinates, direction))
    return coordinates


def directions(row):
    direction = ""
    for char in row:
        direction += char
        if direction in DIRECTIONS:
            yield DIRECTIONS[direction]
            direction = ""


def black_tiles(tile_coordinates):
    flip_counts = tile_flip_counts(tile_coordinates)
    return {tile for tile, count in flip_counts.items() if count % 2 == 1}


def tile_flip_counts(tile_coordinates):
    flip_counts = defaultdict(int)
    for tile in tile_coordinates:
        flip_counts[tile] += 1
    return flip_counts


def daily_flip(black_tiles_):
    to_flip = []
    whites_with_adj_black = defaultdict(int)

    for tile in black_tiles_:
        adj_blacks = len(adjacent_blacks(tile, black_tiles_))
        if adj_blacks == 0 or adj_blacks > 2:
            to_flip.append(tile)
        for adj_white in adjacent_whites(tile, black_tiles_):
            whites_with_adj_black[adj_white] += 1

    for white, adj_blacks in whites_with_adj_black.items():
        if adj_blacks == 2:
            to_flip.append(white)

    return black_tiles(list(black_tiles_) + to_flip)


def adjacent_blacks(tile, black_tiles_):
    return [x for x in adjacents(tile) if x in black_tiles_]


def adjacents(tile):
    for direction in DIRECTIONS.values():
        yield tuple(sum(x) for x in zip(tile, direction))


def adjacent_whites(tile, black_tiles_):
    return [x for x in adjacents(tile) if x not in black_tiles_]


if __name__ == '__main__':
    INPUT = read_input()
    TILE_COORDINATES = parse_instructions(INPUT)
    BLACK_TILES = black_tiles(TILE_COORDINATES)
    print(f"Black tiles after executing instructions {len(BLACK_TILES)}")
    assert(len(BLACK_TILES) == 228)

    for _ in range(1, 101):
        BLACK_TILES = daily_flip(BLACK_TILES)
    print(f"Black tiles after 100 days {len(BLACK_TILES)}")
    assert(len(BLACK_TILES) == 3672)
