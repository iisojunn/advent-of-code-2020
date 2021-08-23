"""Day 17 Advent of code"""
from collections import defaultdict
from itertools import chain, product

ACTIVE_MARK = "#"


def read_input():
    with open("input", "r") as input_file:
        return [list(row) for row in input_file.read().splitlines()]


def initialize_cubes(list2d, padding):
    active = set()
    for y, row in enumerate(list2d):
        for x, status in enumerate(row):
            if status == ACTIVE_MARK:
                active.add((x, y, *padding))
    return active


def neighbours_of(coordinates):
    return [
        tuple(dx + x for dx, x in zip(delta, coordinates))
        for delta in product([-1, 0, 1], repeat=len(coordinates))
        if any(d != 0 for d in delta)
    ]


def affected_neighbours(active):
    affected = defaultdict(int)
    neighbours = [neighbours_of(coordinates) for coordinates in active]
    for coordinates in chain(*neighbours):
        affected[coordinates] += 1
    return affected


def play_cycle(active):
    neighbours = affected_neighbours(active)
    return {
        cube
        for cube, amount in neighbours.items()
        if amount == 3 or (amount == 2 and cube in active)
    }


if __name__ == '__main__':
    ACTIVE = initialize_cubes(read_input(), (0,))
    for _ in range(6):
        ACTIVE = play_cycle(ACTIVE)
    print(f"Active cubes after 6 cycles {len(ACTIVE)}")

    ACTIVE = initialize_cubes(read_input(), (0, 0))
    for _ in range(6):
        ACTIVE = play_cycle(ACTIVE)
    print(f"Active hypercubes after 6 cycles {len(ACTIVE)}")
