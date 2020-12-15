"""Day 11 Advent of code"""
from itertools import chain

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


def read_input(filename):
    with open(filename, "r") as input_file:
        return [list(row) for row in input_file.read().splitlines()]


def apply_rules(layout):
    new_layout = []
    for y, row in enumerate(layout):
        new_layout.append([])
        for x in range(len(row)):
            new_layout[y].append(new_status(layout, x, y))
    return new_layout


def new_status(layout, x, y):
    spot = layout[y][x]
    if is_floor(spot):
        return FLOOR
    adjacents = adjacent_spots(layout, x, y)
    if is_empty(spot) and OCCUPIED not in adjacents:
        return OCCUPIED
    if is_occupied(spot) and is_congested(adjacents):
        return EMPTY
    return spot


def adjacent_spots(layout, x, y):
    adjacents = []
    height = len(layout)
    width = len(layout[0])
    for x0 in range(max(0, x - 1), min(x + 1, width) + 1):
        for y0 in range(max(0, y - 1), min(y + 1, height) + 1):
            try:
                if not (x0 == x and y0 == y):
                    adjacents.append(layout[y0][x0])
            except IndexError:
                continue
    return adjacents


def is_congested(adjacents):
    return adjacents.count(OCCUPIED) >= 4


def is_occupied(spot):
    return spot == OCCUPIED


def is_floor(spot):
    return spot == FLOOR


def is_empty(spot):
    return spot == EMPTY


def seats_changed(new_layout, layout):
    return any([new_spot != current_spot for new_spot, current_spot
                in zip(chain(*new_layout), chain(*layout))])


def apply_rules_until_settled(layout):
    while True:
        new_layout = apply_rules(layout)
        if not seats_changed(new_layout, layout):
            return layout
        layout = new_layout


def count_occupied(layout):
    return [spot for spot in chain(*layout)].count(OCCUPIED)


if __name__ == '__main__':
    seat_layout = read_input("input")
    print(seat_layout)
    final_layout = apply_rules_until_settled(seat_layout)
    print(final_layout)
    occupied = count_occupied(final_layout)
    print(f"Occupied seats after people settle down {occupied}")
