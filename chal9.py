#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphabets = list(string.ascii_lowercase)
    is_uper = 0

    new_str = ''
    for letter in s:
        if letter.lower() not in alphabets:
            new_str += letter
            continue
        
        index = alphabets.index(letter.lower())
        new_index = (index + k) % len(alphabets) # I make modulo 26 not 25 because we start from the 0 index
        if letter.isupper():
            new_str += alphabets[new_index].upper()
        else:
            new_str += alphabets[new_index]
    return new_str
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
