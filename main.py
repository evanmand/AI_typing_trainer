from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

string_thing = "QWer"

def create_label(input_text):
    input_text
    text = ttk.Label(frm, text=input_text,font=("Arial", 25)).grid(column=0, row=0)

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

def keystroke(event):
    global string_thing
    key = event.char
    print(f"'{key}' key pressed")
    # clear_frame()
    # string_thing = string_thing + key
    # string_thing = string_thing + key
    temp_string = string_thing + key
    string_thing = "BB"
    create_label(temp_string)


    # text = ttk.Label(frm, text=key,font=("Arial", 25)).grid(column=0, row=0)
root.bind('<Key>', keystroke)

root.attributes('-fullscreen', True)
# text_var = prompt_text
root.mainloop()