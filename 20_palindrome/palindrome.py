# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.
#
# Example 1:
#
# Input: x = 121
# Output: true


def solution(x: int) -> bool:
    # convert to list of strings
    x_copy = list(str(x))

    # find the middle item
    mid = int(len(x_copy) / 2)

    # deal with odd length
    if mid % 2 == 1:
        x_copy.remove(x_copy[mid])

    # slice list into two
    h_a = x_copy[:mid]
    h_b = x_copy[mid:]

    # reverse 2nd
    h_b = h_b[::-1]

    # compare
    if h_a == h_b:
        return True

    return False


def solution_b(x: int) -> bool:
    if x < 0:
        return False

    return str(x) == str(x)[::-1]
