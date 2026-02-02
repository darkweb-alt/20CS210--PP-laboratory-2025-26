# 1. A university library management system stores book details in a Python dictionary named books, where the is the book_id and the is another dictionary containing title, author, and available_copies.
# During end-of-day processing, the librarian performs the following operations:
# Creates a backup of the current books record before making changes.
# Initializes a new dictionary of default categories ("Science", "Arts", "Engineering") with an initial count of 0.
# Safely retrieves the number of available copies for a given book_id without causing an error if the ID does not exist.
# Displays all book IDs with their corresponding details for reporting.
# Extracts only the list of book IDs and only the list of available copy counts for analytics.
# Removes a book record when a book is permanently discarded.
# Removes the most recently added book entry during a data correction step.
# Ensures a missing book category is added with a default value if it does not already exist.
# Merges a newly received shipment of books (stored in another dictionary) into the existing books dictionary.
# Finally, clears all records at the end of the academic year.
# Identify and justify the appropriate Python dictionary methods (clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), values(), update()) that should be used for each of the above operations, and explain each method is suitable in the given scenario.


# Initial books dictionary
books = {
    101: {"title": "Physics", "author": "Einstein", "available_copies": 5},
    102: {"title": "Chemistry", "author": "Curie", "available_copies": 3},
    103: {"title": "Mathematics", "author": "Newton", "available_copies": 4}
}

# 1. Backup current books
backup_books = books.copy()  # copy() creates a shallow copy

# 2. Initialize new categories with count 0
categories = dict.fromkeys(["Science", "Arts", "Engineering"], 0)

# 3. Safely retrieve available copies
book_id = 102
copies = books.get(book_id, {}).get("available_copies", 0)
print(f"Book {book_id} has {copies} copies")

# 4. Display all book IDs with details
for bid, details in books.items():
    print(f"Book ID: {bid}, Details: {details}")

# 5. Extract only book IDs and only available copies
book_ids = list(books.keys())
available_copies = [details["available_copies"] for details in books.values()]

# 6. Remove a permanently discarded book
books.pop(103)  # removes book with ID 103

# 7. Remove most recently added book
books.popitem()  # removes last inserted book (Python 3.7+)

# 8. Add missing category safely
categories.setdefault("Mathematics", 0)  # adds if missing

# 9. Merge newly received shipment
new_books = {
    104: {"title": "Biology", "author": "Darwin", "available_copies": 6},
    105: {"title": "History", "author": "Herodotus", "available_copies": 2}
}
books.update(new_books)

# 10. Clear all records at end of year
books.clear()
categories.clear()
