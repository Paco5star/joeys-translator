
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Joeys Translator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

content_frame = Frame(window, bg=BACKGROUND_COLOR)
content_frame.grid(row=0, column=0, columnspan=2)

header = Label(content_frame, text="Joey's Translator", font=("ariel", 24, "bold"), bg=BACKGROUND_COLOR)
header.pack()

front_card = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_card)
word_l = canvas.create_text(400, 263, text="word", font=("ariel", 60, "bold"))
title_l = canvas.create_text(400, 150, text="Dutch", font=("ariel", 40, "italic"))
old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")

def generate():
    global current_card
    current_card = choice(dict)
    canvas.itemconfig(title_l, text="Dutch", fill="black")
    canvas.itemconfig(word_l, text=current_card["Dutch"], fill="black")
    canvas.itemconfig(canvas_image, image=old_image)
    print(current_card["English"])

def flip_card():
    global current_card

    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(title_l, text="English", fill="white")
    canvas.itemconfig(word_l, text=current_card["English"], fill="white")

def is_known():
    dict.remove(current_card)
    data1 = pandas.DataFrame(dict)
    data1.to_csv("words_to_learn.csv", index=False)
    generate()

def add_word():
    new_word = entry.get()
    new_translation = entry_translation.get()
    dict.append({"Dutch": new_word, "English": new_translation})
    entry.delete(0, END)
    entry_translation.delete(0, END)

canvas.grid(row=0, column=0, columnspan=2)

my_image_no = PhotoImage(file="images/wrong.png")
no_but = Button(image=my_image_no, command=generate, highlightthickness=0, bg=BACKGROUND_COLOR)
no_but.config(padx=50)
no_but.grid(row=1, column=0)
my_image_yes = PhotoImage(file="images/right.png")
yes_but = Button(image=my_image_yes, command=is_known, highlightthickness=0, bg=BACKGROUND_COLOR)
yes_but.grid(row=1, column=1)

entry = Entry(window)
entry.grid(row=2, column=0)
entry_translation = Entry(window)
entry_translation.grid(row=2, column=1)

add_button = Button(window, text="Add Word", command=add_word, highlightthickness=0, bg=BACKGROUND_COLOR)
add_button.grid(row=3, column=0, columnspan=2)

flip_button = Button(window, text="Flip Card", command=flip_card, highlightthickness=0, bg=BACKGROUND_COLOR)
flip_button.grid(row=4, column=0, columnspan=2)

dict = {}
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("dutch_words.csv")
    dict = original_data.to_dict(orient="records")
else:
    dict = data.to_dict(orient="records")
print(dict)
current_card = choice(dict)


generate()

window.mainloop()