__author__ = 'kevin'

from tkinter import *

root = Tk()
Topframe = Frame(root)
Topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button_1 = Button(Topframe, text= "inloggen", fg= "red")
button_2 = Button(Topframe, text= "click here", fg= "green")
button_3 = Button(Topframe, text= "click here", fg= "yellow")
button_4 = Button(bottomframe, text= "click here", fg= "blue")

button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()

root.mainloop()
