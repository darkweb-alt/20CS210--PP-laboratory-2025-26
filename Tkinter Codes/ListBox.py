import tkinter as tk

root = tk.Tk()

lb = tk.Listbox(root)
lb.insert(1, "Python")
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "Any other")

lb.pack()
root.mainloop()