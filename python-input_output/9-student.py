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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance

        Returns:
            dict: Dictionary containing all attributes of the student
        """
        return self.__dict__
