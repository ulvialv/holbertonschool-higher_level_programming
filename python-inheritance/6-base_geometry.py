#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """Base class for geometry"""

    def area(self):
        """Raises an exception because area is not implemented"""
        raise Exception("area() is not implemented")
