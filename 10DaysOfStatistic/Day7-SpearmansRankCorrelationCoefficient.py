
# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

# The first line contains an integer, n, denoting the number of values in data sets X and Y.
# The second line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set X.
# The third line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set Y.

"""
10
10 9.8 8 7.8 7.7 1.7 6 5 1.4 2
200 44 32 24 22 17 15 12 8 4
"""

def ranking(elementslist):
    sortedElementsList = sorted(elementslist)
    sortedDict = dict()

    for i in range(len(elementslist)):
        sortedDict[sortedElementsList[i]] = i+1

    return sortedDict

def spearmansCorrelation(X, Y):
    rankX = ranking(X)
    rankY = ranking(Y)
    n = len(X)

    d = []
    for j in range(n):
        d.append(rankX[X[j]] - rankY[Y[j]])

    sumd = sum([pow(x,2) for x in d])

    return 1 - (6 * sumd / ( n * (pow(n , 2) - 1)))

if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))

    print(round(spearmansCorrelation(X, Y), 3))

