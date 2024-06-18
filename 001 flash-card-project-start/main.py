from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
words_learned = []
word = ""

# -----------------------------------PARSING DATA-------------------------------------------------#
df = pd.read_csv("./data/french_words.csv")


# ----------------------------------FUNCTIONS-------------------------------------------------#

def update_display():
    global word
    word_is_unknown = True
    while word_is_unknown:
        word = random.choice(df["French"])
        if word not in words_learned:
            word_is_unknown = False

    translation = df[df["French"] == word]["English"].values[0]

    canvas.itemconfig(image, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word, fill="black")

    screen.after(3000, show_translation, translation)


def show_translation(translation):
    canvas.itemconfig(image, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=translation, fill="white")


def click_yes():
    global word
    words_learned.append(word)
    update_display()


# -----------------------------------GUI-------------------------------------------------#
screen = Tk()
screen.title("Flashy")

screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Insert images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
correct_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="language", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
correct_button = Button(image=correct_img, highlightthickness=0, command=click_yes)
correct_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=update_display)
wrong_button.grid(column=0, row=1)

french_label = Label()
french_label.grid()

update_display()

screen.mainloop()
