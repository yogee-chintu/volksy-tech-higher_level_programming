#!/usr/bin/python3
"""This is Square module"""


class Square:
    """
    sqare module
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an intezer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return (self.__size)**2
