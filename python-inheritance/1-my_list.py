#!/usr/bin/python3
class Mylist(list):
    """A class that inherits from list and adds a method to print the list sorted."""


    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original."""
        print(sorted(self))

