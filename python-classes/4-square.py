#!/usr/bin/python3
"""This is Square module"""


class Square:
    """
    sqare module
    """
    def __init__(self, size=0):
        self.size = size
    def size(self):
        return self.__size
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an intezer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        return (self.__size)**2
