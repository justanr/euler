from itertools import takewhile

def fibs():
    a, b = 0, 1
    while True:
        yield a+b
        a, b = b, a+b

even_fibs = (f for f in fibs() if not f%2) 
solution = sum(takewhile(lambda x: x < 4000000, even_fibs)) 

print(solution)
