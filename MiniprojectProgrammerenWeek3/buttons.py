__author__ = 'Bram'

from tkinter import *

#de dementsies van het scherm
root = Tk()
root["bg"] = "grey"
root.wm_title("simple gui")
root.resizable(width= False, height= True)
root.geometry("1200x720+0+0")
canvas = Canvas(width = 300, height = 200, bg = 'Gray')
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'achtergrond.gif')
canvas.create_image(0, 0, image = gif1, anchor = NW)


#de werking van de knopen
def inlogscherm():
    top = Toplevel()
    top.title("login")
    label_1 = Label(top, text = "Name")
    label_2 = Label(top, text = "password")
    entry_1 = Entry(top)
    entry_2 = Entry(top)

    label_1.grid(row = 0, sticky = E)
    label_2.grid(row = 1, sticky = E)
    entry_1.grid(row = 0, column = 1)
    entry_2.grid(row = 1, column =1)

def registreren():
    top = Toplevel()
    top.title("Register")
    top.resizable(width= False, height= False)
    top.geometry("500x250+50+70")
    top["bg"] = "grey"

    helptekst = Canvas(top, width = 200, height = 50)
    helptekst.create_rectangle(200,50,0,0, fill = "red")
    helptekst.create_text(100, 25, text = "Fill in the blanks", fill = "white", font = ("broadway", 12))
    helptekst.place(relx= 0.3,rely = 0.05)

    bottomframe = Frame(top)
    bottomframe.pack(side = BOTTOM)

    label_1 = Label(bottomframe, text = "Email")
    label_2 = Label(bottomframe, text = "Name")
    label_3 = Label(bottomframe, text = "Surname")
    label_4 = Label(bottomframe, text = "Password")
    label_5 = Label(bottomframe, text = "Repeat password")

    entry_1 = Entry(bottomframe)
    entry_2 = Entry(bottomframe)
    entry_3 = Entry(bottomframe)
    entry_4 = Entry(bottomframe)
    entry_5 = Entry(bottomframe)

    label_1.grid(row = 1, sticky = W)
    label_2.grid(row = 2, sticky = W)
    label_3.grid(row = 3, sticky = W)
    label_4.grid(row = 4, sticky = W)
    label_5.grid(row = 5, sticky = W)

    entry_1.grid(row = 1, column = 1)
    entry_2.grid(row = 2, column = 1)
    entry_3.grid(row = 3, column = 1)
    entry_4.grid(row = 4, column = 1)
    entry_5.grid(row = 5, column = 1)

#de knopen voor het inloggen


buton_1 = Button(root, text = " login   ", command = inlogscherm)
buton_2 = Button(root, text = "register", command = registreren)

buton_1.place(x = 1145, y = 20)
buton_2.place(x = 1090, y = 20)

def welkom_tekst():
    w = Canvas(root,width = 400, height = 200)
    w.create_rectangle(400, 200, 0 , 0, fill = "red")
    w.create_text(190, 100,text = "Welcome to Movie-Net", fill = "white", font = ("broadway", 20))
    w.place(x = 10, y = 10)

welkom_tekst()

def aanbot_1():
    w = Canvas(root,width = 1100, height = 50)
    w.create_rectangle(1100, 50, 0, 0, fill = "red")
    w.create_text(100, 25,text = "Today on Movie-Net", fill = "white", font = ("broadway", 12))
    w.place(x = 10, y = 300)

aanbot_1()

root.mainloop()
