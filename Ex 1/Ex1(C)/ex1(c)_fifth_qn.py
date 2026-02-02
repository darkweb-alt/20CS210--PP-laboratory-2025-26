# 5. Write a recursive Python program to analyze a given positive integer.
# You must NOT use loops (for, while).
# Given an integer n, write recursive functions to:
# Count the number of digits
# Find the sum of digits
# Find the maximum digit
# Reverse the number
n = 12345

# 1. Count digits
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

# 2. Sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

# 3. Maximum digit
def max_digit(n):
    if n < 10:
        return n
    return max(n % 10, max_digit(n // 10))

# 4. Reverse number
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

print("Digits count:", count_digits(n))
print("Sum of digits:", sum_digits(n))
print("Maximum digit:", max_digit(n))
print("Reversed number:", reverse_number(n))
