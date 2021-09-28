"""
Returns number of pair of socks in an array.
Example:
        n = 9
        array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
"""


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
