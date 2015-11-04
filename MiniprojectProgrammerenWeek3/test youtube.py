import sys
from tkinter import *
def mhelo():
    mtext = ment.get()
    mlabel2 = Label(mGui,text=mtext).pack()



mGui = Tk()
ment = StringVar()

mGui.geometry("1280x720+0+0")
mGui.title('hallo')

mlabel = Label(mGui,text='My Label').pack

mbutton = Button(mGui,text = 'OK',command = mhelo, fg ='red',bg ='blue').pack()

mEnrty = Entry(mGui,textvariable=ment).pack()

mGui.mainloop()