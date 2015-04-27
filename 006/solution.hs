squared_sum n = (n * ( n + 1) / 2) ^ 2
summed_squares n = (n * (n + 1) * (2 * n + 1))/6
main = print $ (squared_sum 100) - (summed_squares 100)
