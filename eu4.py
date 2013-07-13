def reverse(n):
    n = str(n)
    return ''.join(n[::-1])

def isPalin(n):
    n = str(n)
    return n == reverse(n)


largest = 1

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        if y < x:
            continue
        if isPalin(x*y) and (largest < x*y):
            largest = x*y

print largest
