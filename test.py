__author__ = 'Bram'

from tkinter import *

#de dementsies van het scherm
root = Tk()
root["bg"] = "grey"
root.wm_title("simple gui")
root.geometry("720x500+320+100")

#de knopen voor het inloggen
buton_frame = Frame(root)
buton_frame.pack(side = TOP)
buton_1 = Button(buton_frame, text = "login")
buton_2 = Button(buton_frame, text = "register")
buton_1.grid(row = 0, sticky = E)
buton_2.grid(row = 0,column = 1, sticky = E)


entry_1 = Entry(root)
entry_2 = Entry(root)

root.mainloop()


def inlogscherm():
    pass