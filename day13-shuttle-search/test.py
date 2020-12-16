"""Tests"""

import unittest

from main import search_t, bus_requirements


class ShuttleTimeTests(unittest.TestCase):

    def assert_t(self, schedule, t):
        found_t = search_t(bus_requirements(schedule))
        self.assertEqual(found_t, t)

    def test_searching_t(self):
        self.assert_t("17,x,13,19", 3417)
        self.assert_t("67,7,59,61", 754018)
        self.assert_t("67,x,7,59,61", 779210)
        self.assert_t("67,7,x,59,61", 1261476)
        self.assert_t("1789,37,47,1889", 1202161486)
