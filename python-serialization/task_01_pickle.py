#!/usr/bin/python3
"""
Custom object serialization module using pickle

This module provides a CustomObject class that can serialize and
deserialize itself using Python's pickle module.
"""
import pickle


class CustomObject:
    """
    A custom class that demonstrates serialization with pickle

    Attributes:
        name (str): Name of the person
        age (int): Age of the person
        is_student (bool): Whether the person is a student
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance

        Args:
            name (str): Name of the person
            age (int): Age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle

        Args:
            filename (str): Name of the file to save the object to

        Returns:
            None if an error occurs, otherwise nothing
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle

        Args:
            filename (str): Name of the file to load the object from

        Returns:
            CustomObject: Deserialized object, or None if error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, Exception):
            return None
