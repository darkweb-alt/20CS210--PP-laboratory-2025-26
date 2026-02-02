
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


# Initial sets as per question
registered_students = {101, 102, 103, 104}
workshop_A = {101, 103}
workshop_B = {102, 104}
volunteers = {101, 105}

print("INITIAL SETS:")
print(f"Registered Students: {registered_students}")
print(f"Workshop A: {workshop_A}")
print(f"Workshop B: {workshop_B}")
print(f"Volunteers: {volunteers}")
print("-" * 40)

# 1. Add new student registration dynamically (add())
registered_students.add(105)
print("1. ADDED NEW STUDENT (add()):")
print(f"   Updated registered: {registered_students}")

# 2. Safe backup (copy())
backup_registered = registered_students.copy()
print("\n2. BACKUP CREATED (copy()):")
print(f"   Backup: {backup_registered}")

# 3. Registered but didn't attend Workshop A (difference())
not_in_A = registered_students.difference(workshop_A)
print("\n3. NOT IN WORKSHOP A (difference()):")
print(f"   {not_in_A}")

# 4. Remove cancelled students (difference_update())
registered_students.difference_update({104})  # Student 104 cancelled
print("\n4. CANCELLED STUDENTS REMOVED (difference_update()):")
print(f"   Updated registered: {registered_students}")

# 5. Safe remove without error (discard())
registered_students.discard(999)  # Safe even if 999 doesn't exist
print("\n5. SAFE REMOVE (discard()):")
print(f"   After discard(999): {registered_students}")

# 6. Check if workshops have no common students (isdisjoint())
disjoint_check = workshop_A.isdisjoint(workshop_B)
print("\n6. WORKSHOPS DISJOINT? (isdisjoint()):")
print(f"   Workshop A & B disjoint: {disjoint_check}")

# 7. All volunteers registered? (issubset())
all_volunteers_registered = volunteers.issubset(registered_students)
print("\n7. VOLUNTEERS REGISTERED? (issubset()):")
print(f"   All volunteers registered: {all_volunteers_registered}")

# 8. Students who attended at least one workshop (union())
all_workshop_students = workshop_A.union(workshop_B)
print("\n8. ALL WORKSHOP STUDENTS (union()):")
print(f"   {all_workshop_students}")

# 9. Keep only common attendees (intersection_update())
workshop_A.intersection_update(workshop_B)
print("\n9. COMMON ATTENDEES ONLY (intersection_update()):")
print(f"   Workshop A updated: {workshop_A}")

# 10. Remove random volunteer (pop())
removed_volunteer = volunteers.pop()
print("\n10. RANDOM VOLUNTEER REMOVED (pop()):")
print(f"    Removed: {removed_volunteer}")
print(f"    Remaining volunteers: {volunteers}")

# 11. Immutable final groups (frozenset())
final_groups = frozenset({101, 102, 103})
print("\n11. IMMUTABLE FINAL GROUPS (frozenset()):")
print(f"    {final_groups} (Cannot be modified)")

# 12. Students in only one workshop (symmetric_difference())
only_one_workshop = workshop_A.symmetric_difference(workshop_B)
print("\n12. ONLY ONE WORKSHOP (symmetric_difference()):")
print(f"    {only_one_workshop}")

# 13. Merge all workshops (union())
all_participants = workshop_A.union(workshop_B)
print("\n13. ALL PARTICIPANTS (union()):")
print(f"    {all_participants}")

# 14. Clear all temporary data (clear())
registered_students.clear()
workshop_A.clear()
workshop_B.clear()
volunteers.clear()
print("\n14. ALL DATA CLEARED (clear()):")
print(f"    Registered: {registered_students}")
print(f"    Workshops: {workshop_A}, {workshop_B}")
print(f"    Volunteers: {volunteers}")

print("\n" + "="*50)
print("🎉 ALL 14 SET OPERATIONS COMPLETED SUCCESSFULLY!")
print("="*50)