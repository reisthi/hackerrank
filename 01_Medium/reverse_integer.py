# https://leetcode.com/problems/reverse-integer/
#
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321


def solution(x):
    a_list = list(str(x))
    first_char = a_list[0]

    if first_char.isnumeric():
        a_list.reverse()
        result = int(''.join(a_list))
    else:
        b_list = a_list[1:]
        b_list.reverse()
        result = int(first_char + ''.join(b_list))

    if result.bit_length() >= 32:
        return 0
    return result
