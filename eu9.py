import time

start = time.time()

outer = 1000

for a in range(1,(outer/2)+1):
    for b in range(a,(outer/2)+1):
        c = (a**2+b**2)**0.5
        if a+b+c==outer:
            print a,b,c
            print a*b*c
            break
    

print "Runtime: %s" % (time.time() - start)

# 200 375 425.0
# 31875000.0
# Runtime: 0.0931360721588
