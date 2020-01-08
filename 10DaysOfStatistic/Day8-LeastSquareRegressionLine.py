
# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

# A group of five students enrolls in Statistics immediately after taking a Math aptitude test.
#
# Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed as the following list of points:

"""
x   y
95 85
85 95
80 70
70 65
60 70
"""
#
# If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics?
#
# Determine the equation of the best-fit line using the least squares method, then compute and print the value of y when x = 80.

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

def linear_regression(x, y):
    b = pearsonCoefficient(x, y) * standard_deviation(y) / standard_deviation(x)
    return mean(y) - b * mean(x), b

if __name__ == "__main__":
    x, y = zip(*(map(float, input().split()) for _ in range(5)))
    a, b = linear_regression(x, y)

    x1 = 80

    print(round(a+b*x1, 3))

# 78.288