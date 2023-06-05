from tkinter import *
import pandas as pd
import random
new_word = {}
# ---------------------------- DATA ------------------------------- #
try:
    df = pd.read_csv("data/data_to_learn.csv.csv")
except FileNotFoundError:
    df = pd.read_csv("data/korean_words.csv")

# orient=records is for pairing records in a dictionary
words = df.to_dict(orient="records")


# ---------------------------- FUNCTIONS ------------------------------- #
def update_learning_words():
    global new_word
    words.remove(new_word)
    dataframe_to_learn = pd.DataFrame(words)
    dataframe_to_learn.to_csv('data/data_to_learn.csv', index=False)
    next_card()


def next_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(words)
    print(new_word)
    canvas.itemconfig(canvas_img, image=img_front_card)
    canvas.itemconfig(title_text, text="Korean", fill="black")
    canvas.itemconfig(word_text, text=new_word['Korean'], fill="black")
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    global new_word
    canvas.itemconfig(canvas_img, image=img_back_card)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=new_word['English'], fill="white")


# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy Language App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(5000, func=flip_card)

# Images
img_front_card = PhotoImage(file="images/card_front.png")
img_back_card = PhotoImage(file="images/card_back.png")
img_wrong_button = PhotoImage(file="images/wrong.png")
img_right_button = PhotoImage(file="images/right.png")

# Canvas
canvas = Canvas(width=800, height=526)
# Note: canvas contents are relative to the canvas size
canvas_img = canvas.create_image(400, 263, image=img_front_card)
title_text = canvas.create_text(400, 150, text="Korean", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
button_wrong = Button(image=img_wrong_button, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

button_right = Button(image=img_right_button, highlightthickness=0, command=update_learning_words)
button_right.grid(row=1, column=1)
button_right.grid(row=1, column=1)

next_card()
window.mainloop()
