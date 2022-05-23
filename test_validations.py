#!/usr/bin/env python3

from validations import validate_user
import unittest

class Testvalidtions(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(validate_user("pritam", 3), True)
    
    def test_too_short(self):
        self.assertEqual(validate_user("rj", 4), False)

    def test_invalid_character(self):
        self.assertEqual(validate_user("Hey_there", 3), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)


# Runs the test
unittest.main()
