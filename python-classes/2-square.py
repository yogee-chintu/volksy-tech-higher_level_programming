#!/usr/bin/python3
""""THIS CODE WRIITEN BY YOGEE"""


class Square:
    """This is square class"""
    def __init__(self, size=0):
        """
        The init method
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


