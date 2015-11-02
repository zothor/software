__author__ = 'jouke-bouwe'

import csv
csvKlantBestand = 'C:/Users/jouke-bouwe/Documents/School/schoolOpdrachten/MiniprojectProgrammerenWeek3/klantBestand.csv'

#variablen voor het inloggen van de user
inlogEmail = ""
inlogWachtwoord = ""


def leesUit():

    inlogEmail = input("Geef je e-mail")
    inlogWachtwoord = input("Geef je wachtwoord")

    try:
        LeesKlantUit = open(csvKlantBestand, 'r')
        reader = csv.DictReader(leesKlantUit, delimiter='\n')

        for row in reader:
            if email == inlogEmail and wachtwoord == inlogWachtwoord:
                print("Inloggen is een succes!")
            else:
                print("Inloggen is niet gelukt")
    finally:
        leesKlantUit.close()
leesUit()