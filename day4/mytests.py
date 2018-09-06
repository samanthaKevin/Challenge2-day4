import unittest
from recursion import *

class MyFirstTests(unittest.TestCase):
    def test_recursive_power(self):
        self.assertEqual(recursive_power(3,4), 81)
        self.assertEqual(recursive_power(2,3), 8)