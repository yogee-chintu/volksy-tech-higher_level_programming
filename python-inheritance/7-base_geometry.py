#!/usr/bin/python3
"""python"""


class BaseGeometry:
    """base geometry"""
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an greater than 0".format(name))

    def area(self):
        raise Exception("area() is not implemented")
