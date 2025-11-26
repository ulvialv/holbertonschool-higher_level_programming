#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using Rectangle"""

    def __init__(self, size):
        """Initialize Square with size validated by integer_validator"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
