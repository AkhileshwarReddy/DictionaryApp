from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup as bs

def getMeanings():
    url = "https://www.dictionary.com/browse/" + word.get()
    try:
        r = requests.get(url)
        soup = bs(r.content,"lxml")
    except:
        except_lbl = Label(root, text = "Oops! Check your internet connectivity!!!",
                           ).place(x=20, y=160)
        return

    try:
        d = soup.findAll("ol")
        meanings = d[0].findChildren("li", recursive=False)
    except:
        except_lbl = Label(root,text = "Word Not Found!!!").place(x=20, y=160)
        return
    
    l = len(meanings)
    mean_lbls = []
    txt = "-"*60+" Meanings Here "+"-"*60
    seperator_lbl = Label(root, text=txt).place(x=100,y=150)
    for i in range(l):
        txt = str(i+1)+". "+ meanings[i].text
        mean_lbls.append(Label(root, text = txt))
        mean_lbls[i].place(x=20, y=200+i*30)


if __name__ == "__main__":
    root = Tk()
    root.config(bg="#1289A7")
    scrbl_side = Scrollbar(root).pack(side = RIGHT, fill = Y)
    root.geometry("900x400")
    root.title("Dictionary")

    img = Image.open('./pictures/man3.jpg')
    render = ImageTk.PhotoImage(img)
    img_lbl = Label(root, image=render)
    img_lbl.image = render
    img_lbl.place(x=400, y=10)

    word = StringVar()

    lbl = Label(root, text = "Enter Word : ").place(x=270, y=100)
    ent = Entry(root, width = 30, textvariable=word).place(x = 350, y=100)
    sub = Button(root, text = "Submit", command = getMeanings).place(x=550,y=100)

    

    root.mainloop()
