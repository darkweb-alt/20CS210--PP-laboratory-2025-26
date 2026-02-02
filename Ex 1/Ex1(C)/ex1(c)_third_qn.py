# 3. Write a Python function that takes a string as input and returns the number of vowels (a, e, i, o, u) present in the string.
# The function should be case-insensitive
# Do not count consonants or special characters

def count_vowels(s):
    s = s.lower()
    vowels = "aeiou"
    return sum(1 for char in s if char in vowels)

# Example
text = "Hello World"
print("Vowels count:", count_vowels(text))
