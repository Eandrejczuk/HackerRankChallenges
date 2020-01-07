# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

# Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

"""
10
10 9.8 8 7.8 7.7 7 6 5 4 2
200 44 32 24 22 17 15 12 8 4
"""
import math

def mean(X):
    return sum(X) / len(X)

def covariance(X, Y):
    meanX = mean(X)
    meanY = mean(Y)
    covariance = 0
    for i in range(len(X)):
        covariance +=(X[i] - meanX)*(Y[i] - meanY)
    return covariance / len(X)

def standard_deviation(table):
    avg_elem = sum(table)/float(len(table))
    temp = 0
    for i in table:
        temp += math.pow(i - avg_elem, 2)
    return math.sqrt(temp/float(len(table)))

def pearsonCoefficient(X, Y):
    covarXY = covariance(X, Y)
    return covarXY / (standard_deviation(X) * standard_deviation(Y))

if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))

    print(round(pearsonCoefficient(X, Y), 3))

