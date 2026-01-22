"""
Sample Test
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test that two numbers are added together."""
        res = calc.add(1, 2)

        self.assertEqual(res, 3)

    def test_substract_numbers(self):
        """Test that two numbers are substracted."""
        res = calc.substract(10, 5)

        self.assertEqual(res, 5)
