#!/usr/bin/python3
"""Function that checks if object inherits from a_class"""


def inherits_from(obj, a_class):
    """Return True if obj is instance of subclass of a_class
    (directly or indirectly), but NOT if obj is exactly a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
