
# 2. A college is organizing a , and different student participation details are stored using Python .
# registered_students contains the roll numbers of all students registered for the fest.
# workshop_A and workshop_B contain roll numbers of students attending two different workshops.
# volunteers contains roll numbers of student volunteers.
# During event management, the coordinator needs to:
# Add new student registrations dynamically.
# Create a safe backup of the registered students list.
# Identify students who registered for the fest but did attend a specific workshop.
# Update the main registration list by removing students who cancelled participation.
# Remove a student from a set without raising an error if the student is absent.
# Check whether two workshops have .
# Verify whether all volunteers are part of the registered students list.
# Determine students who attended .
# Update the workshop list to keep only common attendees.
# Remove a random volunteer for reassignment.
# Ensure some student groups remain immutable after final submission.
# Identify students who attended .
# Merge participants from multiple workshops into a single list.
# Clear all temporary data after the fest concludes.
# Choose and justify the appropriate Python (add(), clear(), copy(), difference(), difference_update(), discard(), frozenset(), intersection(), intersection_update(), isdisjoint(), issubset(), issuperset(), pop(), remove(), symmetric_difference(), symmetric_difference_update(), union(), update()) for each of the above operations. 


# Initial sets
registered_students = {101, 102, 103, 104}
workshop_A = {101, 103}
workshop_B = {102, 104}
volunteers = {101, 105}

# 1. Add new student
registered_students.add(105)

# 2. Backup
backup_registered = registered_students.copy()

# 3. Students who registered but didn't attend A
not_in_A = registered_students.difference(workshop_A)

# 4. Remove cancelled students
registered_students.difference_update({104})  # remove student 104

# 5. Remove a student safely
registered_students.discard(999)  # no error even if 999 not present

# 6. Check if two workshops are disjoint
disjoint_check = workshop_A.isdisjoint(workshop_B)

# 7. Verify volunteers are part of registered students
all_volunteers_registered = volunteers.issubset(registered_students)

# 8. Students who attended at least one workshop
all_workshop_students = workshop_A.union(workshop_B)

# 9. Keep only common attendees
workshop_A.intersection_update(workshop_B)

# 10. Remove random volunteer
removed_volunteer = volunteers.pop()

# 11. Immutable student groups
final_groups = frozenset({101, 102, 103})

# 12. Students attended only one workshop
only_one_workshop = workshop_A.symmetric_difference(workshop_B)

# 13. Merge multiple workshops
all_participants = workshop_A.union(workshop_B)

# 14. Clear temporary data
registered_students.clear()
workshop_A.clear()
workshop_B.clear()
volunteers.clear()
