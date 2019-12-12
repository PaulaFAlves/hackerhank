"""
Objective
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a string, S, of length N that is indexed from 0 to N - 1 , print its even-indexed and odd-indexed characters as  2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a String, S .
"""


for N in range(int(input())): #read the number of loops
    S = input() # read the string that we want to work with
    print(S[::2], S[1::2]) # print 1.all the letters on the even positions 2.all the letters from que odd positions