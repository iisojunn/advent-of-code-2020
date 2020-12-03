"""Test Day 3 task related methods"""
import unittest
from math import prod

from main import read_input, trees_on_the_path


class TestTreeCounting(unittest.TestCase):

    def test_trees_on_the_path(self):
        tree_map = read_input("test_input")
        self.assertEqual(trees_on_the_path(tree_map, 1, 1), 2)
        self.assertEqual(trees_on_the_path(tree_map, 3, 1), 7)
        self.assertEqual(trees_on_the_path(tree_map, 5, 1), 3)
        self.assertEqual(trees_on_the_path(tree_map, 7, 1), 4)
        self.assertEqual(trees_on_the_path(tree_map, 1, 2), 2)

    def test_math_prod_can_be_used(self):
        self.assertEqual(prod([2, 7, 3, 4, 2]), 336)
