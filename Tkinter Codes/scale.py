from tkinter import *

master = Tk()

# Vertical scale
vertical_scale = Scale(master, from_=0, to=42)
vertical_scale.pack()

# Horizontal scale
horizontal_scale = Scale(master, from_=0, to=200, orient=HORIZONTAL)
horizontal_scale.pack()

master.mainloop()