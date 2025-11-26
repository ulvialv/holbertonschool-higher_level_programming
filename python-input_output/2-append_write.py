#!/usr/bin/python3
"""Module for appending text to files"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file and returns
    the number of characters added

    Args:
        filename: Path to the file (default: empty string)
        text: Text content to append (default: empty string)

    Returns:
        Number of characters added to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        nb_characters = f.write(text)
        return nb_characters
