#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with '{:d}'.format().
    Returns True if value was printed (is an integer), otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
