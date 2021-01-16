#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positives(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float(self):
        self.assertEqual(max_integer([1.6, 2.5, 3.1, 4.5]), 4.5)

    def test_unique(self):
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        self.assertRaises(TypeError, max_integer())

    def test_words(self):
        self.assertRaises(TypeError, max_integer(['hello', 'world']))

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)
