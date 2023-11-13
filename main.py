from tkinter import *
from tkinter import ttk

def keystroke(event):
    key = event.char
    print(f"'{key}' key pressed")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

prompt_text = "The quick brown fox jumps over the lazy dog"

root.bind('<Key>', keystroke)
text_var = prompt_text
text = ttk.Label(frm, text=text_var,font=("Arial", 25)).grid(column=0, row=0)
root.attributes('-fullscreen', True)
text_var = prompt_text
root.mainloop()