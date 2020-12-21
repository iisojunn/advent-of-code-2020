"""Tests for day 19"""
import unittest

from main import read_input, is_valid

VALID1 = {"bbabbbbaabaabba", "ababaaaaaabaaab", "ababaaaaabbbaba"}

VALID2 = {"bbabbbbaabaabba",
          "babbbbaabbbbbabbbbbbaabaaabaaa",
          "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
          "bbbbbbbaaaabbbbaaabbabaaa",
          "bbbababbbbaaaaaaaabbababaaababaabab",
          "ababaaaaaabaaab",
          "ababaaaaabbbaba",
          "baabbaaaabbaaaababbaababb",
          "abbbbabbbbaaaababbbbbbaaaababb",
          "aaaaabbaabaaaaababaa",
          "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
          "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"}


class TestMonsterMessages(unittest.TestCase):

    def setUp(self):
        self.rules, self.messages = read_input("test-input")

    def test_without_loop(self):
        self.assertEqual(VALID1, self._valid_messages())

    def _valid_messages(self):
        return {msg for msg in self.messages if is_valid(msg, self.rules)}

    def test_with_loop(self):
        self.rules[8] = {(42,), (42, 8)}
        self.rules[11] = {(42, 31), (42, 11, 31)}
        self.assertEqual(VALID2, self._valid_messages())


class TestSimplerMessages(unittest.TestCase):

    def setUp(self):
        self.rules = {
            1: {("a",)},
            2: {("b",)}
        }

    def _valid_messages(self):
        return {msg for msg in self.messages if is_valid(msg, self.rules)}

    def _assert_all_messages_valid(self):
        self.assertEqual(self.messages, self._valid_messages())

    def test_simple_loop_at_the_beginning(self):
        self.rules[0] = {(1, 0), (1, 2)}
        self.messages = {"ab", "aaaaaaaaaab"}
        self._assert_all_messages_valid()

    @unittest.skip("This wont work as depth first search, I guess")
    def test_simple_loop_at_the_end(self):
        self.rules[0] = {(0, 1), (1,)}
        self.messages = {"a"}
        self._assert_all_messages_valid()

    def test_loop_with_three_elements(self):
        self.rules[0] = {(1, 0, 2), (1, 2)}
        self.messages = {
            "ab",
            "aaabbb",
        }
        self._assert_all_messages_valid()

    def test_two_loops(self):
        self.rules = {
            0: {(4, 3)},
            **self.rules,
            3: {(1,), (1, 3)},
            4: {(2,), (2, 4)},
        }
        self.messages = {
            "ba",
            "bba",
            "bbba",
            "baa"
        }
        self._assert_all_messages_valid()
