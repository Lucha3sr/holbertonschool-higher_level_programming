#!/usr/bin/python3

"""Write a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""import from 7-base_geometry"""


class Rectangle(BaseGeometry):

    """Instantiation with width and height"""

    def __init__(self, width, height):

        """width and height must be private"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width__ = width
        self.__height__ = height
