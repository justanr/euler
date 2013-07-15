# http://projecteuler.net/problem=10
#
# Summation of primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Not a very inspiring problem. Pyprimes implements primes functions
# much faster and better than I can (currently).

import pyprimes

print sum(list(pyprimes.primes_below(2000000)))
