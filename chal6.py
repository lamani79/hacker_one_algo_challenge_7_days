#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    
    # Write your code here

    count = []
    size = len(arr)
    # fill the count list with zeros
    # count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(100):
        count.append(0)

    # [3, 3, 4, 0, 1, 1, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0]
    for x in range(size):
        count[arr[x]] += 1
    return count



    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
