import sys
import config
sys.path.append(config.APP_PATH)
import unittest
from app import point

class TestApp(unittest.TestCase):
    def test_addition(self):
        p1 = point.Point(1, 2)
        p2 = point.Point(3, 4)
        expected = point.Point(4, 6)
        self.assertEqual(p1 + p2, expected)