from collections import Counter

# sherlockAndAnagrams returns an integer that represents the number of anagrammatic pairs of substrings in s.
# Full problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for j in b:
            count+=b[j]*(b[j]-1)/2
    return int(count)

if __name__ == '__main__':
    a = 'abba'
    print(sherlockAndAnagrams(a))