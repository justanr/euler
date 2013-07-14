# http://projecteuler.net/problem=7
#
# 10001st Prime
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from pyprimes import primes

y = primes()
x = 10001

while x != 1:
    x = x - 1
    next(y)

print next(y)
