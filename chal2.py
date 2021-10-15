#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    arr_size = len(arr)
    # max sum = last elment in the arry
    max_sum = arr[- 1] 
    # min_sum = first elemnt inthe arry
    min_sum = arr[0]

    for x in range(1,4):
        min_sum += arr[x]
    
    for x in range(2,5):
        max_sum += arr[-x]
    print(min_sum,max_sum)

    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
