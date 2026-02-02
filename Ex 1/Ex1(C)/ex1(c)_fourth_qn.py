# 4. You are given a list of students with their marks in three subjects. Write a Python program that performs the following tasks:
# students = {
# "Anu": [78, 85, 90],
# "Bala": [60, 72, 68],
# "Charan": [88, 91, 84],
# "Divya": [45, 50, 40]
# }
# Write a function calculate_average(marks) that returns the average of a list of marks.
# Use a lambda function to determine whether a student has passed
# (average ≥ 50 → Pass, else → Fail).
# Create a new dictionary containing:
# Student name
# Average marks (rounded to 2 decimals)
# Result (Pass / Fail)
# Print the details of only passed students.
# Find and print the topper’s name (highest average).

students = {
    "Anu": [78, 85, 90],
    "Bala": [60, 72, 68],
    "Charan": [88, 91, 84],
    "Divya": [45, 50, 40]
}

# Function to calculate average
def calculate_average(marks):
    return sum(marks) / len(marks)

# Create new dictionary with averages and results
result_dict = {}
for student, marks in students.items():
    avg = round(calculate_average(marks), 2)
    result = "Pass" if (lambda x: x >= 50)(avg) else "Fail"
    result_dict[student] = {"Average": avg, "Result": result}

# Print only passed students
for student, info in result_dict.items():
    if info["Result"] == "Pass":
        print(student, info)

# Find topper
topper = max(result_dict.items(), key=lambda x: x[1]["Average"])
print("Topper:", topper[0])
