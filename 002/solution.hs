fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

evenFibs :: [Integer]
evenFibs = filter (\f -> f `mod` 2 == 0) fibs

evenFibsLessThan :: Integer -> [Integer]
evenFibsLessThan n = takeWhile (< n) evenFibs

solution :: Integer
solution = sum $ evenFibsLessThan 4000000 

main = print solution
