#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):

    """Instantiation with width and height"""

    def __init__(self, width, height):

        """width and height must be private"""
        self.__width__ = width
        self.__height__ = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
