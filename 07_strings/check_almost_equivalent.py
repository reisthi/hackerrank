# Two strings word1 and word2 are considered almost equivalent
# if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
from collections import Counter


def solution(string_a, string_b):
    ca, cb = Counter(string_a), Counter(string_b)

    ca.subtract(cb)

    for key, value in ca.values():
        if abs(value) > 3:
            return False
    return True
