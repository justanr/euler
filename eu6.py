# http://projecteuler.net/problem=6
#
# Sum square difference
# Problem 6
#
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_sq_diff(limit):
    sq_total = sum(range(limit+1))**2
    total_sq = sum([x**2 for x in range(limit+1)])

    return sq_total - total_sq

print sum_sq_diff(100)

# The actual formula for this
# n = 100
# (n*(n+1)/2)^2 - (n*(n+1)*(2*n+1)/6)
# Much faster.
