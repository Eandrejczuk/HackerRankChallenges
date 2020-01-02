
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

# The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of 2.4 and a standard deviation of 2.
#
# A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
#
# If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

"""
250
100
2.4
2.0
"""
import math

# Define functions
def cumulative_normal(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

if __name__ == '__main__':
    # Set data
    tickets_left = float(input())
    number_students = int(input())
    mean = float(input())
    std = float(input())

    print(round(cumulative_normal(mean * number_students, std * math.sqrt(number_students), tickets_left), 4))