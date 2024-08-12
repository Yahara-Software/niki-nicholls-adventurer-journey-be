import unittest
from distance_calculator import DistanceCalculator


class TestDistanceCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = DistanceCalculator()

    def test_calculate_fixed_direction_distance_returns_correct_output(self):
        self.assertAlmostEqual(round(self.calculator.calculate_fixed_direction_distance("5F5R"), 5),7.07107)
        self.assertAlmostEqual(round(self.calculator.calculate_fixed_direction_distance("5F5R5B"), 5),5)
        self.assertAlmostEqual(round(self.calculator.calculate_fixed_direction_distance("5B5L"), 5),7.07107)
        self.assertAlmostEqual(round(self.calculator.calculate_fixed_direction_distance("5L5F"), 5), 7.07107)

    def test_calculate_fixed_direction_distance_handles_multiple_digits(self):
        self.assertAlmostEqual(round(self.calculator.calculate_fixed_direction_distance("1F23R"), 5),23.02173)
        self.assertAlmostEqual(round(self.calculator.calculate_fixed_direction_distance("100F2000R"), 5),2002.49844)

    def test_calculate_fixed_direction_distance_handles_invalid_input(self):
        for char in "fbrlACDNESW !@#$%^&*()_-":
            with self.assertRaises(ValueError):
                self.calculator.calculate_relative_direction_distance(f"{char}2R3B")
        with self.assertRaises(ValueError):
            self.calculator.calculate_fixed_direction_distance(" 3F2Z3B")
        with self.assertRaises(ValueError):
            self.calculator.calculate_fixed_direction_distance("3F 3B")
        with self.assertRaises(ValueError):
            self.calculator.calculate_fixed_direction_distance("3F3B ")

    def test_calculate_relative_direction_distance_returns_correct_output(self):
        self.assertAlmostEqual(round(self.calculator.calculate_relative_direction_distance("5F5R5R"), 5),
                               5)
        self.assertAlmostEqual(round(self.calculator.calculate_relative_direction_distance("5B5R5R"), 5),
                               5)
        self.assertAlmostEqual(round(self.calculator.calculate_relative_direction_distance("5B5L"), 5),
                               7.07107)
        self.assertAlmostEqual(round(self.calculator.calculate_relative_direction_distance("5R5R"), 5),
                               7.07107)
        self.assertAlmostEqual(round(self.calculator.calculate_relative_direction_distance("10F5R5R"), 5),
                               7.07107)

    def test_calculate_relative_direction_distance_handles_multiple_digits(self):
        self.assertAlmostEqual(round(self.calculator.calculate_relative_direction_distance("1F10R"), 5), 10.04988)
        self.assertAlmostEqual(round(self.calculator.calculate_relative_direction_distance("123B1000R"), 5), 1007.5361)

    def test_calculate_relative_direction_distance_handles_invalid_input(self):
        for char in "fbrlACDNESW !@#$%^&*()_-":
            with self.assertRaises(ValueError):
                self.calculator.calculate_relative_direction_distance(f"{char}2R3B")
        with self.assertRaises(ValueError):
            self.calculator.calculate_relative_direction_distance(" 3F2Z3B")
        with self.assertRaises(ValueError):
            self.calculator.calculate_relative_direction_distance("3F 3B")
        with self.assertRaises(ValueError):
            self.calculator.calculate_relative_direction_distance("3F3B ")


if __name__ == '__main__':
    unittest.main()
