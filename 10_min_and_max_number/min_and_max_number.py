""" Find min and max number in an array.

    - Own custom method.
    - Of course, simple min() and max() method.

"""


def custom_max_min_num(array):
    minimum, maximum = 0, 0
    for number in range(0, len(array)):
        if float(array[number]) < minimum:
            minimum = float(array[number])
        if float(array[number]) > maximum:
            maximum = float(array[number])
    return f"max: {maximum}. min: {minimum}"


def min_max(array):
    return f"max: {max(array)}. min: {min(array)}"
