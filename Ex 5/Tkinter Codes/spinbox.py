from tkinter import *

root = Tk()
root.title("Spinbox Example")

spinbox = Spinbox(root, from_=0, to=10)
spinbox.pack()

root.mainloop()