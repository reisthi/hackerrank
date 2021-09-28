"""
    Example:
    string = ABCDEFGHIJKLIMNOQRSTUVWXYZ
    max_width = 4
"""""

import math


def w(string, max_width):
    new_string = str()
    counter, size = 0, max_width
    iterations = math.ceil(len(string)/max_width)
    for a in range(0, iterations):
        # print(a, type(string[counter:size]))
        new_string += string[counter:size] + '\n'
        counter = size
        size += max_width
    return new_string