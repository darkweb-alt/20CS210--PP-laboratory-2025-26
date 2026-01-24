# Question 2:
# Write a python program to find out if a given year is a leap year or not. Any year which is
# divisible by 4 and not by 100 are leap years. Otherwise, any year which is divisible by 400 is
# also a leap year.

year=int(input("Enter the year: "))
if(year % 400==0) or (year %4 ==0 and year % 100 !=0 ):
    print("The year ", year,"is a leap year")
else:
    print("The year", year,"is not a leap year")