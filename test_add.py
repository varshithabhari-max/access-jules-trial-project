import unittest
from add import add


class TestAdd(unittest.TestCase):
    def test_add_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_integers(self):
        self.assertEqual(add(-1, -5), -6)

    def test_add_mixed_integers(self):
        self.assertEqual(add(10, -4), 6)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
