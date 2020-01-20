#!/bin/python3

# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

# We define super digit of an integer x using the following rules:
#
# Given an integer, we need to find the super digit of the integer.
#
# If x has only 1 digit, then its super digit is .
# Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

"""
9875 4
"""

import os

# Complete the superDigit function below.
def superDigit(n, k):
    digit_string = str(n)
    if len(digit_string) == 0:
        return 0
    elif len(digit_string) == 1:
        return digit_string
    else:
        return superDigit(str(sum([int(x) for x in digit_string])) * k, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
