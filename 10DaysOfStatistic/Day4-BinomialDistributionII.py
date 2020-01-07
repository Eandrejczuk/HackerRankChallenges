# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

# A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because
# they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:
#
# No more than 2 rejects?
# At least 2 rejects?

# Write a program to compute the answer using the above parameters.
# Then print your result, rounded to a scale of 3 decimal places.

from math import factorial, pow

def binomial_dist(numSuccess, numTrials, probability):
    return factorial(numTrials) / (factorial(numSuccess) * factorial(numTrials - numSuccess)) \
           * pow(probability, numSuccess) * pow(1 - probability, numTrials - numSuccess)

if __name__ == "__main__":
    percentage = 0.12
    batch_size = 10
    num_faulty = 2
    sum_prob = 0
    sum_prob1 = 0
    for i in range(0, num_faulty+1):
        sum_prob1 += binomial_dist(i, batch_size, percentage)
    print(round(sum_prob1, 3))

    sum_prob2 = 0
    for i in range(num_faulty, batch_size):
        sum_prob2 += binomial_dist(i, batch_size, percentage)
    print(round(sum_prob2, 3))