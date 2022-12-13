BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import*
import random
current_card=None
timer=None
fr_words=[]
en_words = []

try:
    file = pandas.read_csv("./words_to_learn.csv")
    list = file.to_dict(orient="records")
    # print(list) ### aici vezi lista intreaba de carti ramase

except:
    file = pandas.read_csv("./data/french_words.csv")
    list = file.to_dict(orient="records")

def remove_card():
    global current_card,list

    list.remove(current_card)
    words_to_learn=pandas.DataFrame(list)
    words_to_learn.to_csv("./words_to_learn.csv",index=False)

    if not len(list)==0:
        generate_word_card()
    else:
        canvas.itemconfig(canvas_title, text="END")
        canvas.itemconfig(canvas_word, text="No more words")
        file = pandas.read_csv("./data/french_words.csv")
        list = file.to_dict(orient="records")
        window.after_cancel(timer)

def generate_word_card():
    global current_card
    global timer
    global list

    window.after_cancel(timer)

    # print(current_card["French"])
    # print(current_card["English"])

    current_card = random.choice(list)
    print(f'Current card: {current_card}')
    print(f'Cards to learn in deck : {len(list)}')
    canvas.itemconfig(cover, image=card_back)
    canvas.itemconfig(canvas_title,fill="white",text="French")
    canvas.itemconfig(canvas_word,fill="white",text=current_card["French"])

    timer=window.after(3000, turn_card)

def turn_card():
    global current_card
    canvas.itemconfig(cover,image=card_front)
    canvas.itemconfig(canvas_title,fill="black",text="English")
    canvas.itemconfig(canvas_word,fill="black",text=current_card["English"])

window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


card_back=PhotoImage(file="./images/card_back.png")
card_front=PhotoImage(file="./images/card_front.png")
wrong=PhotoImage(file="./images/wrong.png")
right=PhotoImage(file="./images/right.png")

right_button=Button(highlightthickness=0,image=right,command=remove_card)
right_button.grid(column=1,row=1)

wrong_button=Button(image=wrong,highlightthickness=0,command=generate_word_card)
wrong_button.grid(column=0,row=1)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
cover=canvas.create_image(400,260,image=card_back)
canvas.grid(column=0,columnspan=2,row=0,)
canvas_title=canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), tags="title")
canvas_word=canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), tags=("word"))

timer=window.after(3000, turn_card)
generate_word_card()

window.mainloop()
