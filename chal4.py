#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
        # Write your code here
    time = 0;
    size = len(a)

    for x in range(0,size):
        time = 0
        for y in range(0,size):
            if x == y:
                continue
            if a[x] == a[y]:
                time =  time + 1
                break
        
        if time == 0:
            return a[x]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
