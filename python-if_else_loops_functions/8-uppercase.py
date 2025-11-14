#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            new_str += chr(ord(c) - 32)
        else:
            new_str += c
    print("{}".format(new_str))
