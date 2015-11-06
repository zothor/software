__author__ = 'Rica'

import csv
import random
import os.path
from MiniprojectProgrammerenWeek3 import FilmsOphalen

csvFrankBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/frankBestand.csv'
csvKevinBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/kevinBestand.csv'
csvBramBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/bramBestand.csv'
csvJoukeBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/joukeBestand.csv'
csvRicardoBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/ricardoBestand.csv'

fieldnames2 = ["naam", "achternaam", "film", "code"]

uniekeCode = ""
alleLijsten_van_de_films = []

def maakFrankHeaders():
    frankBestand = open(csvFrankBestand, 'a', newline='')
    writer = csv.writer(frankBestand,dialect='excel')
    writer.writerow(fieldnames2)

def maakKevinHeaders():
    kevinBestand = open(csvKevinBestand, 'a', newline='')
    writer = csv.writer(kevinBestand,dialect='excel')
    writer.writerow(fieldnames2)

def maakBramHeaders():
    bramBestand = open(csvBramBestand, 'a', newline='')
    writer = csv.writer(bramBestand,dialect='excel')
    writer.writerow(fieldnames2)

def maakJoukeHeaders():
    joukeBestand = open(csvJoukeBestand, 'a', newline='')
    writer = csv.writer(joukeBestand,dialect='excel')
    writer.writerow(fieldnames2)

def maakRicardoHeaders():
    ricardoBestand = open(csvRicardoBestand, 'a', newline='')
    writer = csv.writer(ricardoBestand,dialect='excel')
    writer.writerow(fieldnames2)

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
#alleLijsten_van_de_films[0].append(FilmsOphalen.starttijd + " " + buttons.huidigAchternaam + " " + str(uniekeCode))

#print(sorted(alleLijsten_van_de_films[0]))

if os.path.isfile(csvFrankBestand) == True:
    pass
else:
    maakFrankHeaders()
if os.path.isfile(csvKevinBestand) == True:
    pass
else:
    maakKevinHeaders()
if os.path.isfile(csvBramBestand) == True:
    pass
else:
    maakBramHeaders()
if os.path.isfile(csvJoukeBestand) == True:
    pass
else:
    maakJoukeHeaders()
if os.path.isfile(csvRicardoBestand) == True:
    pass
else:
    maakRicardoHeaders()