__author__ = 'Ricardo + Jouke-bouwe'

import csv
import random
import os.path
from MiniprojectProgrammerenWeek3 import FilmsOphalen

#Verwijst naar de csv bestanden. Moeten wel aangepast worden als dit op een andere computer wordt uitgevoerd
csvFrankBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/frankBestand.csv'
csvKevinBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/kevinBestand.csv'
csvBramBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/bramBestand.csv'
csvJoukeBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/joukeBestand.csv'
csvRicardoBestand = 'C:/Users/Rica/PycharmProjects/software/MiniprojectProgrammerenWeek3/ricardoBestand.csv'

#Benaamt de key values voor de csv bestanden van de aanbieders
fieldnames2 = ["naam", "achternaam", "film", "code"]

uniekeCode = ""

#De titels van alle films van die dag
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

#Genereert een random code van 4 cijfers die deel is van de ticket
def genereerCode():
    global uniekeCode
    uniekeCode = random.randrange(1000,9999)

FilmsOphalen.GetStart()

#Controleert of de csv bestanden al bestaan. Als dit niet zo is maakt hij ze aan en schrijft de key values bovenaan
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