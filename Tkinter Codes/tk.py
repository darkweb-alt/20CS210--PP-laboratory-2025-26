import tkinter as tk

root = tk.Tk()
# root.title("Counting Seconds")
label = tk.Label(root, text="Pitambar")
# label.pack()


tk.Label(root, text="First Name").grid(row=0, column=0)
tk.Label(root, text="Last Name").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
button = tk.Button(root, text="Submit", width=25, command=root.destroy)
# button.pack()
root.mainloop()