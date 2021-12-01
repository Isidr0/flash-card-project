from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/spanish_words.csv")

words = df.to_dict(orient="records")
current_card = {}

def random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(current_language, text="Spanish", fill="black")
    canvas.itemconfig(current_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(current_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(current_language, text="English", fill="white")
    canvas.itemconfig(current_word, text=current_card["English"], fill="white")
    canvas.itemconfig(current_image, image=card_back_image)


def known_card():
    random_word()
    words.remove(current_card)
    words_to_learn = pandas.DataFrame(words)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    print(len(words))



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Define images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Front Card
current_image = canvas.create_image(400, 260, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
current_language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
current_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))


# Buttons
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_card)
right_button.grid(row=1, column=1)

random_word()

window.mainloop()