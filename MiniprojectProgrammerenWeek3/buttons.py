__author__ = 'Bram + Frank'
import csv
csvKlantBestand = 'C:/Users\Frank\PycharmProjects\software\MiniprojectProgrammerenWeek3\klantBestand.csv'
from tkinter import *


#de dementsies van het scherm
root = Tk()
#fieldnames voor het opslaan in csv bestand
fieldnames = ["email", "wachtwoord", "naam", "achternaam"]

#maakt header aan
def maakDictionaryHeaders():
    klantBestand = open(csvKlantBestand, 'a', newline='')
    writer = csv.writer(klantBestand,dialect='excel')
    writer.writerow(fieldnames)
maakDictionaryHeaders()

#slaat de textvariable op als een string
Email = StringVar()
Name = StringVar()
Surname = StringVar()
Password = StringVar()
Password2 = StringVar()
login = StringVar()
login2 = StringVar()

root["bg"] = "grey"
root.wm_title("simple gui")
root.resizable(width= False, height= True)
root.geometry("1200x720+0+0")
canvas = Canvas(width = 300, height = 200, bg = 'Gray')
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'achtergrond.gif')
canvas.create_image(0, 0, image = gif1, anchor = NW)


#knop voor het inloggen en inglogscherm
def inlogscherm():
    top = Toplevel()
    top.title("login")
    top["bg"] = "grey"
    login = Button(top, text = "login", command = leesUit)
    login.grid(row = 3, columnspan = 2)
    label_1 = Label(top, text = "Name", bg = "grey", fg = "white")
    label_2 = Label(top, text = "password", bg = "grey", fg = "white")
    entry_1 = Entry(top, textvariable = login)
    entry_2 = Entry(top, textvariable = login2)

    label_1.grid(row = 0, sticky = W)
    label_2.grid(row = 1, sticky = W)
    entry_1.grid(row = 0, column = 1)
    entry_2.grid(row = 1, column = 1)
#scherm voor het invullen van gegevens
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

    entry_1 = Entry(bottomframe, textvariable = Email)
    entry_2 = Entry(bottomframe, textvariable = Name)
    entry_3 = Entry(bottomframe, textvariable = Surname)
    entry_4 = Entry(bottomframe, textvariable = Password)
    entry_5 = Entry(bottomframe, textvariable = Password2)

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
    submit = Button(bottomframe, text = "submit", command = opslaan)
    submit.grid(row = 6, columnspan = 2)


#slaat de tekst op in csv bestand
def opslaan():
    email = Email.get()
    naam = Name.get()
    achternaam = Surname.get()
    wachtwoord = Password.get()
    wachtwoord2 = Password2.get()

    if wachtwoord == wachtwoord2:
        try:
            klantBestand = open(csvKlantBestand, 'a', newline='')
            writer = csv.DictWriter(klantBestand,delimiter=',', fieldnames=fieldnames)
            writer.writerow({"email": email, "wachtwoord": wachtwoord, "naam":naam, "achternaam": achternaam})

        finally:
            klantBestand.close()

    else:
        print("Wachtwoord komt niet overeen")

#controle inloggen
def leesUit():

    inlogEmail = login.get()
    inlogWachtwoord = login2.get()

    print(inlogEmail)
    print(inlogWachtwoord)

    try:
        leesKlantUit = open(csvKlantBestand, 'r')
        reader = csv.DictReader(leesKlantUit, delimiter=',')

        for row in reader:
            if row["email"] == inlogEmail and row["wachtwoord"] == inlogWachtwoord:
                print("Inloggen is een succes!")
            else:
                print("Inloggen is niet gelukt")

    finally:
        leesKlantUit.close()





#de knopen voor het inloggen
buton_1 = Button(root, text = " login   ", command = inlogscherm, bg = "red", fg = "white", width = 10 ,height = 1, font = ("broadway", 12))
buton_2 = Button(root, text = "register", command = registreren, bg = "red", fg = "white", width = 10, height = 1, font = ("broadway", 12))

buton_1.place(x = 800, y = 30)
buton_2.place(x = 800, y = 80)
#tekt met welkom erin
def welkom_tekst():
    w = Canvas(root,width = 400, height = 200)
    w.create_rectangle(400, 200, 0 , 0, fill = "red")
    w.create_text(190, 100,text = "Welcome to Movie-Net", fill = "white", font = ("broadway", 20))
    w.place(x = 10, y = 10)

welkom_tekst()
#rode balk in hoofdscherm
def rodebalk():
    w = Canvas(root,width = 1100, height = 50)
    w.create_rectangle(1100, 50, 0, 0, fill = "red")
    w.create_text(100, 25,text = "Today on Movie-Net", fill = "white", font = ("broadway", 12))
    w.place(x = 10, y = 300)
rodebalk()

def na_inloggen():
    top = Toplevel()
    top.title("Movie-Net")
    top["bg"] = "grey"
    top.resizable(width= False, height= True)
    top.geometry("1200x720+0+0")

    achtergrond = Canvas(Toplevel, width = 200, height = 200)
    achtergrond.pack()
    img = Tk.P
    achtergrond.create_image(50,50,image = img)

    helptekst = Canvas(top, width = 200, height = 50)
    helptekst.create_rectangle(200,50,0,0, fill = "red")
    helptekst.create_text(100, 25, text = "", fill = "white", font = ("broadway", 12))
    helptekst.place(relx= 0.41,rely = 0.05)

    w = Canvas(top,width = 400, height = 200)
    w.create_rectangle(400, 200, 0 , 0, fill = "red")
    w.create_text(190, 100,text = "Welcome to Movie-Net", fill = "white", font = ("broadway", 20))
    w.place(x = 10, y = 10)

    loginemail = login.get()
    loginww = login2.get()






root.mainloop()
