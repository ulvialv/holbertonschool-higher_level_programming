#!/usr/bin/python3
"""Module for loading objects from JSON files"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file

    Args:
        filename: Name of the JSON file to read

    Returns:
        Python object created from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
