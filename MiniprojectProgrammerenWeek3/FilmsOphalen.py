__author__ = 'Ricardo + Jouke-bouwe'

import requests
from bs4 import BeautifulSoup
import time

#De functie geeft datum in MM-DD-YY, dit moeten wij aanpassen om met de API te laten werken
AmerikaanseDatum = time.strftime('%x')
DatumVandaag = AmerikaanseDatum[3:5] + "-" + AmerikaanseDatum[:2] + "-" + "20" + AmerikaanseDatum[6:]
#DatumMorgen = str(int(AmerikaanseDatum[3:5])+1) + "-" + AmerikaanseDatum[:2] + "-" + "20" + AmerikaanseDatum[6:]

URL = "http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=yis8n3b7soomlixah6ut8e6pe93epn2u&dag=" + str(DatumVandaag) + "&sorteer=0"

#Maakt lege variabelen aan waar we later mee gaan werken
starttijd = ""
titelFilms = []
coversFilms = []
lengteFilms = []
alleAanbieders = []
alleJaartallen = []
alleBeschrijvingen = []

def GetTitels():    #Haalt filmtitel op met behulp van BeautifulSoup en slaat deze op in een lijst
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
    global starttijd
    for link in soup.findAll('starttijd'):
        starttijd = link.string

def GetEind(): #Haal film starttijd op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('eindtijd'):
        eindtijd = link.string

def GetRatings(): #Haal IMDB rating op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('imdb_rating'):
        imdb_rating = link.string

def getJaartal(): #Haalt het jaartal van de film op van de api en doorloopt alle jaartallen om te kijken voor welke aanbier hij geld.
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('jaar'):
        jaartal = link.string
        alleJaartallen.append(jaartal)
        jaartalIntMaken = int(jaartal)
        if jaartalIntMaken <= 1969:
            aanbieder = "Kevin"
        elif jaartalIntMaken >= 1970 and jaartalIntMaken <= 1989:
            aanbieder = "Frank"
        elif jaartalIntMaken >= 1990 and jaartalIntMaken <= 1999:
            aanbieder = "Bram"
        elif jaartalIntMaken >= 2000 and jaartalIntMaken <= 2009:
            aanbieder = "Jouke-Bouwe"
        elif jaartalIntMaken >= 2010:
            aanbieder = "Ricardo"
        alleAanbieders.append(aanbieder)

def GetSynopsis(): #Haal film starttijd op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    global synopsis
    for link in soup.findAll('synopsis'):
        synopsis = link.string
        alleBeschrijvingen.append(synopsis)


GetTitels()
GetLengtes()
GetCovers()
GetRatings()
getJaartal()
GetSynopsis()
