"""
Module for validators and decorators 
"""

import os
from ghisa.logger import logger

# import logging
from abc import ABC, abstractmethod


from ghisa.core.defaults import DEFAULT_CONFIG


class Validator(ABC):
    """Abstract class for validators"""

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    """Validator for numbers"""

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Expected {self.private_name[1:]} to be an int or float : received {type(value)} for {value}"
            )


# class GhProfileUrl(Validator):
#     """Validator for the profile url"""

#     def validate(self, value):
#         if not isinstance(value, str):
#             raise TypeError(
#                 f"Expected {self.private_name[1:]} to be a string : received {type(value)} for {value}"
#             )
#         if not value.startswith("https://github.com"):
#             raise ValueError(
#                 f"Expected {self.private_name[1:]} to be a github url : received {value}"
#             )

#         value = value.split("/tree/")[0]
#         value = value.removesuffix("/")

#         value = [i for i in value if i == "/"]

#         if len(value) != 4:
#             raise ValueError(
#                 f"Expected {self.private_name[1:]} to be a github url : received {value}"
#             )


# class GhRepository(Validator):
#     """Validator for the profile url"""

#     def validate(self, value):
#         if not isinstance(value, str):
#             raise TypeError(
#                 f"Expected {self.private_name[1:]} to be a string : received {type(value)} for {value}"
#             )
#         if not value.startswith("https://github.com"):
#             raise ValueError(
#                 f"Expected {self.private_name[1:]} to be a github url : received {value}"
#             )

#         value = value.split("/tree/")[0]
#         value = value.removesuffix("/")

#         value = [i for i in value if i == "/"]

#         if len(value) != 3:
#             raise ValueError(
#                 f"Expected {self.private_name[1:]} to be a github url : received {value}"
#             )
