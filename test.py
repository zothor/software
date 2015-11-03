__author__ = 'kevin'

from tkinter import *

def inlogscherm():
    print("inlogscherm geopend")


root = Tk()
root.wm_title("simple gui")
root.geometry("720x500+320+100")


background = Frame(root, bg = "yellow")
background.pack()
Topframe = Frame(root)
Topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button_1 = Button(Topframe, text= "inloggen", fg= "grey", command = inlogscherm())
button_2 = Button(Topframe, text= "click here", fg= "green")
button_3 = Button(Topframe, text= "click here", fg= "yellow")
button_4 = Button(bottomframe, text= "click here", fg= "blue")

button_1.pack(side= BOTTOM)
button_2.pack(side= TOP)
button_3.pack(side= BOTTOM)
button_4.pack()




root.mainloop()
