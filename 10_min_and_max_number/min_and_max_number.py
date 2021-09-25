""" Find min and max number in an array.

    - Own custom method.
    - Of course, simple min() and max() method.

"""

import random
from timeit import default_timer as timer


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


def gen_random_list(n, mini, maxi):
    a_list = list()
    [a_list.append(random.randint(mini, maxi)) for a in range(0, n)]
    return a_list


def holy(args):
    start = timer()
    # gen_random_list()
    print(custom_max_min_num(args))
    end = timer()
    print(f"Finished: {end - start} ms")