#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    h = len(arr)-1
    side_one, side_two = 0, 0
    for a in range(len(arr)):
        side_one += arr[a][a]   # (00) + (11) + (22)...
        side_two += arr[a][h-a]   # (01) + (11) + (20)...
    return abs(side_one - side_two)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()