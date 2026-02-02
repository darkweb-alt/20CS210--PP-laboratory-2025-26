# 1. A college is developing a using Python lists to store student names. Initially, the list contains duplicate entries and needs to be managed dynamically throughout the semester.
# As part of the system, perform the following tasks using appropriate :
# Add a new student at the end of the list.
# Create a backup copy of the current list before making changes.
# Count how many times a particular student name appears in the list.
# Merge a list of transfer students with the existing list.
# Find the position of a given student in the list.
# Insert a priority student at a specified position.
# Remove the last enrolled student and display the removed name.
# Remove a specific student who has withdrawn from the course.
# Display the list in reverse order.
# Sort the student list alphabetically.
# Clear all records at the end of the semester.

# Initial list of students (with duplicates)
students = ["Pitambar", "Manoj", "Sunil", "Pitambar", "Dipak"]

# 1️⃣ Add a new student at the end
students.append("Siksha")
print("After adding Siksha:", students)

# 2️⃣ Create a backup copy
backup_students = students.copy()
print("Backup list:", backup_students)

# 3️⃣ Count occurrences of a particular student
count_Pitambar = students.count("Pitambar")
print("Pitambar appears:", count_Pitambar, "times")

# 4️⃣ Merge transfer students
transfer_students = ["Farid", "Ganesh"]
students.extend(transfer_students)
print("After merging transfers:", students)

# 5️⃣ Find the position of a student
position_Manoj = students.index("Manoj")
print("Manoj is at position:", position_Manoj)

# 6️⃣ Insert a priority student at a specific position
students.insert(2, "Hanmann")
print("After inserting Hanmann:", students)

# 7️⃣ Remove the last enrolled student and display
removed_student = students.pop()
print("Removed last student:", removed_student)

# 8️⃣ Remove a specific withdrawn student
students.remove("Sunil")
print("After removing Sunil:", students)

# 9️⃣ Display the list in reverse order
students.reverse()
print("Reversed list:", students)

# 10️⃣ Sort the list alphabetically
students.sort()
print("Sorted list:", students)

# 11️⃣ Clear all records at the end of semester
students.clear()
print("After clearing all records:", students)
