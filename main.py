from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!",font=("Arial", 25)).grid(column=0, row=0)
root.attributes('-fullscreen', True)
root.mainloop()
