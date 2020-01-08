
# https://www.hackerrank.com/challenges/word-order/problem

# You are given n words. Some words may repeat. For each word, output its number of occurrences.
#
# The output order should correspond with the input order of appearance of the word.
#
# Note: Each input line ends with a "\n" character.

# Sample input:

"""
4
bcdef
abcdefg
bcde
bcdef
"""

# if __name__ == 'main':
n = int(input())
words = dict()

for _ in range(n):
    word = str(input())
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(' '.join(map(str, words.values())))


