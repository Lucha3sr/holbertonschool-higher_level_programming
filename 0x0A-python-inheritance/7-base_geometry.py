#!/usr/bin/python3

"""class based on 5-base_geometry.py"""


class BaseGeometry:

    """Public instance method"""

    def area(self):

        """raises an Exception with the message area() is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """Public instance method that validates value"""

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
