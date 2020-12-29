"""Tests"""
import unittest

import numpy

from main import Tile, UP, RIGHT, DOWN, LEFT, sea_monster_count, MONSTER, \
    read_input, search_matches, search_corners, original_image, create_image


class TestTile(unittest.TestCase):

    def setUp(self):
        self.tile = Tile(1, ["..#.", "##.#", "....", "#.#."])

    def test_upside(self):
        self.assertEqual(self.tile.upside, "..#.")

    def test_right_side(self):
        self.assertEqual(self.tile.right_side, ".#..")

    def test_downside(self):
        self.assertEqual(self.tile.downside, "#.#.")

    def test_left_side(self):
        self.assertEqual(self.tile.left_side, ".#.#")

    def test_flip(self):
        upside, right_side, downside, left_side = self.tile.sides()
        self.tile.flip()
        self.assertEqual(self.tile.upside, downside)
        self.assertEqual(self.tile.right_side, "".join(reversed(right_side)))
        self.assertEqual(self.tile.downside, upside)
        self.assertEqual(self.tile.left_side, "".join(reversed(left_side)))

    def test_rotate_sides(self):
        upside, right_side, downside, left_side = self.tile.sides()
        self.tile.rotate()
        self.assertEqual(self.tile.upside, right_side)
        self.assertEqual(self.tile.right_side, "".join(reversed(downside)))
        self.assertEqual(self.tile.downside, left_side)
        self.assertEqual(self.tile.left_side, "".join(reversed(upside)))

    def test_rotate_changes_matches(self):
        self.tile.matches = {UP: 1, RIGHT: 2,
                             DOWN: 3, LEFT: 4}
        self.tile.rotate()
        self.assertEqual(self.tile.matches[UP], 2)
        self.assertEqual(self.tile.matches[RIGHT], 3)
        self.assertEqual(self.tile.matches[DOWN], 4)
        self.assertEqual(self.tile.matches[LEFT], 1)

    def test_flip_changes_matches(self):
        self.tile.matches = {UP: 1, RIGHT: 2,
                             DOWN: 3, LEFT: 4}
        self.tile.flip()
        self.assertEqual(self.tile.matches[UP], 3)
        self.assertEqual(self.tile.matches[RIGHT], 2)
        self.assertEqual(self.tile.matches[DOWN], 1)
        self.assertEqual(self.tile.matches[LEFT], 4)

    def test_sides(self):
        self.assertEqual(
            self.tile.sides(),
            ('..#.', '.#..', '#.#.', '.#.#')
        )

    def test_reversed_sides(self):
        self.assertEqual(
            self.tile.reversed_sides(),
            ('.#..', '..#.', '.#.#', '#.#.')
        )

    def test_all_sides(self):
        self.assertEqual(
            self.tile.all_sides(),
            ('..#.', '.#..', '#.#.', '.#.#', '.#..', '..#.', '.#.#', '#.#.')
        )

    def test_sides_match(self):
        other = Tile(2, ["....", "....", "....", "..#."])
        other2 = Tile(3, ["....", "....", "....", ".#.."])
        self.assertTrue(self.tile.sides_match(other, "upside"))
        self.assertFalse(self.tile.sides_match(other2, "upside"))

    def test_image_data(self):
        expected = [["#", "."], [".", "."]]
        data = self.tile.image_data()
        for x in range(2):
            for y in range(2):
                self.assertEqual(data[x][y], expected[x][y])


IMAGE = """.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
"""


class TestMain(unittest.TestCase):

    def test_monster_search(self):
        tile = self._create_test_tile()
        self.assertEqual(sea_monster_count(tile, MONSTER), 2)

    @staticmethod
    def _create_test_tile():
        data = numpy.array([list(row) for row in IMAGE.splitlines()])
        tile = Tile(1, data)
        return tile

    def test_corner_tiles(self):
        _, corner_tiles = self._get_tiles_corner_tiles()
        for corner_id in [1951, 3079, 2971, 1171]:
            self.assertTrue(corner_id in [tile.id for tile in corner_tiles])

    @staticmethod
    def _get_tiles_corner_tiles():
        tiles = read_input("test_input")
        search_matches(tiles)
        corner_tiles = search_corners(tiles)
        return tiles, corner_tiles

    def test_create_image(self):
        tiles, corner_tiles = self._get_tiles_corner_tiles()
        corner_tiles[0].flip()
        image = create_image(corner_tiles, 3)
        # 1951, 2311, 3079
        # 2729, 1427, 2473
        # 2971, 1489, 1171
        self.assertEqual(image[0, 0].id, 1951)
        self.assertEqual(image[0, 1].id, 2729)
        self.assertEqual(image[0, 2].id, 2971)
        self.assertEqual(image[1, 0].id, 2311)
        self.assertEqual(image[1, 1].id, 1427)
        self.assertEqual(image[1, 2].id, 1489)
        self.assertEqual(image[2, 0].id, 3079)
        self.assertEqual(image[2, 1].id, 2473)
        self.assertEqual(image[2, 2].id, 1171)

    def test_original_image(self):
        tiles, corner_tiles = self._get_tiles_corner_tiles()
        image_tile = original_image(tiles, corner_tiles)
        for side in self._create_test_tile().sides():
            self.assertTrue(side in image_tile.all_sides())
