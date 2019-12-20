import os
import heapq

# the cookies function outputs the number of operations that are needed to increase the cookie's sweetness >= k and -1 if not possible
# Complete the cookies function below.
#
# https://www.hackerrank.com/challenges/jesse-and-cookies/problem
#
#cookies has the following parameter(s):
#k: minimum sweetness
#A: an array containing a sweetness of each cookie

def cookies(k, A):
    count_operations = 0
    heapq.heapify(A)
    try:
        while True:
            smallest_element = heapq.heappop(A)
            if smallest_element < k:
                sweetness = smallest_element + 2 * heapq.heappop(A)
                heapq.heappush(A, sweetness)
                count_operations += 1
            else:
                return count_operations
    except:
        return -1

if __name__ == '__main__':

    n = 6
    k = 7
    sweetness_array = [1, 2, 3, 9, 10, 12]

    result = cookies(k, sweetness_array)
    print(str(result) + '\n')

