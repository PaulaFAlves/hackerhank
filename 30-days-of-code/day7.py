"""
Objective
Today, we're learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, N, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Input Format

The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers describing array A's elements.
"""

import math
import os
import random
import re
import sys

def print_reverse(arr):
    print(*reversed(arr)) # the * used to unpack iterables. that means instead of pass the list, like ['x', 'y'], it pass only the content, what means x y.
   

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print_reverse(arr)