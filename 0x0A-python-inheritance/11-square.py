#!/usr/bin/python3

""" class Square that inherits from Rectangle (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle
Square = __import__('10-square').Square

class Square(Rectangle):

    """Instantiation with size: def __init__(self, size)"""

    def __init__(self, size):

        """ size must be private. No getter or setter"""
        """size must be a positive integer, validated by integer_validator"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def area(self):
            """ the area() method implemented"""

            return self.__size * self.__size

        def __str__(self):

            """str method should return the square description"""
            return "[Square] {}/{}".format(self.__width, self.__height)
