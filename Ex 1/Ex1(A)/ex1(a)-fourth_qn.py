# Question 4:
# Menu-Driven Calculator
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# Enter first number: 20
# Enter second number: 10
# Enter your choice: 4
# Result: 2.0

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Result:", first + second)
    case 2:
        print("Result:", first - second)
    case 3:
        print("Result:", first * second)
    case 4:
        print("Result:", first / second)
    case _:
        print("Invalid Choice")






