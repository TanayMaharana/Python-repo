#!/usr/bin/env python3

from reverse_name import reverse_name
import unittest

class testing(unittest.TestCase):
  def testbasic(self):
    testcase = "Maharana, Tanay"
    expected = "Tanay Maharana"
    self.assertEqual(reverse_name(testcase), expected)

  def testemptystring(self):
    testcase = ""
    expected = ""
    self.assertEqual(reverse_name(testcase), expected)

  def testdoublename(self):
    testcase = "Maharana, Tanay M."
    expected = "Tanay M. Maharana"
    self.assertEqual(reverse_name(testcase), expected)

  def testsinglename(self):
    testcase = "Tanay"
    expected = "Tanay"
    self.assertEqual(reverse_name(testcase), expected)

unittest.main()
