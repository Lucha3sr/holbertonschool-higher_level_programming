#!/usr/bin/python3

"""Write the class Rectangle that inherits from Base"""

from models.base import Base

class Rectangle(Base):

    """Private instance attributes each with its own public getter and setter"""

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get value """
        return self.__width

    @width.setter
    def width(self, width):
        """set value"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ get value """

        return self.__height

    @height.setter
    def height(self, height):
        """set value"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
         """ get value """
        return self.__x

    @x.setter
    def x(self, x):
        """set value"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ get value """
        return self.__y

    @y.setter
    def y(self, y):
        """set value"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
        self.__y = y

    def area(self):
        """area of rectangle"""
        return self.width * self.height
