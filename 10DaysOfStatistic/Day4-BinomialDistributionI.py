# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

# TThe ratio of boys to girls for babies born in Russia is 1.09 : 1.
# If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters.
# Then print your result, rounded to a scale of 3 decimal places.

from math import factorial, pow

def binomial_dist(numSuccess, numTrials, probability):
    return factorial(numTrials) / (factorial(numSuccess) * factorial(numTrials - numSuccess)) \
           * pow(probability, numSuccess) * pow(1 - probability, numTrials - numSuccess)

if __name__ == "__main__":
    boys = 1.09 / 2.09
    num_children = 6
    num_boys = 3
    sum_prob = 0
    for i in range(num_boys, num_children+1):
        sum_prob += binomial_dist(i, num_children, boys)
    print(round(sum_prob, 3))