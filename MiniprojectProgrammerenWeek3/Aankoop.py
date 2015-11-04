__author__ = 'Rica'

from  MiniprojectProgrammerenWeek3 import FilmsOphalen

i=0

alleLijsten_van_de_films = []

#Maakt lijsten van de films van die dag
while i < len(FilmsOphalen.titelFilms):
    nieuwelijst = []
    alleLijsten_van_de_films.append(nieuwelijst)
    i += 1

print (alleLijsten_van_de_films)

#Aanschaf knop, voegt gebruikersnaam toe aan ID van de film
alleLijsten_van_de_films[0].append("asdaweasd")

print(alleLijsten_van_de_films[0])