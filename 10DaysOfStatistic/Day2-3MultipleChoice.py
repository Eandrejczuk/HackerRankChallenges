# Day 2: Basic Probability
#In a single toss of  fair (evenly-weighted) six-sided dice,
# find the probability that their sum will be at most 9.

#impossible combinations:
#5+5 2/36
p1 = 1/6 * 1/6 + 1/6 * 1/6
#5+6 2/36
p2 = 1/6 * 1/6 + 1/6 * 1/6
#6+6 2/36
p3 = 1/6 * 1/6 + 1/6 * 1/6

#print(p1+p2+p3) p = 1/6

#Day 2: More Dice
# In a single toss of 2 fair (evenly-weighted) six-sided dice,
# find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

# 2 + 4 2/36
# 1 + 5 2/36

# p = 1/9

# Day 2: Compound Event Probability

#Urn 1 contains 4 red balls and 3 black balls.
#Urn 2 contains 5 red balls and 4 black balls.
#Urn 3 contains 4 red balls and 4 black balls.

#One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?
#possibilities:
# red red black
# red black red
# black red red
p = 4/7*5/9*4/8 + 4/7*4/9*4/8 + 3/7*5/9*4/8
print(p)

#Day 3: Conditional Probability
# Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?
#P(B|A) = P(A * B) / P(A)
# P(B|A) = 1/3

# Day 3: Cards of the Same Suit
# You draw 2 cards from a standard -card deck without replacing them.
# What is the probability that both cards are of the same suit?

p = 13/52 * 12/51 * 4
print(p)

# Day 3: Drawing Marbles
#A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement.
# If the first marble drawn is red, what is the probability that the second marble is blue?
# p = 4/6