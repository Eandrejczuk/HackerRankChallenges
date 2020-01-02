
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

# A large elevator can transport a maximum of 9800 pounds.
#
# Suppose a load of cargo containing 49 boxes must be transported via the elevator.
#
# The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds.
#
# Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

"""
9800
49
205
15
"""

import math

# Define functions
def cumulative_normal(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

if __name__ == '__main__':
    # Set data
    max_load = float(input())
    number_boxes = int(input())
    mean = float(input())
    std = float(input())

    print(round(cumulative_normal(mean * number_boxes, std * math.sqrt(number_boxes), max_load), 4))


