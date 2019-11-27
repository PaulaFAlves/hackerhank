"""
Given an array of integers, find the sum of its elements.
For example, if the array a = [1,2,3], so return is 6.
"""
import os
import sys


def simpleArraySum(ar):
    n = 0
    tamanho = len(ar)
    sum = 0
    for n in range(tamanho):
        sum += ar[n]
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()