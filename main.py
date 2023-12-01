from tkinter import *
from tkinter import ttk
from openai import OpenAI

f = open("api_key.txt", "r")
key = f.readline()
f.close()

client = OpenAI(
    api_key=key,
)

root = Tk()
root.title("Evan's Typing Tutor") 
root.grid_columnconfigure(0, weight = 0)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 0)
root.grid_rowconfigure(1, weight = 1)
root.attributes('-fullscreen', False)

frm = ttk.Frame(root, padding=10)
frm.grid()

def create_label(input_text, row):
    label = ttk.Label(frm, text=input_text, font=("Arial", 25), wraplength=1000, justify=LEFT)
    label.grid(column = 0,
               row = row,
               sticky = NW)

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

user_input = ""

def keystroke(event):
    global user_input
    key = event.char
    print(f"'{key}' key pressed")
    # clear_frame()
    # string_thing = string_thing + key
    # string_thing = string_thing + key
    user_input = user_input + key
    create_label(user_input, 0)

root.bind('<Key>', keystroke)

def main():
    # Clear frame
    for widgets in frm.winfo_children():
        widgets.destroy()

    global user_input
    user_input = ''

    # Generate new prompt text from ChatGPT
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    print(completion.choices[0].message)
    prompt_text = "ststs"
    create_label("", 10) # Placeholder before user starts typing
    create_label(prompt_text, 1)
    restart = ttk.Button(frm, text="Restart", command=main)
    restart.grid()
    exit = ttk.Button(frm, text="Quit", command=quit)
    exit.grid()

    
main()
root.mainloop()