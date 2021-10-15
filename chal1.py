#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arr_size = len(arr)
    neg_nums = 0
    pos_nums = 0
    zeros = 0
    for x in arr:
        if(x<0):
            
            neg_nums += 1 
        elif(x>0):
            pos_nums += 1
        else:
            zeros += 1
    
    neg_nums /= arr_size
    pos_nums /= arr_size
    zeros /= arr_size

    print('pos nums: ',format(pos_nums,'.6f'))
    print('neg nums: ',format(neg_nums,'.6f'))
    print('zeros nums: ',format(zeros,'.6f'))
    
if __name__ == '__main__':
    n = int(input('entre the array size; ').strip())

    arr = list(map(int, input('entre the array elements sperate them with space: ').rstrip().split()))

    plusMinus(arr)


    # #################################################################
    # hacher rank format:
    #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    # Write your code here
    arr_size = len(arr)
    neg_nums = 0
    pos_nums = 0
    zeros = 0
    for x in arr:
        if(x<0):
            
            neg_nums += 1 
        elif(x>0):
            pos_nums += 1
        else:
            zeros += 1
    
    neg_nums /= arr_size
    pos_nums /= arr_size
    zeros /= arr_size

    print(format(pos_nums,'.6f'))
    print(format(neg_nums,'.6f'))
    print(format(zeros,'.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
