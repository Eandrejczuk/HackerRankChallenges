# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def standard_deviation(table, n):
    avg_elem = sum(table)/float(n)
    temp = 0
    for i in table:
        temp += math.pow(i - avg_elem, 2)
        print(temp)
    return math.sqrt(temp/float(n))

if __name__ == "__main__":
    n = 5
    elements = [10, 40, 30, 50, 20]
    print(standard_deviation(elements, n))
