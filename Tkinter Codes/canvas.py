from tkinter import *

root = Tk()
root.title("Hiii, this is canvas example: ")

canvas = Canvas(root, width=200, height=60)
canvas.pack()

y = 30
canvas.create_line(0, y, 200, y)
root.mainloop()