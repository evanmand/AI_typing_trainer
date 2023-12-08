from tkinter import *
from tkinter import ttk
from openai import OpenAI
import time

f = open("api_key.txt", "r")
key = f.readline()
f.close()

theme = 'dark' # Change dark/light mode
if theme == 'light':
    text_color = 'black'
else:
    text_color = 'white'

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

global first_round
global most_missed_letter
most_missed_letter = ''
first_round = True

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
    global incorrect_count
    global start_time
    global end_time
    global most_missed_letter

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
        current_text = create_label(user_input, 0, text_color)
        current_index += 1
    else: # Wrong key
        user_input = user_input
        current_text.destroy()
        current_text = create_label(user_input, 0, 'red')
        if str(ord(key)) in letters:
            letters[str(ord(key))] = letters[str(ord(key))] + 1
        incorrect_count += 1

    if current_index == len(prompt_text): # User has reached end of text
        end_time = time.time()
        end_screen()


root.bind('<Key>', keystroke)

def main():
    global first_round

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

    global incorrect_count
    incorrect_count = 0

    user_input = 'Start typing the words below!'
    current_text = create_label(user_input, 0, 'grey')

    # Generate new prompt text from ChatGPT
    print("Generating content, this will take a short moment...")
    print(most_missed_letter)
    if first_round:
        message = {"role": "user", "content": "Hey ChatGPT please write a paragraph with less than 50 words about something random."}
    else:
        message = {"role": "user", "content": "Hey ChatGPT please write a paragraph with less than 50 words about something random using a lot of the letter " + chr(int(most_missed_letter)) + "."}
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[message]
    )
    content = completion.choices[0].message.content
    content = content.split('\n')
    prompt_text = content[-1]

    create_label("", 10, text_color) # Placeholder before user starts typing
    create_label("\n" + prompt_text, 1, text_color)

    restart = ttk.Button(frm, text="Restart", command=main)
    restart.grid()
    exit = ttk.Button(frm, text="Quit", command=quit)
    exit.grid()

def end_screen():
    global most_missed_letter
    global first_round
    most_missed_letter
    first_round = False

    # Find most missed letter
    most_missed_letter = ''
    most_misses = 0
    for char in letters:
        if letters[char] >= most_misses:
            most_misses = letters[char]
            most_missed_letter = char
    letters[most_missed_letter] = 0 # Reset missed letter

    for widgets in frm.winfo_children():
        widgets.destroy()
    print(len(prompt_text))

    words_count = len(prompt_text)
    elapsed_time = (end_time - start_time) * 1000 # Convert from ms to seconds
    speed = "WPM: " + str(round((words_count/elapsed_time) * 60 * 100))

    print("Correct " + str(len(prompt_text) - incorrect_count))
    print("incorrect " + str(incorrect_count))

    acc_string = "Accuracy: " + str(round(100 * ((len(prompt_text) - incorrect_count) / (incorrect_count + len(prompt_text) - incorrect_count)))) + "%"
    create_label("Well done!", 0, text_color)
    create_label(speed, 1, text_color)
    create_label(acc_string, 2, text_color)
    restart = ttk.Button(frm, text="Restart", command=main)
    restart.grid()
    exit = ttk.Button(frm, text="Quit", command=quit)
    exit.grid()

main()
root.mainloop()