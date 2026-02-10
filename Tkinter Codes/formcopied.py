import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Course Registration Form")
root.geometry("600x550")
# root.configure(bg="#f2f2f2") COmment to explore it 

frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.pack(padx=20, pady=20, fill="both", expand=True)
# Frame is also commented to be used later: 

# Title
tk.Label(
    frame, text="Course Registration Form",
    font=("Arial", 18, "bold"), bg="white"
).grid(row=0, column=0, columnspan=3, pady=(0, 15))

def label(text, r, c):
    tk.Label(frame, text=text, bg="white").grid(row=r, column=c, sticky="w", pady=5)

def entry(r, c):
    e = ttk.Entry(frame, width=25)
    e.grid(row=r+1, column=c, padx=5)
    return e

# First / Last name
label("First name *", 1, 0)
label("Last name *", 1, 1)
entry(1, 0)
entry(1, 1)

# Email / Phone
label("Email *", 3, 0)
label("Your phone", 3, 1)
entry(3, 0)
entry(3, 1)

# Birth date / Gender
label("Birth Date *", 5, 0)
label("Gender *", 5, 1)
entry(5, 0)

gender = ttk.Combobox(frame, values=["Male", "Female", "Other"], width=23)
gender.grid(row=6, column=1, padx=5)

# Address
label("Address", 7, 0)
addr = ttk.Entry(frame, width=55)
addr.grid(row=8, column=0, columnspan=2, pady=5)

# City / State / Zip
label("City", 9, 0)
label("State/Prov/Region", 9, 1)
label("Postal/Zip", 9, 2)

entry(9, 0)
entry(9, 1)
entry(9, 2)

# Country
label("Country", 11, 0)
country = ttk.Combobox(
    frame,
    values=["India", "USA", "UK", "Canada", "Other"],
    width=52
)
country.grid(row=12, column=0, columnspan=3, pady=5)

# Submit button
submit = ttk.Button(frame, text="SUBMIT")
submit.grid(row=13, column=2, pady=20, sticky="e")

root.mainloop()
