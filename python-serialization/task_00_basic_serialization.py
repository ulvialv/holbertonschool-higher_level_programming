#!/usr/bin/python3
"""
Basic serialization module for JSON files

This module provides functionality to serialize Python dictionaries
to JSON files and deserialize JSON files back to Python dictionaries.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the output JSON file

    Note:
        If the file exists, it will be replaced
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserialize a JSON file to a Python dictionary

    Args:
        filename (str): Name of the input JSON file

    Returns:
        dict: Python dictionary with deserialized data
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
