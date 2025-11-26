#!/usr/bin/python3
"""Module for writing text to files"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns the number of characters written
    Args:
        filename: Path to the file to write (default: empty string)
        text: Text content to write to the file (default: empty string)
    Returns:
        Number of characters written to the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        nb_characters = f.write(text)
        return nb_characters
