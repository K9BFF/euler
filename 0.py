# project euler
# problem 0

# a number is a perfect square, or a square number, if it is the square of a positive integer.
# for example, 25 is a square number because 5**2 = 5*5 = 25; it is also an odd square.
# the first 5 square numbers are 1, 4, 9, 16, and 25, and the sum of the odd squares is 1+9+25 = 35
# among the first 742 thousand square numbers, what is the sum of all the odd squares?

import math

print("Problem 0")

# game plan
# find squares (math.sqrt = whole nr?)

for i in range(742000): # for loop to count up to 742000
    if math.sqrt(i) % 2 == 1: # if the square root is odd...
