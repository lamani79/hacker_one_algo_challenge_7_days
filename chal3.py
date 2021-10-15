#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # 12:00:00 am ==> 00:00:00
    # 12:00:00 pm ==> 12:00:00
##################################
# 1/ knowing if the time is in am or pm
    am = 'AM' in s.upper() # return true or false
# 2/ get min and sec and hour in a list
    time = s.split(':')
    # remove 'PM' and 'AM' from the list 
    time[2] = time[2][0:2]
    hour = int(time[0])  # convert to int
    mins = int(time[1])
    secs = int(time[2])

    if(hour in range(1,13)):
        print('hour format ok')
        
        if(am): #if the morning
            if(hour == 12):
                print(f'00:{mins:02}:{secs:02}')
            else:
                # convert time to int and  then transform the one degit into two
                print(f'{hour:02}:{mins:02}:{secs:02}')
        else:  #in the evening
            if(hour == 12):
                print(f'12:{mins:02}:{secs:02}')
            else:
                # I dont convert hour into two degits because (hour+12) > two degits
                print(f'{hour+12}:{mins:02}:{secs:02}')


# // turn print to return to work in hacker One


    else:
        print('date format error')

    
  

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    # result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()

    timeConversion(s)
