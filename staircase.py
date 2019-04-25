#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    index = 1
    for a in range(n):
        print(' ' * (n-index) + '#' * index)
        index += 1


if __name__ == '__main__':
    n = int(input())

    staircase(n)

# result if n = 6
     #
    ##
   ###
  ####
 #####
######