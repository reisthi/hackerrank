#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    index = n - 1 if n > 1 else 1  # in case n is 1
    temp = 0 if n > 1 else 1
    for a in range(n - 1):
        temp = n * index
        n = temp
        index -= 1
    print(temp)

# Another approach
def extraLongFactorials_2(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)