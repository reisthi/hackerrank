# An anagram is positive result between a comparison of two words with the same characters frequency.
from collections import Counter


def solution(a, b):
    ca = Counter(a)
    cb = Counter(b)
    ca.subtract(cb)

    if sum([abs(item) for item in ca.values()]) == 0:
        return True
    return False


# without using Collections
def solution_2(a, b):
    dict_a, dict_b = dict(), dict()
    result = 0
    checked_items = list()

    for i in a:
        if i not in dict_a:
            dict_a[i] = 1
        else:
            new_value = dict_a[i] + 1
            dict_a[i] = new_value

    for i in b:
        if i not in dict_b:
            dict_b[i] = 1
        else:
            new_value = dict_b[i] + 1
            dict_b[i] = new_value

    for k, v in dict_a.items():
        checked_items.append(k)
        if k in dict_b:
            result += abs(dict_b[k] - v)

    for k, v in dict_b.items():
        if k not in checked_items and k in dict_a:
            result += abs(dict_a[k] - v)

    return True if result == 0 else False




