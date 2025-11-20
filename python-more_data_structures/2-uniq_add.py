#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = []
    total = 0

    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.append(num)
            total += num

    return total
