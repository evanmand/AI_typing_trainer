from tkinter import *
from tkinter import ttk
from openai import OpenAI
import time

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

# Create dictionary of characters (rather, their decimal values) to track how often they are missed
letters = {}
i = 33 # Start at char 33 (!), end at 126 (~)
while i <= 126:
    letters[str(i)] = 0
    i += 1

def keystroke(event):
    global current_index
    global current_text
    global user_input
    global prompt_text
    global started
    global correct_count
    global incorrect_count
    global start_time
    global end_time

    key = event.char
    print(f"'{key}' key pressed")

    # If key is shift, alt, etc... do nothing
    if key == '':
        return

    if started:
        # global started
        started = False # This boolean helps erase starting text
        user_input = ''
        start_time = time.time() # Time starts when first key is pressed

    # Check if typed character is correct
    print(key)
    print(prompt_text[current_index])
    print(key == prompt_text[current_index])
    if key == prompt_text[current_index]: # Correct key
        user_input = user_input + key
        current_text.destroy()
        current_text = create_label(user_input, 0, 'black')
        current_index += 1
        correct_count += 1
    else: # Wrong key
        user_input = user_input
        current_text.destroy()
        current_text = create_label(user_input, 0, 'red')
        if ord(key) in letters:
            letters[key] = letters[key] + 1
        incorrect_count += 1

    if current_index == len(prompt_text): # User has reached end of text
        end_time = time.time()
        end_screen()


root.bind('<Key>', keystroke)

def main():
    # Clear frame
    for widgets in frm.winfo_children():
        widgets.destroy()

    global start_time
    global end_time
    start_time = ''
    end_time = ''

    global current_index
    current_index = 0

    global current_text
    global user_input
    global prompt_text

    global started
    started = True

    global correct_count
    global incorrect_count
    correct_count = 0
    incorrect_count = 0

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

def end_screen():
    for widgets in frm.winfo_children():
        widgets.destroy()
    speed = "WPM: " + str(round(((len(prompt_text) / 5) / ((end_time - start_time)/ 1000) / 60)))
    print(correct_count)
    print(incorrect_count)
    acc_string = "Accuracy: " + str(round(100 * (correct_count / (incorrect_count + correct_count)))) + "%"
    create_label("Well done!", 0, 'black')
    create_label(speed, 1, 'black')
    create_label(acc_string, 2, 'black')
    restart = ttk.Button(frm, text="Restart", command=main)
    restart.grid()
    exit = ttk.Button(frm, text="Quit", command=quit)
    exit.grid()

main()
root.mainloop()