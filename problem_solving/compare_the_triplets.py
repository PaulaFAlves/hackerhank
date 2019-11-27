"""
Given a and b, determine their respective comparison points.
For example, a = [1,2,3] are tje number for Alice,
 and b =[3,2,1] are the numbers for Bob. 
As a[0] < b[0], then Bob awarded a point. 
As a[1] == b[1], then no points are earned. 
As a[2] > b[2], then Alice awarded a point.
Your retorn array must be [1,1], as each one 
earned a point in this example.

"""
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    i = 0
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice, bob

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	a = list(map(int, input().rstrip().split()))

	b = list(map(int, input().rstrip().split()))

	result = compareTriplets(a, b)

	fptr.write(' '.join(map(str, result)))
	fptr.write('\n')

	fptr.close()