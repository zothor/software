__author__ = 'Rica'

import random
from MiniprojectProgrammerenWeek3 import Klant
from  MiniprojectProgrammerenWeek3 import FilmsOphalen

uniekeCode = ""
alleLijsten_van_de_films = []

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