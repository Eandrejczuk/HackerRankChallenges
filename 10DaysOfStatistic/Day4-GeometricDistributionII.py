# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

# The probability that a machine produces a defective product is 1/3.
#
# What is the probability that the 1st defect is found during the first 5 inspections?

from math import pow

def geometric_dist(numTrials, probability):
    return pow(1 - probability, numTrials)

if __name__ == "__main__":
    probability = 1 / float(3)
    trials = 5

    print(round(1 - geometric_dist(trials, probability), 3))