"""Day 20 Advent of code"""
import math
import re

import numpy
from itertools import product

LEFT = "left_side"
DOWN = "downside"
RIGHT = "right_side"
UP = "upside"

SIDES = {
    (0, -1): UP,
    (1, 0): RIGHT,
    (0, 1): DOWN,
    (-1, 0): LEFT,
}

OPPOSITES = {
    UP: DOWN,
    RIGHT: LEFT,
    DOWN: UP,
    LEFT: RIGHT
}

MONSTER = r"""..................#.
#....##....##....###
.#..#..#..#..#..#..."""


class Tile:

    def __init__(self, id_, rows):
        self.id = int(id_)
        self.data = numpy.array([list(row) for row in rows])
        self.matches = {}

    def __repr__(self):
        return f"<Tile {self.id}>"

    def __str__(self):
        return f'Tile {self.id}:\n{self.data_str()}\n'

    def data_str(self):
        return "\n".join("".join(row) for row in self.data)

    @property
    def upside(self):
        return "".join(self.data[0])

    @property
    def right_side(self):
        return "".join([row[-1] for row in self.data])

    @property
    def downside(self):
        return "".join(self.data[-1])

    @property
    def left_side(self):
        return "".join([row[0] for row in self.data])

    def flip(self):
        self.data = numpy.flipud(self.data)
        self.change_match_sides([(UP, DOWN),
                                 (RIGHT, RIGHT),
                                 (DOWN, UP),
                                 (LEFT, LEFT)])

    def rotate(self):
        self.data = numpy.rot90(self.data)
        self.change_match_sides([(UP, LEFT),
                                 (RIGHT, UP),
                                 (DOWN, RIGHT),
                                 (LEFT, DOWN)])

    def change_match_sides(self, sides):
        matches = self.matches.copy()
        self.matches = {}
        for side, new_side in sides:
            if matches.get(side):
                self.matches[new_side] = matches.get(side)

    def sides(self):
        return self.upside, self.right_side, self.downside, self.left_side

    def reversed_sides(self):
        return tuple("".join(reversed(side)) for side in self.sides())

    def all_sides(self):
        return *self.sides(), *self.reversed_sides()

    def check_matches(self, other):
        for side in [UP, DOWN, LEFT, RIGHT]:
            if getattr(self, side) in other.all_sides():
                self.matches[side] = other

    def flip_and_rotate_to_match(self, other, side):
        for _flip in range(2):
            for _rotation in range(4):
                if self.sides_match(other, side):
                    return
                self.rotate()
            self.flip()

    def sides_match(self, other, side):
        return getattr(self, side) == getattr(other, OPPOSITES[side])

    def image_data(self):
        return [row[1:-1] for row in self.data[1:-1]]


def read_input(filename):
    with open(filename, "r") as input_file:
        return [parse_tile(tile) for tile in input_file.read().split("\n\n")]


def parse_tile(tile):
    tile_data = tile.splitlines()
    tile_id = tile_data[0].replace("Tile ", "").replace(":", "")
    return Tile(tile_id, tile_data[1:])


def search_matches(tiles):
    for tile, other in product(tiles, repeat=2):
        if tile.id != other.id:
            tile.check_matches(other)


def search_corners(tiles):
    return [tile for tile in tiles if len(tile.matches) == 2]


def base_image(size):
    return {(x, y): None for x, y in product(range(size), repeat=2)}


def place_first_tile(image, corner):
    image[(0, 0)] = corner
    while {DOWN, RIGHT} != set(corner.matches.keys()):
        corner.rotate()
    return image


def place_tiles(image):
    for empty_spot, neighbour_spot_, neighbour in spots_to_fill(image):
        side = get_side(empty_spot, neighbour_spot_)
        tile = neighbour.matches[OPPOSITES[side]]
        image[empty_spot] = tile
        tile.flip_and_rotate_to_match(neighbour, side)
    return image


def spots_to_fill(image):
    while not is_filled(image):
        for empty_spot in empty_spots(image):
            for spot, neighbour in neighbour_spot(image, empty_spot):
                yield empty_spot, spot, neighbour


def empty_spots(image):
    yield from {spot for spot, tile in image.items() if tile is None}


def is_filled(image):
    return all(tile is not None for tile in image.values())


def neighbour_spot(image, spot):
    x, y = spot
    for spot_ in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        try:
            neighbour = image.get(spot_)
        except KeyError:
            pass
        else:
            if neighbour is not None:
                yield spot_, neighbour
                break


def get_side(origin, destination):
    return SIDES[subtract(destination, origin)]


def subtract(tuple1, tuple2) -> tuple:
    return tuple(a - b for a, b in zip(tuple1, tuple2))


def side_length(square):
    return int(numpy.math.sqrt(len(square)))


def original_image(tiles, corner_tiles):
    image_size = side_length(tiles)
    image = create_image(corner_tiles, image_size)
    return Tile(1, image_list(combined_image(image, image_size)))


def create_image(corner_tiles, image_size):
    image = base_image(image_size)
    image = place_first_tile(image, corner_tiles[0])
    image = place_tiles(image)
    return image


def combined_image(image, size):
    combined = {}
    for y in range(size):
        for x in range(size):
            data = image[(x, y)].image_data()
            for y0, row in enumerate(data):
                for x0, cell in enumerate(row):
                    combined[(x * len(data) + x0,
                              y * len(data[0]) + y0)] = cell
    return combined


def image_list(image_dict):
    image = []
    for y in range(side_length(image_dict)):
        image.append([])
        for x in range(side_length(image_dict)):
            image[y].append(image_dict[(x, y)])
    return image


def monster_areas(image, monster):
    monster_ = monster.splitlines()
    for y in range(0, len(image) - len(monster_)):
        for x in range(0, len(image[0]) - len(monster_[0])):
            sub_area = image[y:y + len(monster_), x:x + len(monster_[0])]
            sub_string = "\n".join(["".join(row) for row in sub_area])
            yield sub_string


def sea_monster_count(image, monster):
    return sum([monster_count(data, monster) for data in orientations(image)])


def monster_count(image, monster):
    return [True for string in monster_areas(image, monster) if
            re.match(monster, string)].count(True)


def orientations(image_tile):
    for _flip in range(2):
        for _rotation in range(4):
            yield image_tile.data
            image_tile.rotate()
        image_tile.flip()


if __name__ == '__main__':
    TILES = read_input("input")
    search_matches(TILES)
    CORNER_TILES = search_corners(TILES)
    RESULT = math.prod([TILE.id for TILE in CORNER_TILES])
    print(f"Corner tiles multiplied is {RESULT}")

    IMAGE = original_image(TILES, CORNER_TILES)
    MONSTERS = sea_monster_count(IMAGE, MONSTER)
    ROUGHNESS = IMAGE.data_str().count("#") - MONSTERS * MONSTER.count("#")
    print(f"Sea roughness is {ROUGHNESS}")
