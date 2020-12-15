"""Tests"""
import unittest

from main import read_input, count_occupied, seats_changed, is_congested, \
    new_status, adjacent_spots


class TestSeatOccupancy(unittest.TestCase):

    def setUp(self):
        self.layout = read_input("test_input")

    def test_count_occupied(self):
        self.assertEqual(count_occupied(self.layout), 20)

    def test_seats_changed(self):
        self.assertFalse(seats_changed(self.layout, self.layout))
        self.assertTrue(seats_changed(reversed(self.layout), self.layout))

    def test_is_congested(self):
        self.assertFalse(is_congested(["#", ".", "L"], 4))
        self.assertFalse(is_congested(["#", "#", "#"], 4))
        self.assertTrue(is_congested(["#", "#", "#", "#"], 4))
        self.assertTrue(is_congested(["#", "#", "#", "#", "#"], 4))

    def test_adjacent_spots(self):
        self.assertEqual(adjacent_spots(self.layout, 2, 0),
                         ['.', 'L', 'L', 'L', 'L'])

    def test_new_status(self):
        self.assertEqual(new_status("L", ['.', 'L', 'L', 'L', 'L'], 4), "#")
