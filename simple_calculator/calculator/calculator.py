# -*- coding: utf-8 -*-
import ast
from typing import Tuple, Union


class Calculator:
    """
    This class handles all the available operations you can perform with this
    simple_calculator
    """
    value_1 = None
    operation = None
    value_2 = None
    _allowed_operations = {
        '+': 'sum',
        '-': 'subtraction',
        '*': 'multiply',
        '/': 'divide',
        '^': 'exponent'
    }

    def __init__(self, operation):
        self.requested_calculation = operation

    def _guess_the_cast(self) -> None:
        """
        Evaluate the value if it's an int or float.
        :return:
        """
        self.value_1 = ast.literal_eval(self.value_1)
        self.value_2 = ast.literal_eval(self.value_2)
        print('\033[32m{}\033[0m'.format(type(self.value_1)), flush=True)  # green
        print('\033[32m{}\033[0m'.format(type(self.value_2)), flush=True)  # green

    def prepare_values_for_operation(self) -> Tuple[bool, str]:
        """
        Making sure the values provided types are allowed
        @TODO: In the future we could handle operations of multiple arguments

        Also trying to catch some possible situations.
        :return:
        """
        values = self.requested_calculation.split()

        if len(values) > 3:
            return False, 'The operation can only be of two values'

        try:
            self.value_1, self.operation, self.value_2 = values
        except ValueError:
            return False, 'The requested operation must have spaces e.g. 1 + 2'

        try:
            self._guess_the_cast()
        except ValueError:
            return False, 'This simple_calculator only works for integers or floats'
        finally:
            if not isinstance(self.value_1, (int, float)) \
                    or not isinstance(self.value_2, (int, float)):
                return False, 'This simple_calculator only works for integers or floats'

        return True, ''

    def sum(self, value_1: int, value_2: int) -> int:
        """
        This method represents sum
        :param value_1:
        :param value_2:
        :return:
        """
        return value_1 + value_2

    def subtraction(
            self, value_1: Union[int,float], value_2: Union[int,float]) \
            -> Union[int,float]:
        """
        This subracts the second value to the first
        :param value_1:
        :param value_2:
        :return:
        """
        return value_1 - value_2

    def multiply(
            self, value_1: Union[int,float], value_2: Union[int,float]) \
            -> Union[int,float]:
        """
        The multipication of two values
        :param value_1:
        :param value_2:
        :return:
        """
        return value_1 * value_2

    def divide(self, value_1: Union[int,float], value_2: Union[int,float]):
        """
        The division of two values
        :param value_1:
        :param value_2:
        :return:
        """
        return value_1 / value_2

    def exponent(self,value_1: Union[int,float], value_2: Union[int,float]):
        """
        x^y
        :param value_1:
        :param value_2:
        :return:
        """
        return value_1 ** value_2

    def calculate(self) -> Union[Tuple[bool, str], Tuple[bool, int]]:
        """
        Perform the actual operation
        :return:
        """
        success, message = self.prepare_values_for_operation()
        if not success:
            return success, message

        the_operand = self._allowed_operations.get(self.operation, None)
        if the_operand is None:
            return False, f'Only the following operations are allowed: ' \
                          f'{self._allowed_operations}'

        func = getattr(self, the_operand)
        try:
            result = func(self.value_1, self.value_2)
        except ZeroDivisionError:
            return False, 'Oh no! You tried to create a black hole! ' \
                          'That is a no no!'

        return True, result
