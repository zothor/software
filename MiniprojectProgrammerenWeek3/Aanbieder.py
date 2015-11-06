__author__ = 'Jouke-bouwe + Ricardo'

from  MiniprojectProgrammerenWeek3 import FilmsOphalen

#Deze klasse wordt op dit moment niet gebruikt. Het functioneerde als test om alle films van een aanbieder in een lijst te zetten.

print (FilmsOphalen.alleAanbieders)

#Maakt lege lijsten aan die later worden gevuld
lijstFrank = []
lijstKevin = []
lijstJouke = []
lijstBram = []
lijstRicardo = []

FilmsOphalen.getJaartal()

#Doorloopt een loop die films aan de lijsten toevoegt tot de laatste film is behaald
i=0
while i < len(FilmsOphalen.titelFilms):
    if FilmsOphalen.alleAanbieders[i] == "Frank":
        lijstFrank.append(FilmsOphalen.titelFilms[i])
        i += 1
    elif FilmsOphalen.alleAanbieders[i] == "Kevin":
        lijstKevin.append(FilmsOphalen.titelFilms[i])
        i += 1
    elif FilmsOphalen.alleAanbieders[i] == "Jouke-Bouwe":
        lijstJouke.append(FilmsOphalen.titelFilms[i])
        i += 1
    elif FilmsOphalen.alleAanbieders[i] == "Bram":
        lijstBram.append(FilmsOphalen.titelFilms[i])
        i += 1
    elif FilmsOphalen.alleAanbieders[i] == "Ricardo":
        lijstRicardo.append(FilmsOphalen.titelFilms[i])
        i += 1
    else:
        print("Het werkt niet")
        i += 1

#Test of de lijsten werken
print ("Frank : " + str(lijstFrank))
print ("Kevin : " + str(lijstKevin))
print ("Jouke-Bouwe : " + str(lijstJouke))
print ("Bram : " + str(lijstBram))
print ("Ricardo : " + str(lijstRicardo))