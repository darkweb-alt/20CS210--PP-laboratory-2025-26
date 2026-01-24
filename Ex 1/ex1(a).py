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


