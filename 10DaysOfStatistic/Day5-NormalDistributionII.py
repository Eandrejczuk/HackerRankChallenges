# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

# The final grades for a Physics exam taken by a large group of students have a mean of 70 and a standard deviation of 10.
# If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:
#
# Scored higher than 80 (i.e., have a grade > 80)?
# Passed the test (i.e., have a grade >= 60)?
# Failed the test (i.e., have a grade < 60)?
# Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

#70 10
#80
#60
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

if __name__ == '__main__':
    # Set data
    mean, std = list(map(float, input().split()))
    higher_score = float(input())
    passed_grade = float(input())

    print(round((1 - cumulative(mean, std, 80)) * 100, 2))
    print(round((1 - cumulative(mean, std, 60)) * 100, 2))
    print(round(cumulative(mean, std, 60) * 100, 2))

# 15.87
# 84.13
# 15.87