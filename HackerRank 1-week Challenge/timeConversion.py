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
    isAM = False
    se = filter(str.isdigit, s)
    toInt = int(se)
    result = ""
    if "AM" in s:
        isAM = True
    if toInt in range(10000, 115900) and isAM:
        result = str(toInt)
    elif toInt in range(120000, 125900) and not isAM:
        result = str(toInt)
    elif toInt in range(120000, 125900) and isAM:
        result = str(toInt-120000)
    elif toInt in range(10000, 115900) and not isAM:
        result = str(toInt+120000)
    
    result = ''.join(list(''.join(l + ':' * (n % 2 == 1) for n, l in enumerate(result)))) 
    return result[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
