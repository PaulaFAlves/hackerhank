"""
Objective
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

Task
Given an integer, n , print its first 10 multiples. Each multiple n x i (where 1<= i <= 10 ) should be printed on a new line in the form: n x i = result.
"""

import math
import os
import random
import re
import sys

def mult(n):
    for i in range(1, 11):
        result = n * i
        print(n, 'x', i, '=', result)
        i += 1


if __name__ == '__main__':
    n = int(input())
    mult(n)