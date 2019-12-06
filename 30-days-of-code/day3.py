"""
Objective
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an n integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.
"""

import math
import os
import random
import re
import sys

def test(n):
    if (n % 2 != 0):
        print('Weird') 
    elif (n >= 2) and (n <= 5):
        print('Not Weird')
    elif (n >= 6) and (n < 20):
        print('Weird')
    elif (n >= 20):
        print('Not Weird')

if __name__ == '__main__':
    n = int(input())
    test(n)