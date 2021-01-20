#!/usr/bin/python3

"""Write a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Instantiation with width and height"""

    def __init__(self, width, height):

        """width and height must be private"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        """the area() method implemented"""

        return self.__width * self.__height

    def __str__(self):

        """
        str method should return, the following rectangle description:"""
        """[Rectangle] <width>/<height>"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
