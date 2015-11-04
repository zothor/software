__author__ = 'jouke-bouwe'

from  MiniprojectProgrammerenWeek3 import FilmsOphalen

print (FilmsOphalen.alleAanbieders)

lijstFrank = []
lijstKevin = []
lijstJouke = []
lijstBram = []
lijstRicardo = []

FilmsOphalen.getJaartal()

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

print ("Frank : " + str(lijstFrank))
print ("Kevin : " + str(lijstKevin))
print ("Jouke-Bouwe : " + str(lijstJouke))
print ("Bram : " + str(lijstBram))
print ("Ricardo : " + str(lijstRicardo))