import tkinter as tk

root = tk.Tk()
v = tk.IntVar()

tk.Radiobutton(root, text="A", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="B", variable=v, value=2).pack(anchor=tk.W)
root.mainloop()