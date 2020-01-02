# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

# In a certain plant, the time taken to assemble a car is a random variable, X,
# having a normal distribution with a mean of 29 hours and a standard deviation of 2 hours.
#
# What is the probability that a car can be assembled at this plant in:
#
# Less than 19.5 hours?
# Between 20 and 22 hours?

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

if __name__ == '__main__':
    # Set data
    mean, std = list(map(float, input().split()))
    less_period = float(input())
    between_period = list(map(float, input().split()))

    # Gets the result and show on the screen
    print (round(cumulative(mean, std, less_period),3))
    print (round(cumulative(mean, std, between_period[1]) - cumulative(mean, std, between_period[0]), 3))