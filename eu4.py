import time
start = time.time()

largest = 1

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        if y < x:
            continue
        a = x*y
        if (str(a) == str(a)[::-1]) and (largest < x*y):
            largest = x*y

runtime = time.time() - start

print "Largest: %s" % (largest)
print "Runtime: %s" % (runtime)


# This algorithm is ~28 times faster (~.02 seconds compared to ~.56) than mine 
# And a lot more efficent.
#
# a = 999
# lowerlimit = 0 
# largest = 0
# 
# while(a>=100):
#     for b in range(lowerlimit, 1000):
#         palnum = a*b
#         if (str(palnum) == str(palnum)[::-1]):
#             print palnum
#             if palnum > largest:
#                 largest = palnum
# 
#         if (largest != 0):
#             lowerlimit = int(largest/a)
#         else:
#             lowerlimit = a
#     a = a - 1
# 
# print "Largest: %s" % (str(largest))
