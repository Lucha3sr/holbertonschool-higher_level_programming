#!/usr/bin/python3


""" this class defines a square that has a Private instance attribute size"""


class Square:

    """Instantiation with optional size"""

    def __init__(self, size=0, position=(0, 0)):

        """size is private attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):

        """getting the value"""
        return self.__size

    @size.setter
    def size(self, size):

        """setting the value"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ print square with #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
