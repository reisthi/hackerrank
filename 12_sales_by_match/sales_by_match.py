"""
It must return an integer representing the number of matching pairs of socks that are available
Example:
        n = 9
        array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
"""
from collections import Counter

def solution(array):
    """ Return the amount of pair of numbers in a list. """
    amount = 0
    new_list = []
    for item in array:
        if item not in new_list:
            new_list.append(item)
            if array.count(item) > 1:
                amount += int(array.count(item) / 2)
    return amount


def solution_2(array):
    coll = Counter(array)
    pairs = 0

    for key, value in coll.items():
        if value > 1:
            pairs += value // 2
    return pairs
