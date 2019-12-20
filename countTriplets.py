from collections import Counter

#The countTriplets function returns the number of triplets forming a geometric progression for a given r as an integer.
#
#Full challenge: https://www.hackerrank.com/challenges/count-triplets-1/problem
#
#countTriplets has the following parameter(s):
#arr: an array of integers
#r: an integer, the common ratio

def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0

    for v in arr:
        if v in r3:
            count += r3[v]

        if v in r2:
            r3[v * r] += r2[v]

        r2[v * r] += 1

    return count

if __name__ == '__main__':
    r = 2
    array = [1,2,1,2,3,6,4]
    print(countTriplets(array,r))