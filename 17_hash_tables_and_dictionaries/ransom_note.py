from collections import Counter


def solution(a_list, b_list):
    ca, cb = Counter(a_list), Counter(b_list)
    cb.subtract(ca)
    passed = 'Yes'

    for item in cb.values():
        if item >= 1:
            passed = 'No'
            break
    print(passed)
