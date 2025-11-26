#!/usr/bin/python3
"""Function that checks if an object is exactly an instance of a class"""



def is_same_class(obj, a_class):
    """Return True if obj is exactly instance of a_class; otherwise False"""
    return type(obj) == a_class
