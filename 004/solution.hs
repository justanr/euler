isPalindrome n = n == reverse n
palins = [x*y | x <- [99..999], y <- [x..999], isPalindrome $ show (x*y)]
solution = maximum palins
main = print(solution)
