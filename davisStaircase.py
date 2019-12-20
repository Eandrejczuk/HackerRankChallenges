import os

dict = {0:0, 1:1, 2:2, 3:4}

# the stepPerms function recursively calculatse and returns the integer number of ways Davis can climb the staircase, modulo 10000000007.
#
# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
#
# stepPerms has the following parameter(s):
# n: an integer, the number of stairs in the staircase

def stepPerms(n):
    if n in dict.keys():
        return dict.get(n)
    result = stepPerms(n-3) + stepPerms(n-2) + stepPerms(n-1)
    dict.update({n: result})
    return dict.get(n)

if __name__ == '__main__':

    s = [1, 3, 7]

    for s_itr in s:
        res = stepPerms(s_itr)
        print(str(res))
