#!/usr/bin/python3
"""Module for reading and printing file contents"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its contents to stdout

    Args:
        filename: Path to the file to read (default: empty string)
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content, end='')
