fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
solution = sum $ takeWhile (<4000000) $ filter even fibs
main = print solution
