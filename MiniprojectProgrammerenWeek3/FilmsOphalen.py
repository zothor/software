__author__ = 'Rica'

import requests
from bs4 import BeautifulSoup
import time

AmerikaanseDatum = time.strftime('%x')
DatumVandaag = AmerikaanseDatum[3:5] + "-" + AmerikaanseDatum[:2] + "-" + "20" + AmerikaanseDatum[6:]
#DatumMorgen = str(int(AmerikaanseDatum[3:5])+1) + "-" + AmerikaanseDatum[:2] + "-" + "20" + AmerikaanseDatum[6:]

URL = "http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=yis8n3b7soomlixah6ut8e6pe93epn2u&dag=" + str(DatumVandaag) + "&sorteer=0"
print (URL)

titelFilms = []
coversFilms = []
lengteFilms = []
alleAanbieders = []
alleJaartallen = []

#Bij deze functie voegen wij alle informatie afkomstig van de XML pagina samen tot een geheel (bedoeling is om ook te gaan tekenen met deze functie)
def printInformatie_van_een_film():
    hoeveelFilms = len(titelFilms)
    films = 0
    statement = True


    while statement:
        if films < hoeveelFilms:
            print(str(films+1) + ': ' + str(titelFilms[films]) + " - " + coversFilms[films]+ " - "+ str(lengteFilms[films]) + " - " +
                  str(alleJaartallen[films]) + " - " + str(alleAanbieders[films]))
            films += 1

        else:
            statement = False



def GetTitels():    #Haalt filmtitel op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('titel'):
        titel = link.string
        titelFilms.append(titel)


def GetCovers():    #Haalt film cover op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('cover'):
        cover = link.string
        coversFilms.append(cover)

def GetLengtes():   #Haal filmlengte op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('duur'):
        duur = link.string
        lengteFilms.append(duur)
        print(duur)

def GetLinks(): #Haal link op naar de FilmTotaal pagina
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('ft_link'):
        ft_link = link.string

def GetStart(): #Haal film starttijd op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('starttijd'):
        starttijd = link.string

def GetEind(): #Haal film starttijd op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('eindtijd'):
        eindtijd = link.string

def GetAanbieders():   #Haal zenders (aanbieders?) op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('zender'):
        zender = link.string
        alleAanbieders.append(zender)

def getJaartal(): #Haalt het jaartal van de film op van de api.
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('jaar'):
        jaartal = link.string
        alleJaartallen.append(jaartal)


print("Hieronder alle titels die vandaag draaien:")
GetTitels()
print("\n Hieronder vermelden we hoelang een film duurt:")
GetLengtes()
print("\n hieronder worden de links van de covers benoemd:")
GetCovers()
print("\n De namen van de aanbieders staan hieronder:")
GetAanbieders()
getJaartal()


printInformatie_van_een_film()