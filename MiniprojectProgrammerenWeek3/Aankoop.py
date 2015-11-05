__author__ = 'Rica'

import csv
import random
from MiniprojectProgrammerenWeek3 import Klant
from MiniprojectProgrammerenWeek3 import FilmsOphalen

csvFrankBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/frankBestand.csv'
csvKevinBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/kevinBestand.csv'
csvBramBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/bramBestand.csv'
csvJoukeBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/joukeBestand.csv'
csvRicardoBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/ricardoBestand.csv'

fieldnames = ["naam", "achternaam", "film"]

uniekeCode = ""
alleLijsten_van_de_films = []

def maakFrankHeaders():
    frankBestand = open(csvFrankBestand, 'a', newline='')
    writer = csv.writer(frankBestand,dialect='excel')
    writer.writerow(fieldnames)

def maakKevinHeaders():
    kevinBestand = open(csvKevinBestand, 'a', newline='')
    writer = csv.writer(kevinBestand,dialect='excel')
    writer.writerow(fieldnames)

def maakBramHeaders():
    bramBestand = open(csvBramBestand, 'a', newline='')
    writer = csv.writer(bramBestand,dialect='excel')
    writer.writerow(fieldnames)

def maakJoukeHeaders():
    joukeBestand = open(csvJoukeBestand, 'a', newline='')
    writer = csv.writer(joukeBestand,dialect='excel')
    writer.writerow(fieldnames)

def maakRicardoHeaders():
    ricardoBestand = open(csvRicardoBestand, 'a', newline='')
    writer = csv.writer(ricardoBestand,dialect='excel')
    writer.writerow(fieldnames)

def voegFrankKlantToe():    #Hebben nog input nodig welke film wordt geselecteerd
    try:
        frankBestand = open(csvFrankBestand, 'a', newline='')
        writer = csv.DictWriter(frankBestand,delimiter=',', fieldnames=fieldnames)
        writer.writerow({"naam": Klant.huidigNaam, "achternaam": Klant.huidigAchternaam, "film":input})
    finally:
        frankBestand.close()

#Maakt lijsten van de films van die dag
i=0
while i < len(FilmsOphalen.titelFilms):
    nieuwelijst = []
    alleLijsten_van_de_films.append(nieuwelijst)
    i += 1

def genereerCode():
    global uniekeCode
    uniekeCode = random.randrange(1000,9999)

genereerCode()
FilmsOphalen.GetStart()

#Aanschaf knop, voegt gebruikersnaam toe aan ID van de film
alleLijsten_van_de_films[0].append(FilmsOphalen.starttijd + " " + Klant.huidigAchternaam + " " + str(uniekeCode))

print(sorted(alleLijsten_van_de_films[0]))