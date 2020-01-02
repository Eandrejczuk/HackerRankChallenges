
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

# You have a sample of 100 values from a population with mean 500 and with standard deviation 80.
#
# Compute the interval that covers the middle 0.95 of the distribution of the sample mean; in other words, compute A and B such that P(A < x < B) > 0.95.
#
# Use the value of z = 1.96. Note that 1.96 is the z-score.


"""
100
500
80
.95
1.96
"""
import math

# Define functions
def cumulative_normal(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

if __name__ == '__main__':
    # Set data
    n = int(input())
    mean = float(input())
    baseStdDev = float(input())
    stdDev = baseStdDev / math.sqrt(n)
    z = 1.96

    A = mean - z * stdDev
    B = mean + z * stdDev

    print(round(A, 2))
    print(round(B, 2))