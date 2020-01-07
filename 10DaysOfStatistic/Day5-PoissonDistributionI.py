# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

# A random variable, X, follows Poisson distribution with mean of 2.5.
# Find the probability with which the random variable X is equal to 5.

from math import factorial, pow, exp

def poisson_dist(k, poisson_lambda):
    return pow(poisson_lambda, k) * exp(-poisson_lambda)/factorial(k)

if __name__ == "__main__":
    mean = 2.5
    success = 5
    print(round(poisson_dist(success, mean), 3))