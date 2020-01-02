#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/30-regex-patterns/problem

if __name__ == '__main__':
    N = 6

    email_table = [['riya', 'riya@gmail.com'],['julia', 'julia@julia.me'],['julia', 'sjulia@gmail.com'],
                   ['samantha', 'samantha@gmail.com'], ['tanya', 'tanya@gmail.com'], ['julia', 'julia@gmail.com']]

    lst=[]
    for N_itr in range(N):

        firstName = email_table[N_itr][0]

        emailID = email_table[N_itr][1]

        if re.search('@gmail\.com$', emailID):
            lst.append(firstName)
    print(*sorted(lst), sep='\n')
