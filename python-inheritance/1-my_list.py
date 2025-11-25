#!/usr/bin/python3
"""This module defines the MyList class.The MyList class inherits from list and adds a method to print the list in a sorted (ascending) order without modifying it."""


class MyList(list):
    """A class that inherits from list and prints the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
