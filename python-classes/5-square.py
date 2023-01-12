#!/usr/bin/python3
"""SUARE MODULE"""


class Square:
    """
    Square MOdule
    """
    def __init__(self, size=0):
    """
    Intialize square
    """
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        return (self.__size) ** 2

    def my_print(self):
        """
        Prints square with #'s
        """
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))

