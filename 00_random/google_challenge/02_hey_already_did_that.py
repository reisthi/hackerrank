import numpy as np


cycle_a = list()
cycle_b = list()


def solution(number, b, i):
    original_size = len(number)
    while i < 100:
        x = order_number(number[:original_size], desc=True)
        y = order_number(number[:original_size], desc=False)
        z = subtract_as_decimals(x, y, b)
        z = convert_to_base_n(z, b)
        z = resize(z, original_size)
        if z not in cycle_a:
            cycle_a.append(z)
        else:
            if z not in cycle_b:
                cycle_b.append(z)
            else:
                return len(cycle_b), cycle_b
        i += 1
        return solution(z, b, i)


def order_number(number, desc):
    """ Returns digits of a number in order desc or asc in a string format. """
    a_list = list()
    [a_list.append(a) for a in number]
    a_list.sort(reverse=desc)
    return ''.join(a_list)


def subtract_as_decimals(x, y, b):
    """ Converts two numbers into their corresponding decimals.
        Returns the difference between them.
    """
    xd, yd = int(x, b), int(y, b)
    return xd - yd


def convert_to_base_n(number, b):
    if type(number) == str:
        number = int(number)
    return np.base_repr(number, b)


def resize(number, size):
    if type(number) == int:
        number = str(number)
    number_length = len(str(number))
    if number_length == size:
        return number
    if number_length > size:
        return number[:size]
    return number.zfill(size)

