__author__ = 'jouke-bouwe'
#
import csv
csvKlantBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/klantBestand.csv'
#csvKlantBestand = 'C:/Users/jouke-bouwe/Documents/School/software/MiniprojectProgrammerenWeek3/klantBestand.csv'

#variablen voor het registreren en opslag
email = ""
naam = ""
achternaam = ""
wachtwoord = ""
wachtwoord2 = ""

#variablen voor het inloggen van de user
inlogEmail = ""
inlogWachtwoord = ""

#variabelen voor het opslaan wie is ingelogd
huidigEmail = ""
huidigNaam = ""
huidigAchternaam = ""

fieldnames = ["email", "wachtwoord", "naam", "achternaam"]


def maakDictionaryHeaders():
    klantBestand = open(csvKlantBestand, 'a', newline='')
    writer = csv.writer(klantBestand,dialect='excel')
    writer.writerow(fieldnames)

#In deze functie slaan we de gegevens van de klant op in een csv bestand.

def registreren(email, wachtwoord, naam, achternaam):

    email = input("Vul hier je e-mail adress in")
    wachtwoord = input("Vul hier je wachtwoord in")
    wachtwoord2 = input("Vul hier je wachtwoord in ter controle")
    naam = input("Vul hier je naam in")
    achternaam = input("Vul hier je achternaam in")

    if wachtwoord == wachtwoord2:
        try:
            klantBestand = open(csvKlantBestand, 'a', newline='')
            writer = csv.DictWriter(klantBestand,delimiter=',', fieldnames=fieldnames)
            writer.writerow({"email": email, "wachtwoord": wachtwoord, "naam":naam, "achternaam": achternaam})

        finally:
            klantBestand.close()
    else:
        print("Wachtwoord komt niet overeen")

#leest het csv bestand uit en kijkt of de usergegevens overeenkomen met die hij heeft ingevuld.
def leesUit():

    inlogEmail = input("Geef je e-mail")
    inlogWachtwoord = input("Geef je wachtwoord")

    try:
        leesKlantUit = open(csvKlantBestand, 'r')
        reader = csv.DictReader(leesKlantUit, delimiter=',')

        for row in reader:
            if row["email"] == inlogEmail and row["wachtwoord"] == inlogWachtwoord:
                print ("Ingeloggen is een succes")
                global huidigEmail, huidigNaam, huidigAchternaam
                huidigEmail = row["email"]
                huidigNaam = row["naam"]
                huidigAchternaam = row["achternaam"]
            else:
                print("Inloggen is niet gelukt")

    finally:
        leesKlantUit.close()

#maakDictionaryHeaders()
#registreren(email, wachtwoord, naam, achternaam)
#leesUit()
#print (huidigEmail)
#print (huidigNaam)
#print (huidigAchternaam)
