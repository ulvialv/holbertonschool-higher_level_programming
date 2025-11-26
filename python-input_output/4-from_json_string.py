#!/usr/bin/python3
"""Module for JSON deserialization"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string

    Args:
        my_str: JSON string to deserialize

    Returns:
        Python data structure (list, dict, etc.) from JSON string
    """
    return json.loads(my_str)
