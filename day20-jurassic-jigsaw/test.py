"""Tests"""
import unittest

from main import Tile


class TestTile(unittest.TestCase):

    def setUp(self):
        self.tile = Tile(1, ["..#", "###", ".##"])

    def test_upside(self):
        self.assertEqual(self.tile.upside, "..#")

    def test_downside(self):
        self.assertEqual(self.tile.downside, ".##")

    def test_right_side(self):
        self.assertEqual(self.tile.right_side, "###")

    def test_left_side(self):
        self.assertEqual(self.tile.left_side, ".#.")

    def test_transpose(self):
        upside, right_side, downside, left_side = self.tile.sides()
        self.tile.transpose()
        self.assertEqual(self.tile.upside, left_side)
        self.assertEqual(self.tile.right_side, downside)
        self.assertEqual(self.tile.downside, right_side)
        self.assertEqual(self.tile.left_side, upside)

    def test_rotate(self):
        upside, right_side, downside, left_side = self.tile.sides()
        self.tile.rotate()
        self.assertEqual(self.tile.upside, right_side)
        self.assertEqual(self.tile.right_side, "".join(reversed(downside)))
        self.assertEqual(self.tile.downside, left_side)
        self.assertEqual(self.tile.left_side, "".join(reversed(upside)))

    def test_sides(self):
        self.assertEqual(
            self.tile.sides(),
            ('..#', '###', '.##', '.#.')
        )

    def test_reversed_sides(self):
        self.assertEqual(
            self.tile.reversed_sides(),
            ('#..', '###', '##.', '.#.')
        )

    def test_all_sides(self):
        self.assertEqual(
            self.tile.all_sides(),
            ('..#', '###', '.##', '.#.', '#..', '###', '##.', '.#.')
        )
