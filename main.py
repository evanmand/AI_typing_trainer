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

def create_label(input_text, row, color):
    label = ttk.Label(frm, text=input_text, font=("Arial", 25), wraplength=1000, justify=LEFT, foreground=color)
    label.grid(column = 0,
               row = row,
               sticky = NW)
    return label

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

def keystroke(event):
    global current_index
    global current_text
    global user_input
    global prompt_text
    global started

    key = event.char
    print(f"'{key}' key pressed")

    # If key is shift, alt, etc... do nothing
    if key == '':
        return

    if started:
        # global started
        started = False # This boolean helps erase starting text
        user_input = ''

    # Check if typed character is correct
    print(key)
    print(prompt_text[current_index])
    print(key == prompt_text[current_index])
    if key == prompt_text[current_index]:
        user_input = user_input + key
        current_text.destroy()
        current_text = create_label(user_input, 0, 'black')
        current_index += 1
    else:
        user_input = user_input
        current_text.destroy()
        current_text = create_label(user_input, 0, 'red')


root.bind('<Key>', keystroke)

letters = {
        '65': 0,
        '66': 0,
        '67': 0,
        '68': 0,
        '69': 0,
        '70': 0,
        '71': 0,
        '72': 0,
        '73': 0,
        '74': 0,
        '75': 0,
        '76': 0,
        '77': 0,
        '78': 0,
        '79': 0,
        '80': 0,
        '81': 0,
        '82': 0,
        '83': 0,
        '84': 0,
        '85': 0,
        '86': 0,
        '87': 0,
        '88': 0,
        '89': 0,
        '90': 0,
        '91': 0,
        '92': 0,
        '93': 0,
        '94': 0,
        '95': 0,
        '96': 0,
        '97': 0,
        '98': 0,
        '99': 0,
        '100': 0,
        '101': 0,
        '102': 0,
        '103': 0,
        '104': 0,
        '105': 0,
        '106': 0,
        '107': 0,
        '108': 0,
        '109': 0,
        '110': 0,
        '111': 0,
        '112': 0,
        '113': 0,
        '114': 0,
        '115': 0,
        '116': 0,
        '117': 0,
        '118': 0,
        '119': 0,
        '120': 0,
        '121': 0,
        '122': 0
    }
def main():
    # Clear frame
    for widgets in frm.winfo_children():
        widgets.destroy()

    global current_index
    current_index = 0

    global current_text
    global user_input
    global prompt_text

    global started
    started = True

    user_input = 'Start typing the words below!'
    current_text = create_label(user_input, 0, 'grey')

    # Generate new prompt text from ChatGPT
    print("Generating content, this will take a short moment...")
    # completion = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "user", "content": "Hey ChatGPT please write a paragraph about something random. Don't start with something like \"here's a paragraph about...\""}
    #         # {"role": "user", "content": "Hey ChatGPT please write a paragraph about something random using a lot of the letter 'z'."}
    #     ]
    # )
    # content = completion.choices[0].message.content
    # content = content.split('\n')
    # prompt_text = content[-1]
    prompt_text = "Test words hehehehe."


    # print(type(prompt_text))
    # print(prompt_text)
    # for char in prompt_text:
    #     if str(ord(char)) in letters:
    #         letters[str(ord(char))] = letters[str(ord(char))] + 1
    # letters['iteration'] = letters['iteration'] + 1

    create_label("", 10, 'black') # Placeholder before user starts typing
    create_label(prompt_text, 1, 'black')
    # print("Iteration: " + str(letters['iteration']))
    # print(letters)
    restart = ttk.Button(frm, text="Restart", command=main)
    restart.grid()
    exit = ttk.Button(frm, text="Quit", command=quit)
    exit.grid()

main()
root.mainloop()