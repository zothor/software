__author__ = 'Bram'

from tkinter import *

#de dementsies van het scherm
root = Tk()
root["bg"] = "grey"
root.wm_title("simple gui")
root.resizable(width= False, height= False)
root.geometry("1280x720+0+0")

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
    top.title("register")
    label_1 = Label(top, text = "Email")
    label_2 = Label(top, text = "Name")
    label_3 = Label(top, text = "Surname")
    label_4 = Label(top, text = "Password")
    label_5 = Label(top, text = "Repeat password")

    entry_1 = Entry(top)
    entry_2 = Entry(top)
    entry_3 = Entry(top)
    entry_4 = Entry(top)
    entry_5 = Entry(top)

    label_1.grid(row = 0, sticky = E)
    label_2.grid(row = 1, sticky = E)
    label_3.grid(row = 2, sticky = E)
    label_4.grid(row = 3, sticky = E)
    label_5.grid(row = 4, sticky = E)

    entry_1.grid(row = 0, column = 1)
    entry_2.grid(row = 1, column = 1)
    entry_3.grid(row = 2, column = 1)
    entry_4.grid(row = 3, column = 1)
    entry_5.grid(row = 4, column = 1)

#de knopen voor het inloggen


buton_1 = Button(root, text = " login   ", command = inlogscherm)
buton_2 = Button(root, text = "register", command = registreren)

buton_1.grid(row = 0, ipadx = 25, padx = 600)
buton_2.grid(row = 1, ipadx = 25)


root.mainloop()
