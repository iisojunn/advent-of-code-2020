"""Day 20 Advent of code"""
import math
import numpy

from itertools import product


class Tile:

    def __init__(self, id_, rows):
        self.id = int(id_)
        self.data = [list(row) for row in rows]
        self.upside = "".join(self.data[0])
        self.downside = "".join(self.data[-1])
        self.left_side = "".join([row[0] for row in self.data])
        self.right_side = "".join([row[-1] for row in self.data])
        self.matches = set()

    def __repr__(self):
        return f"<Tile {self.id}>"

    def __str__(self):
        data = "\n".join("".join(row)for row in self.data)
        return f'Tile {self.id}:\n{data}\n'

    def transpose(self):
        self.upside, self.left_side = self.left_side, self.upside
        self.right_side, self.downside = self.downside, self.right_side

    def rotate(self):
        self.upside, self.right_side, self.downside, self.left_side = \
            self.right_side, "".join(reversed(self.downside)), \
            self.left_side, "".join(reversed(self.upside))

    def sides(self):
        return self.upside, self.right_side, self.downside, self.left_side

    def reversed_sides(self):
        return tuple("".join(reversed(side)) for side in self.sides())

    def all_sides(self):
        return *self.sides(), *self.reversed_sides()


def read_input():
    with open("input", "r") as input_file:
        return [parse_tile(tile) for tile in input_file.read().split("\n\n")]


def parse_tile(tile):
    tile_data = tile.splitlines()
    tile_id = tile_data[0].replace("Tile ", "").replace(":", "")
    return Tile(tile_id, tile_data[1:])


def spots_for_tile(image, new_tile, neighbour_required):
    for spot in possible_spots(image, neighbour_required):
        for _transpose in range(2):
            for _rotation in range(4):
                if is_suitable_spot(spot, new_tile, image):
                    yield spot, new_tile
                new_tile.rotate()
            new_tile.transpose()


def possible_spots(image, neighbour_required):
    for spot, tile in image.items():
        if tile is None:
            if not neighbour_required or has_neighbour(image, spot):
                yield spot


def has_neighbour(image, spot):
    x, y = spot
    for x0, y0 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        try:
            neighbour = image[(x0, y0)]
        except KeyError:
            pass
        else:
            if neighbour is not None:
                return True
    return False


def is_suitable_spot(spot, new_tile, image):
    matching_sides = [is_suitable_side(new_tile, side, neighbour_pixels) for
                      side, neighbour_pixels in sides_to_compare(image, spot)]
    return all(matching_sides)


def is_suitable_side(tile, side, neighbour_pixels):
    return getattr(tile, side) == neighbour_pixels


def sides_to_compare(image, spot):
    x, y = spot
    for my_side, neighbour_side, x0, y0 in adjacent(x, y):
        try:
            neighbour = image[(x0, y0)]
        except KeyError:
            pass
        else:
            if neighbour is not None:
                yield my_side, getattr(neighbour, neighbour_side)


def adjacent(x, y):
    yield "left_side", "right_side", x - 1, y
    yield "right_side", "left_side", x + 1, y
    yield "upside", "downside", x, y - 1
    yield "downside", "upside", x, y + 1


def base_image(tiles):
    return {(x, y): None for x, y in
            product(range(int(numpy.math.sqrt(tiles))), repeat=2)}


def is_filled(image):
    return all(tile is not None for tile in image.values())


def place_tiles(image, tiles, neighbour_required=False):
    check = [i for i, tile in enumerate(tiles) if tile not in image.values()]
    while check:
        tile = tiles[check.pop()]
        for spot, tile0 in spots_for_tile(image, tile, neighbour_required):
            image[spot] = tile0
            image = place_tiles(image, tiles, True)
            if is_filled(image):
                return image
            image[spot] = None
    return image


def search_matches(tiles):
    for tile in tiles:
        for other in tiles:
            if tile.id != other.id:
                for side in tile.all_sides():
                    if side in other.all_sides():
                        tile.matches.add(other)


def search_corners(tiles):
    return [tile for tile in tiles if len(tile.matches) == 2]


if __name__ == '__main__':
    TILES = read_input()
    print(TILES)
    search_matches(TILES)
    corner_tiles = search_corners(TILES)
    result = math.prod([tile.id for tile in corner_tiles])
    print(f"Corner tiles multiplied is {result}")
