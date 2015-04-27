from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return b


def lcm(a, b):
    return abs(a*b)//gcd(a, b)

print(reduce(lcm, range(11, 21)))
