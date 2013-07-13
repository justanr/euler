# http://projecteuler.net/problem=3
#
# Largest Prime Factor
# Problem 3 
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143

p = 3
while n != 1:
    while n % p == 0:
        n = n/p
        largest = p
    p += 2

print largest

# The antigravity way
#
# pip install pyprimes
#
# import pyprimes
# print max(pyprimes.factors(n))
