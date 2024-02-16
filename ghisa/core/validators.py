"""
Module for validators and decorators 
"""

# from ghisa.logger import logger

from ..validators import Validator


class Number(Validator):
    """Validator for numbers"""

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Expected {self.private_name[1:]} to be an int or float : received {type(value)} for {value}"
            )
