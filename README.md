# AI_typing_trainer
Evan Anderson
USU CS5890 Final Project

This program uses OpenAI's gpt-3.5-turbo. It requires the following dependencies:
- tkinter
- openai

You can install these using pip (or pip3):
```
pip install tkinter
```
```
pip install openai
```

After installing dependencies, change the text in api_key.txt to your API key. You can create an OpenAI API key at https://openai.com/blog/openai-api.

Run the following (or python3) to start the program:
```
python main.py
```

The theme of the window is determined by the OS, so if you are experiencing issues with the theme (white text over white background or black text over black background) change the "theme" variable on line 10 of main.py to either "light" or "dark".