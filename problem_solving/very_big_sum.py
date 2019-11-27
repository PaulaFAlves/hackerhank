"""
Complete the Very Big Sum function, it must return the sum of all array elements.
The first line of the input consists of an integer.
The next line contains n spaces-separeted integers contained in the array.
"""
import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    count = len(ar)
    n = 0
    for n in range(count):
        sum += ar[n]
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()