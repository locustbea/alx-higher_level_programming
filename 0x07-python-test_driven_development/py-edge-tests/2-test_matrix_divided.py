#!/usr/bin/python3

import unittest

from matrix_divided import matrix_divided


class TestMatrixDividedFunction(unittest.TestCase):

    # Test that the function raises a TypeError if the input matrix is empty.
    def test_matrix_divided_with_empty_input_matrix(self):
        with self.assertRaises(TypeError):
            matrix_divided([], 10)

    # Test that the function raises a TypeError if any of the elements in the input matrix are not numbers.
    def test_matrix_divided_with_invalid_input_element(self):
        with self.assertRaises(TypeError):
            matrix_divided([[2, 4, 8], [1, "foo", 3]], 2)

    # Test that the function raises a ZeroDivisionError if the divisor is zero.
    def test_matrix_divided_with_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            matrix_divided([[2, 4, 8], [1, 2, 3]], 0)

    # Test that the function returns the correct result for normal input.
    def test_matrix_divided_with_normal_input(self):
        expected_result = [[1.0, 2.0, 4.0], [0.5, 1.0, 1.5]]
        actual_result = matrix_divided([[2, 4, 8], [1, 2, 3]], 2)

        # Verify that the expected and actual results are equal.
        self.assertEqual(expected_result, actual_result)

# My path route is not working as expected
if __name__ == "__main__":
    unittest.main()
