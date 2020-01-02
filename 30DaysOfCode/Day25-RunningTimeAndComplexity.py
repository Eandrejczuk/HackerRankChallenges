
# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

def isPrime(n):
    if n == 1:
        return 'Not prime'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 'Not prime'
    return 'Prime'

T = 3
table =  [12, 5, 7]

for i in range(T):
    number = table[i]
    print(isPrime(number))

