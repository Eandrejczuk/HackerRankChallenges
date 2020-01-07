# Enter your code here. Read input from STDIN. Print output to STDOUT

# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

# The probability that a machine produces a defective product is 1/3.
#
# What is the probability that the 1st defect is found during the 5th inspection?

from math import pow

def geometric_dist(numTrials, probability):
    return probability * pow(1 - probability, numTrials - 1)

if __name__ == "__main__":
    probability = 1 / float(3)
    trials = 5
    print(round(geometric_dist(trials, probability), 3))