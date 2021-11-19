"""
    Example:
    string = ABCDEFGHIJKLIMNOQRSTUVWXYZ
    max_width = 4
"""""

import math


def w(string, max_width):
    if max_width <= 0:
        return

    new_string = str()
    counter, size = 0, max_width
    iterations = len(string) // max_width

    for a in range(0, iterations):
        new_string += string[counter:size] + '\n'
        counter = size
        size += max_width
    print(new_string)