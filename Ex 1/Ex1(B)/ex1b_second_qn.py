# 2. An e-commerce company stores (Product ID, Product Name, Category, Price) as a to ensure the data remains . Multiple such tuples are stored and analyzed for reporting purposes.
# Using appropriate , perform the following tasks:
# Create a tuple to store product details.
# Access and display specific elements from the tuple using indexing.
# Count how many times a particular category appears in a tuple of categories.
# Find the index of a given product name in a tuple.
# Demonstrate tuple slicing to display a subset of product details.
# Convert the tuple into a list to update the price and convert it back to a tuple.
# Explain why tuples are preferred over lists for storing fixed product records.
# Write a Python program to implement the above operations using tuples and justify the use of tuples in this scenario.

# Initial tuple for product details: (Product ID, Name, Category, Price)
product = (101, "Laptop", "Electronics", 55000)

# 1️⃣ Access elements using indexing
print("Product Name:", product[1])
print("Price:", product[3])

# 2️⃣ Count occurrences of a category in a tuple of categories
categories = ("Electronics", "Clothing", "Electronics", "Toys")
electronics_count = categories.count("Electronics")
print("Electronics appears:", electronics_count, "times")

# 3️⃣ Find index of a product name in a tuple
product_names = ("Laptop", "Shirt", "Toy Car")
index_laptop = product_names.index("Laptop")
print("Laptop is at index:", index_laptop)

# 4️⃣ Tuple slicing
subset = product[1:3]  # Name and Category
print("Subset of product details:", subset)

# 5️⃣ Convert tuple to list, update price, convert back to tuple
product_list = list(product)
product_list[3] = 60000
product = tuple(product_list)
print("Updated product tuple:", product)

# 6️⃣ Why tuples are preferred
print("Tuples are immutable, so product records remain safe and unchanged accidentally.")
