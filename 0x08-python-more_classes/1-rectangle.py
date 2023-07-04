#!/usr/bin/python3

"""Create a class Rectangle that defines a rectangle"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """To retreive attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set the attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value