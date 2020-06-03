# -*- coding: utf-8 -*-
import unittest

from simple_calculator.calculator.calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator('1 + 1')

    def test_results_type(self):
        result = self.calc.calculate()
        self.assertTrue(isinstance(result, tuple))

    def test_sum(self):
        val_1 = 1
        val_2 = 1
        result = self.calc.sum(val_1, val_2)
        self.assertTrue(result == 2)

    def test_subtraction(self):
        val_1 = 2.0
        val_2 = 1
        result = self.calc.subtraction(val_1, val_2)
        self.assertTrue(result == 1.0)

    def test__guess_the_cast_wrong(self):
        calc = Calculator('1 + a')
        self.assertRaises(ValueError, calc._guess_the_cast)

    def test_divide_by_zero(self):
        val_1 = 2
        val_2 = 0
        self.assertRaises(
            ZeroDivisionError, self.calc.divide, val_1, val_2)


