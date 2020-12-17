"""Day 17 Advent of code"""
from collections import defaultdict
from itertools import chain

ACTIVE = "#"


def read_input():
    with open("input", "r") as input_file:
        return [list(row) for row in input_file.read().splitlines()]


def initialize_cubes(list2d):
    active = set()
    print(list2d)
    for y, row in enumerate(list2d):
        for x, status in enumerate(row):
            if status == ACTIVE:
                active.add((x, y, 0))
    return active


def neighbours_of(x, y, z):
    neighbours = []
    for x0 in [x - 1, x, x + 1]:
        for y0 in [y - 1, y, y + 1]:
            for z0 in [z - 1, z, z + 1]:
                if (x0 != x) or (y0 != y) or (z0 != z):
                    neighbours.append((x0, y0, z0))
    return neighbours


def affected_neighbours(active):
    affected = defaultdict(int)
    neighbours = [neighbours_of(x, y, z) for x, y, z in active]
    for coordinates in chain(*neighbours):
        affected[coordinates] += 1
    return affected


def play_cycle(active):
    active_after_cycle = set()
    neighbours = affected_neighbours(active)
    for cube, amount in neighbours.items():
        if amount == 3:
            active_after_cycle.add(cube)
        elif amount == 2 and cube in active:
            active_after_cycle.add(cube)
    return active_after_cycle


if __name__ == '__main__':
    ACTIVE = initialize_cubes(read_input())
    for i in range(6):
        ACTIVE = play_cycle(ACTIVE)

    print(f"Active cubes after 6 cycles {len(ACTIVE)}")
