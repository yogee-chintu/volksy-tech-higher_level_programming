#!/usr/bin/python3
"""python input output."""


def read_file(filename=""):
    """prints the contents of a utf8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
