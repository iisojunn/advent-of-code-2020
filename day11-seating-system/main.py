"""Day 11 Advent of code"""
from itertools import chain, product

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


def read_input(filename):
    with open(filename, "r") as input_file:
        return [list(row) for row in input_file.read().splitlines()]


def apply_rules_until_settled(layout, adjacency_method, congestion_limit):
    while True:
        new_layout = apply_rules(layout, adjacency_method, congestion_limit)
        if not seats_changed(new_layout, layout):
            return layout
        layout = new_layout


def apply_rules(layout, adjacency_method, congestion_limit):
    new_layout = []
    for y, row in enumerate(layout):
        new_layout.append([])
        for x, spot in enumerate(row):
            adjacents = adjacency_method(layout, x, y)
            new_layout[y].append(new_status(spot, adjacents, congestion_limit))
    return new_layout


def new_status(spot, adjacents, congestion_limit):
    if is_floor(spot):
        return FLOOR
    if is_empty(spot) and OCCUPIED not in adjacents:
        return OCCUPIED
    if is_occupied(spot) and is_congested(adjacents, congestion_limit):
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


def is_congested(adjacents, limit):
    return adjacents.count(OCCUPIED) >= limit


def is_occupied(spot):
    return spot == OCCUPIED


def is_floor(spot):
    return spot == FLOOR


def is_empty(spot):
    return spot == EMPTY


def seats_changed(new_layout, layout):
    return any([new_spot != current_spot for new_spot, current_spot
                in zip(chain(*new_layout), chain(*layout))])


def count_occupied(layout):
    return [spot for spot in chain(*layout)].count(OCCUPIED)


def spots_in_direction(layout, x, y, direction):
    if direction == (0, 0):
        yield
    height = len(layout)
    width = len(layout[0])
    x_add, y_add = direction
    x += x_add
    y += y_add
    while 0 <= x < width and 0 <= y < height:
        yield layout[y][x]
        x += x_add
        y += y_add


def first_seat_status(consecutive_spots):
    for spot in consecutive_spots:
        if is_floor(spot):
            continue
        return spot


def visible_seats(layout, x, y):
    visible = []
    for direction in product((-1, 0, 1), (-1, 0, 1)):
        spots = spots_in_direction(layout, x, y, direction)
        visible.append(first_seat_status(spots))
    return visible


if __name__ == '__main__':
    seat_layout = read_input("input")

    final_layout = apply_rules_until_settled(seat_layout, adjacent_spots, 4)
    occupied = count_occupied(final_layout)
    print(f"Occupied seats after people settle down {occupied}")

    final_layout2 = apply_rules_until_settled(seat_layout, visible_seats, 5)
    occupied2 = count_occupied(final_layout2)
    print(f"Occupied seats with better vision and more tolerance {occupied2}")
