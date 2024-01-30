import unittest
from ..6-max_integer import max_integer

class TestMaxIntegerFunction(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 0, 3, -7]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_duplicate_max_value(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_strings_in_list(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])

    def test_non_iterable_argument(self):
        with self.assertRaises(TypeError):
            max_integer(123)

if __name__ == '__main__':
    unittest.main()

