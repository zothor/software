__author__ = 'Bram + Frank + Ricardo + Kevin + Jouke-bouwe'
import csv
from tkinter import *
from MiniprojectProgrammerenWeek3 import FilmsOphalen, Aankoop

#Verwijst naar de csv bestanden die gebruikt worden. Moet worden aangepast als deze op een andere pc wordt uitgevoerd
csvKlantBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/klantBestand.csv'
csvFrankBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/frankBestand.csv'
csvKevinBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/kevinBestand.csv'
csvBramBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/bramBestand.csv'
csvJoukeBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/joukeBestand.csv'
csvRicardoBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/ricardoBestand.csv'

'''Variabelen die gebruikt werden in de loop die buttons zou maken
#variablen om films op te halen
naarbeneden = 330
opgehaaldefilm=0
alleFilmButtons = []
'''

#variabelen voor het opslaan wie is ingelogd
huidigEmail = ""
huidigNaam = ""
huidigAchternaam = ""
ingelogdOfNiet = False

#Variabelen die gebruikt worden om film informatie te tonen
labelnaam = ""
labelfilm = ""
labelduur = ""

#maakt het hoofdscherm aan
root = Tk()
root["bg"] = "grey"
root.wm_title("Movie-Net")
root.resizable(width= False, height= True)
root.geometry("1200x720+0+0")

#fieldnames voor het opslaan van key values in csv bestand
fieldnames = ["email", "wachtwoord", "naam", "achternaam"]

#maakt header aan van het bestand waar klantinformatie wordt opgeslagen
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
login1 = StringVar()
login2 = StringVar()

#het achtergrond plaatje
canvas = Canvas( width = 300, height = 200, bg = 'Gray')
canvas.pack( expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'achtergrond.gif')
canvas.create_image(0, 0, image = gif1, anchor = NW)

#de werking van de knoppen op het inlogscherm
def inlogscherm():
    top = Toplevel()
    top.title("login")
    top["bg"] = "grey"

    #Leest de inputs van de gebruiker
    login = Button(top, text = "login", command = (lambda: leesUit(top)))
    login.grid(row = 3, columnspan = 2)
    label_1 = Label(top, text = "Email", bg = "grey", fg = "white")
    label_2 = Label(top, text = "Password", bg = "grey", fg = "white")
    entry_1 = Entry(top, textvariable = login1)
    entry_2 = Entry(top, textvariable = login2)

    label_1.grid(row = 0, sticky = W)
    label_2.grid(row = 1, sticky = W)
    entry_1.grid(row = 0, column = 1)
    entry_2.grid(row = 1, column = 1)

#scherm voor het invullen van gegevens voor registreren
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
    bottomframe["bg"] = "grey"

    label_1 = Label(bottomframe, text = "Email", bg = "grey", fg = "white")
    label_2 = Label(bottomframe, text = "Name", bg = "grey", fg = "white")
    label_3 = Label(bottomframe, text = "Surname", bg = "grey", fg = "white")
    label_4 = Label(bottomframe, text = "Password", bg = "grey", fg = "white")
    label_5 = Label(bottomframe, text = "Repeat password", bg = "grey", fg = "white")

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
    submit = Button(bottomframe, text = "submit", command = (lambda: opslaan(top)))
    submit.grid(row = 6, columnspan = 2)


#slaat de gebruikersinformatie op in csv bestand
def opslaan(top):
    global naam
    top.destroy()
    email = Email.get()
    naam = Name.get()
    achternaam = Surname.get()
    wachtwoord = Password.get()
    wachtwoord2 = Password2.get()

    #Controleert of het wachtwoord 2 keer goed is ingevoerd
    if wachtwoord == wachtwoord2:
        try:
            klantBestand = open(csvKlantBestand, 'a', newline='')
            writer = csv.DictWriter(klantBestand,delimiter=',', fieldnames=fieldnames)
            writer.writerow({"email": email, "wachtwoord": wachtwoord, "naam":naam, "achternaam": achternaam})

        finally:
            klantBestand.close()

    else:
        print("Wachtwoord komt niet overeen")

#Nieuw hoofdscherm na inloggen
def welkomtekst():
    user = Canvas(root,width = 400, height = 100)
    user.create_rectangle(400, 200, 0 , 0, fill = "red")
    user.create_text(190, 50,text = ("Welcome " + huidigNaam ), fill = "white", font = ("broadway", 20))
    user.place(x = 10, y = 10)

#Leest de opgeslagen gegevens uit het csv bestand
def leesUit(top):

    global inlogEmail
    inlogEmail = login1.get()
    inlogWachtwoord = login2.get()

    print(inlogEmail)
    print(inlogWachtwoord)

    try:
        leesKlantUit = open(csvKlantBestand, 'r')
        reader = csv.DictReader(leesKlantUit, delimiter=',')

        for row in reader:
            if row["email"] == inlogEmail and row["wachtwoord"] == inlogWachtwoord:
                print("Inloggen is een succes!")
                print ("Ingeloggen is een succes")
                global huidigEmail, huidigNaam, huidigAchternaam
                huidigEmail = row["email"]
                huidigNaam = row["naam"]
                huidigAchternaam = row["achternaam"]
                #cleart het scherm
                global buton_1
                global buton_2
                global today
                global w
                buton_1.destroy()
                buton_2.destroy()
                top.destroy()
                w.destroy()
                global ingelogdOfNiet
                ingelogdOfNiet = True
                welkomtekst()

            else:
                print("Inloggen is niet gelukt")

    finally:
        leesKlantUit.close()





#de knoppen voor het inloggen en registreren aanmaken op het hoofdscherm
buton_1 = Button(root, text = " login   ", command = inlogscherm, bg = "red", fg = "white", width = 10 ,height = 1, font = ("broadway", 12))
buton_2 = Button(root, text = "register", command = registreren, bg = "red", fg = "white", width = 10, height = 1, font = ("broadway", 12))

buton_1.place(x = 800, y = 30)
buton_2.place(x = 800, y = 80)

#De layout instellen van het hoofdscherm
w = Canvas(root,width = 400, height = 100)
w.create_rectangle(400, 200, 0 , 0, fill = "red")
w.create_text(190, 50,text = "Welcome to Movie-Net", fill = "white", font = ("broadway", 20))
w.place(x = 10, y = 10)

#de balk met het aan bod vandaag
def today():
    today = Canvas(root,width = 1100, height = 50)
    today.create_rectangle(1100, 50, 0, 0, fill = "red")
    today.create_text(100, 25,text = "Today on Movie-Net", fill = "white", font = ("broadway", 12))
    today.place(x = 10, y = 150)




def filmsOphalen():
    ''' Dit was de code om de buttons met een loop te maken, maar het is ons niet gelukt om hier mee te werken
    global opgehaaldefilm, naarbeneden,alleFilmButtons

    attributen voor het ophalen van de films
    nummersToevoegen =0

    while opgehaaldefilm <len(FilmsOphalen.titelFilms):
        j = opgehaaldefilm
        alleFilmButtonsNummers = alleFilmButtons.append(nummersToevoegen)
        naamButton = "Button" + str(j)
        naamButton = Button(root, text=FilmsOphalen.titelFilms[opgehaaldefilm], bg = "red", fg = "white", font = ("broadway", 12))

        labelLengteFilm = Label(root, text= ("Duur: " + str(FilmsOphalen.lengteFilms[opgehaaldefilm])))
        labelLengteFilm.place(x=500, y=naarbeneden)

        naamButton.place(x = 20, y = naarbeneden)
        opgehaaldefilm+=1
        naarbeneden += 35
        nummersToevoegen +=1
        '''

    #Maakt alle knoppen hardcoded aan :(
    try :
        Button1 = Button(root, text=FilmsOphalen.titelFilms[0], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(0)))
        Button1.place(x = 20, y = 230, width=350)
        Button2 = Button(root, text=FilmsOphalen.titelFilms[1], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(1)))
        Button2.place(x = 20, y = 265, width=350)
        Button3 = Button(root, text=FilmsOphalen.titelFilms[2], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(2)))
        Button3.place(x = 20, y = 300, width=350)
        Button4 = Button(root, text=FilmsOphalen.titelFilms[3], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(3)))
        Button4.place(x = 20, y = 335, width=350)
        Button5 = Button(root, text=FilmsOphalen.titelFilms[4], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(4)))
        Button5.place(x = 20, y = 370, width=350)
        Button6 = Button(root, text=FilmsOphalen.titelFilms[5], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(5)))
        Button6.place(x = 20, y = 405, width=350)
        Button7 = Button(root, text=FilmsOphalen.titelFilms[6], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(6)))
        Button7.place(x = 20, y = 440, width=350)
        Button8 = Button(root, text=FilmsOphalen.titelFilms[7], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(7)))
        Button8.place(x = 20, y = 475, width=350)
        Button9 = Button(root, text=FilmsOphalen.titelFilms[8], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(8)))
        Button9.place(x = 20, y = 510, width=350)
        Button10 = Button(root, text=FilmsOphalen.titelFilms[9], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(9)))
        Button10.place(x = 20, y = 545, width=350)
        Button11 = Button(root, text=FilmsOphalen.titelFilms[10], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(10)))
        Button11.place(x = 20, y = 580, width=350)
        Button12 = Button(root, text=FilmsOphalen.titelFilms[11], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(11)))
        Button12.place(x = 20, y = 615, width=350)
        Button13 = Button(root, text=FilmsOphalen.titelFilms[12], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(12)))
        Button13.place(x = 20, y = 650, width=350)
        Button14 = Button(root, text=FilmsOphalen.titelFilms[13], bg = "red", fg = "white", font = ("broadway", 12), command=(lambda:laatBeschrijvingZien(13)))
        Button14.place(x = 20, y = 685, width=350)
    except :
        pass

#Haalt de beschrijving van de film op en laat de koop knop zien
def laatBeschrijvingZien(filmnummer):
    global labelnaam
    global labelfilm
    global labelduur

    #Verwijdert de oude label als deze bestaat, anders overlappen ze elkaar
    if labelnaam == "":
        pass
    else:
        labelnaam.destroy()
    if labelfilm == "":
        pass
    else:
        labelfilm.destroy()
    if labelduur == "":
        pass
    else:
        labelduur.destroy()
    labelnaam = Label(root,text=(FilmsOphalen.titelFilms[filmnummer] + " : "), font = ("broadway", 18))
    labelnaam.place(x=400,y=230)
    labelduur = Label(root,text=("Filmduur : " + FilmsOphalen.lengteFilms[filmnummer] + " minuten."),wraplength=700, anchor=W, justify=LEFT, bg="black", fg="white")
    labelduur.place(x=400, y=270, width=700)
    labelfilm = Label(root,text=("Omschrijving : \n" + FilmsOphalen.alleBeschrijvingen[filmnummer]),wraplength=700, anchor=W, justify=LEFT, bg="black", fg="white")
    labelfilm.place(x=400, y=290, width=700)
    if ingelogdOfNiet == True:
        koopbutton = Button(root, text="Purchase", bg = "red", fg = "white", font = ("broadway", 12), command =(lambda:filmKopen(filmnummer)))
        koopbutton.place(x=1000, y=600)

#Voegt de aankoop toe aan het bestand van die aanbieder
def filmKopen(filmnummer):
    if FilmsOphalen.alleAanbieders[filmnummer] == "Frank":
        voegFrankKlantToe(filmnummer)
    elif FilmsOphalen.alleAanbieders[filmnummer] == "Bram":
        voegBramKlantToe(filmnummer)
    elif FilmsOphalen.alleAanbieders[filmnummer] == "Jouke":
        voegJoukeKlantToe(filmnummer)
    elif FilmsOphalen.alleAanbieders[filmnummer] == "Kevin":
        voegKevinKlantToe(filmnummer)
    elif FilmsOphalen.alleAanbieders[filmnummer] == "Ricardo":
        voegRicardoKlantToe(filmnummer)

#Hieronder de functies die de klant informatie toevoegt aan de aanbieder's lijst
def voegFrankKlantToe(filmnummer):    #Hebben nog input nodig welke film wordt geselecteerd
    Aankoop.genereerCode()
    kooptop = Toplevel()
    kooptop.title("Purchase successful!")
    kooptop.geometry("280x30+50+70")
    kooptop["bg"] = "grey"
    kooplabel = Label(kooptop, text=("Uw ticket code is : " + str(Aankoop.uniekeCode)), bg = "grey")
    kooplabel.pack()
    try:
        global frankBestand
        frankBestand = open(Aankoop.csvFrankBestand, 'a', newline='')
        writer = csv.DictWriter(frankBestand,delimiter=',', fieldnames=Aankoop.fieldnames2)
        writer.writerow({"naam": huidigNaam, "achternaam": huidigAchternaam, "film":FilmsOphalen.titelFilms[filmnummer], "code":Aankoop.uniekeCode})
    finally:
        frankBestand.close()

def voegBramKlantToe(filmnummer):    #Hebben nog input nodig welke film wordt geselecteerd
    Aankoop.genereerCode()
    kooptop = Toplevel()
    kooptop.title("Purchase successful!")
    kooptop.geometry("280x30+50+70")
    kooptop["bg"] = "grey"
    kooplabel = Label(kooptop, text=("Uw ticket code is : " + str(Aankoop.uniekeCode)), bg = "grey")
    kooplabel.pack()
    try:
        global bramBestand
        bramBestand = open(Aankoop.csvBramBestand, 'a', newline='')
        writer = csv.DictWriter(bramBestand,delimiter=',', fieldnames=Aankoop.fieldnames2)
        writer.writerow({"naam": huidigNaam, "achternaam": huidigAchternaam, "film":FilmsOphalen.titelFilms[filmnummer], "code":Aankoop.uniekeCode})
    finally:
        bramBestand.close()

def voegJoukeKlantToe(filmnummer):    #Hebben nog input nodig welke film wordt geselecteerd
    Aankoop.genereerCode()
    kooptop = Toplevel()
    kooptop.title("Purchase successful!")
    kooptop.geometry("280x30+50+70")
    kooptop["bg"] = "grey"
    kooplabel = Label(kooptop, text=("Uw ticket code is : " + str(Aankoop.uniekeCode)), bg = "grey")
    kooplabel.pack()
    try:
        global joukeBestand
        joukeBestand = open(csvJoukeBestand, 'a', newline='')
        writer = csv.DictWriter(joukeBestand,delimiter=',', fieldnames=Aankoop.fieldnames2)
        writer.writerow({"naam": huidigNaam, "achternaam": huidigAchternaam, "film":FilmsOphalen.titelFilms[filmnummer], "code":Aankoop.uniekeCode})
    finally:
        joukeBestand.close()

def voegKevinKlantToe(filmnummer):    #Hebben nog input nodig welke film wordt geselecteerd
    Aankoop.genereerCode()
    kooptop = Toplevel()
    kooptop.title("Purchase successful!")
    kooptop.geometry("280x30+50+70")
    kooptop["bg"] = "grey"
    kooplabel = Label(kooptop, text=("Uw ticket code is : " + str(Aankoop.uniekeCode)), bg = "grey")
    kooplabel.pack()
    try:
        global kevinBestand
        kevinBestand = open(csvKevinBestand, 'a', newline='')
        writer = csv.DictWriter(kevinBestand,delimiter=',', fieldnames=Aankoop.fieldnames2)
        writer.writerow({"naam": huidigNaam, "achternaam": huidigAchternaam, "film":FilmsOphalen.titelFilms[filmnummer], "code":Aankoop.uniekeCode})
    finally:
        kevinBestand.close()

def voegRicardoKlantToe(filmnummer):    #Hebben nog input nodig welke film wordt geselecteerd
    Aankoop.genereerCode()
    kooptop = Toplevel()
    kooptop.title("Purchase successful!")
    kooptop.geometry("280x30+50+70")
    kooptop["bg"] = "grey"
    kooplabel = Label(kooptop, text=("Uw ticket code is : " + str(Aankoop.uniekeCode)), bg = "grey")
    kooplabel.pack()
    try:
        global ricardoBestand
        ricardoBestand = open(csvRicardoBestand, 'a', newline='')
        writer = csv.DictWriter(ricardoBestand,delimiter=',', fieldnames=Aankoop.fieldnames2)
        writer.writerow({"naam": huidigNaam, "achternaam": huidigAchternaam, "film":FilmsOphalen.titelFilms[filmnummer], "code":Aankoop.uniekeCode})
    finally:
        ricardoBestand.close()
today()
filmsOphalen()
root.mainloop()
