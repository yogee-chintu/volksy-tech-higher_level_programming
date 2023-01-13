#!/usr/bin/python3
"""python module"""


def inherits_from(obj, a_class):
    """inherits program"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
