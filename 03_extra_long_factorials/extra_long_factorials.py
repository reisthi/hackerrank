#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the extraLongFactorials function below.
def extra_long_factorials(n):
    index = n - 1 if n > 1 else 1  # in case n is 1
    temp = 0 if n > 1 else 1
    for a in range(n - 1):
        temp = n * index
        n = temp
        index -= 1
    print(temp)


# Another approach
def extra_long_factorials_2(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)


def recursive_factorial(x):
    if x == 1:
        return x
    else:
        return x * recursive_factorial(x - 1)


if __name__ == '__main__':
    n = int(input())

    extra_long_factorials(n)