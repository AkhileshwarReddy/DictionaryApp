from tkinter import *
from tkinter.ttk import *
import requests as req
from bs4 import BeautifulSoup as bs

def getMeanings():
    frame = Frame(root,height=300, width=880).place(x = 10,y = 90)
    url = "https://en.oxforddictionaries.com/definition/" + word.get()

    try:
        r = req.get(url)
        soup = bs(r.content, "lxml")
    except:
        Label(frame, text="Oops!!! Check your internet connection.").place(x=350, y=160)
        return
    
    try:
        ul = soup.find_all("ul",class_="semb")
        meanings = ul[0].find_all("span",class_="ind")
    except:
        Label(frame,text="No Content About The Word \""+word.get()+"\"").place(x=350,y=160)
        return

    length = len(meanings)
    meaning_labels = []
    seperator_lbl = Label(root,text = "-"*60+"Meanings are Here"+"-"*60).place(x=100, y=60)
    for i in range(1,length):
        txt = str(i)+". "+meanings[i].text
        meaning_labels.append(Label(frame, text=txt))
        meaning_labels[i-1].place(x=20, y=70+i*30)
    meaning_labels = None


if __name__ == "__main__":
    root = Tk()
    root.config(bg="#2f3640")
    root.geometry("900x400")
    root.title("Dictionary 2.0")

    word = StringVar()

    lbl = Label(root,text="Enter Word : ").place(x=270, y=30)
    ent = Entry(root, width=30, textvariable=word).place(x=360,y=30)
    sub = Button(root, text = "Submit", command=getMeanings).place(x=550,y=30)

    

    root.mainloop()
