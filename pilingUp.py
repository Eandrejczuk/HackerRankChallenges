from collections import deque

#There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
# The new pile should follow these directions: if cube_i is on top of cube_j then sideLength_j >= sideLength_i.

# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
# Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

# https://www.hackerrank.com/challenges/piling-up/problem
#
# The function pileOFCubes outputs a single line containing either Yes if possible to stack cubes and No otherwise.

#pileOfCubes has the following parameter(s):
#table: an array of integers

def pileOfCubes(table):
    queue = deque(table)

    for cube in reversed(sorted(queue)):
        if queue[-1] == cube:
            queue.pop()
        elif queue[0] == cube:
            queue.popleft()
        else:
            print('No')
            break
    else:
        print('Yes')

if __name__ == '__main__':
    table = [[4, 3, 2, 1, 3, 4], [1, 3, 2]]

    for i in table:
        pileOfCubes(i)

