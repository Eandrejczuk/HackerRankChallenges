# Enter your code here. Read input from STDIN. Print output to STDOUT

def median(a,n):
    if n%2 == 0:
        index = int(n//2)
        return (a[index-1]+a[index])/float(2)
    else:
        return a[int(n/2)]

def create_set(table, frequency):
    new_set = []
    for i in range(len(table)):
        for j in range(frequency[i]):
            new_set.append(table[i])

    return sorted(new_set)

if __name__ == "__main__":
    b = [10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30,
         30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    n = len(b)
    if n%2 != 0:
        q2 = median(b, n)
        b.pop(n//2+1)
        print(b)

    n =len(b)
    print(b[n//2:], len(b[n//2:]))
    q1 = median(b[:n//2], n//2)
    q3 = median(b[n//2:], n//2)
    print(q1, q3)
    print(round(float(q3-q1), 1))

