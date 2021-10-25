import numpy as np

cycle_a = list()
cycle_b = list()


def solution(number, b):
    original_size = len(number)
    if b == 3:
        return b
    while True:
        x, y = order_number(number, desc=True), order_number(number, desc=False)
        z = str(int(x) - int(y))
        z = convert_to_base(z, b)
        z = resize(z, original_size)
        if z not in cycle_a:
            cycle_a.append(z)
        else:
            if z not in cycle_b:
                cycle_b.append(z)
            else:
                return len(cycle_b)
        # print(f'{x} - {y} = {z}')
        return solution(z, b)


def subtract(a, b):
    return int(a) - int(b)


def order_number(number, desc):
    """ Returns digits of a number
        in order desc or asc in a string format.
    """
    a_list = list()
    [a_list.append(a) for a in number]
    a_list.sort(reverse=desc)
    return ''.join(a_list)


def convert_to_base(number, b):
    if type(number) == str:
        number = int(number)
    return np.base_repr(number, b)


def resize(number, size):
    number_length = len(str(number))
    if number_length == size:
        return number
    if number_length > size:
        return number[:size]
    return number.zfill(size)

