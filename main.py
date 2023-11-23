from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def create_label():
    prompt_text = "The quick brown fox jumps over the lazy dog"
    text_var = prompt_text
    text = ttk.Label(frm, text=text_var,font=("Arial", 25)).grid(column=0, row=0)
   

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

def keystroke(event):
    key = event.char
    print(f"'{key}' key pressed")
    # clear_frame()
    create_label()
    # text = ttk.Label(frm, text=key,font=("Arial", 25)).grid(column=0, row=0)
root.bind('<Key>', keystroke)

root.attributes('-fullscreen', True)
# text_var = prompt_text
root.mainloop()