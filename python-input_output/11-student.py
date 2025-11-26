#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """
    A class that defines a student

    Attributes:
        first_name (str): First name of the student
        last_name (str): Last name of the student
        age (int): Age of the student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): List of attribute names to retrieve.
                         If None, retrieve all attributes.

        Returns:
            dict: Dictionary containing specified attributes
        """
        if attrs is None:
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)
        return filtered_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary

        Args:
            json (dict): Dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
