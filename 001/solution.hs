import Data.List (union)

solution = sum $ union [3,6..999] [5,10..999]

main = print solution
