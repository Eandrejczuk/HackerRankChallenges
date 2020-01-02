
# https://www.hackerrank.com/challenges/30-bitwise-and/problem

if __name__ == '__main__':
    t = 3

    N = [5, 8, 2]
    K = [2, 5, 2]

    for t_itr in range(t):

        n = N[t_itr]
        k = K[t_itr]

        print(k-1 if ((k-1) | k) <= n else k-2)
