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
    positive, negative, zero = 0, 0, 0
    # Write your code here
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else: 
            zero += 1
    print("{:.6f}".format(round(float(positive/len(arr)), 6)))
    print("{:.6f}".format(round(float(negative/len(arr)), 6)))
    print("{:.6f}".format(round(float(zero/len(arr)), 6)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
