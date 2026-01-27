 # Question 1:
# Write a Python program to calculate and display the interest on a loan amount (Rupees) using
# the formula:
# interest=(principal * rate of interest * time)/100

p=int(input("Enter Principal: "))
r=float(input("Enter Rate of interest: "))
t=int(input("Enter Timer in years: "))
si=float(
    (p*t*r)/100
)
print("The interest is ",si)



# Question 2:
# Write a python program to find out if a given year is a leap year or not. Any year which is
# divisible by 4 and not by 100 are leap years. Otherwise, any year which is divisible by 400 is
# also a leap year.

year=int(input("Enter the year: "))
if(year % 400==0) or (year %4 ==0 and year % 100 !=0 ):
    print("The year ", year,"is a leap year")
else:
    print("The year", year,"is not a leap year")


# Write a python program to print the given pattern
# *****
# ****
# ***
# **
# *
# and the output is verified.


for i in range(5,0,-1):
    print("*" * i)

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






