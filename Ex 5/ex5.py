# ---------------------------------------------------------
# Course Registration System using Tkinter
# ---------------------------------------------------------
# Importing required modules
import tkinter as tk
from tkinter import messagebox
# Function to submit the form
def submit_form():
    # Getting values from entry fields
    first_name = entry_first.get()
    last_name = entry_last.get()
    email = entry_email.get()
    phone = entry_phone.get()
    birthdate = entry_birth.get()
    gender = gender_var.get()
    address = entry_address.get()
    city = entry_city.get()
    state = entry_state.get()
    postal = entry_postal.get()
    country = entry_country.get()

    # Display confirmation message
    messagebox.showinfo("Registration Successful",
                        f"Student {first_name} {last_name} registered successfully!")

# Creating main window
root = tk.Tk()
root.title("Course Registration System")
root.geometry("500x650")

# Heading
tk.Label(root, text="Course Registration Form",
         font=("Arial", 16, "bold")).pack(pady=10)

# First Name
tk.Label(root, text="First Name").pack()
entry_first = tk.Entry(root, width=40)
entry_first.pack()

# Last Name
tk.Label(root, text="Last Name").pack()
entry_last = tk.Entry(root, width=40)
entry_last.pack()

# Email
tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack()

# Phone
tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()

# Birthdate
tk.Label(root, text="Birthdate (DD/MM/YYYY)").pack()
entry_birth = tk.Entry(root, width=40)
entry_birth.pack()

# Gender
tk.Label(root, text="Gender").pack()
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

# Address
tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root, width=40)
entry_address.pack()

# City
tk.Label(root, text="City").pack()
entry_city = tk.Entry(root, width=40)
entry_city.pack()

# State/Province/Region
tk.Label(root, text="State/Province/Region").pack()
entry_state = tk.Entry(root, width=40)
entry_state.pack()

# Postal Zip
tk.Label(root, text="Postal Zip Code").pack()
entry_postal = tk.Entry(root, width=40)
entry_postal.pack()
# Country
tk.Label(root, text="Country").pack()
entry_country = tk.Entry(root, width=40)
entry_country.pack()
# Submit Button
tk.Button(root, text="Submit", command=submit_form,
          bg="green", fg="white").pack(pady=15)

# Run the application
root.mainloop()