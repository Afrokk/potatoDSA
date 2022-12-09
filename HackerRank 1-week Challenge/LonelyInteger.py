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
# [1,2,3,4,3,2,1]
# [1], [1]
# [2], 1,2
# [3], 1,2,3
# ... [1,2,3,4,3]

def lonelyinteger(a):
    # Write your code here
    if len(a) == 1:
        return a[0]

    for n in a:
        if a.count(n) == 1:
            return n
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
