#!/usr/bin/python3
"""
This module defines the MyList class.
"""


class MyList(list):
    """A subclass of list with a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying it."""
        print(sorted(self))
