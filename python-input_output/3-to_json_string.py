#!/usr/bin/python3
"""Module for JSON serialization"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string

    Args:
        my_obj: Python object to serialize (list, dict, str, int, etc.)

    Returns:
        JSON string representation of the object
    """
    return json.dumps(my_obj)
