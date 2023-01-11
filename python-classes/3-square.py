#!/usr/bin/python3
"""THIS CODE WRITTEN BY YOGEE"""


class Square:
    """This is asquare class"""
    def __init__(self, size=0)
    if type(size) != int:
        raise TypeError("size must be intezer")
    if size < 0:
        raise ValueError("size must be >=0")
    def area(self):
