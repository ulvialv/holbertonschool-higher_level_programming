#!/usr/bin/python3
"""Module for saving objects to JSON files"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation

    Args:
        my_obj: Python object to serialize and save
        filename: Name of the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
