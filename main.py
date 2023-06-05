from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy Language App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Images
img_front_card = PhotoImage(file="images/card_front.png")
img_wrong_button = PhotoImage(file="images/wrong.png")
img_right_button = PhotoImage(file="images/right.png")

# Canvas
canvas = Canvas(width=800, height=526)
# Note: canvas contents are relative to the canvas size
canvas.create_image(400, 263, image=img_front_card)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
button_wrong = Button(image=img_wrong_button, highlightthickness=0)
button_wrong.grid(row=1, column=0)

button_right = Button(image=img_right_button, highlightthickness=0)
button_right.grid(row=1, column=1)

window.mainloop()
