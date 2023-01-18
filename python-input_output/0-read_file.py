#!/usr/bin/python3
"""python input output"""


def read_file(filename=""):
    """def_file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='")
