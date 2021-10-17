#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    first_diagnol = 0
    second_diagnol = 0

    # first diagnol:
    for x in range(0,n):
        first_diagnol += arr[x][x]
        
    # second diagnol:
    for x in range(0,n):
        second_diagnol += arr[(n-1)-x][x]
    
    return abs(first_diagnol - second_diagnol)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
