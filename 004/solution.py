def is_palindrome(n):
    return n == n[::-1]


def find_largest_palindrome_number():
    largest = 0
    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            num = x*y
            if num > largest and str(num) == str(num)[::-1]:
                largest = num
    return largest

print(find_largest_palindrome_number())
