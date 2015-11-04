__author__ = 'Rica'

import requests
from bs4 import BeautifulSoup
import time

AmerikaanseDatum = time.strftime('%x')
DatumVandaag = AmerikaanseDatum[3:5] + "-" + AmerikaanseDatum[:2] + "-" + "20" + AmerikaanseDatum[6:]
#DatumMorgen = str(int(AmerikaanseDatum[3:5])+1) + "-" + AmerikaanseDatum[:2] + "-" + "20" + AmerikaanseDatum[6:]

URL = "http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=yis8n3b7soomlixah6ut8e6pe93epn2u&dag=" + str(DatumVandaag) + "&sorteer=0"
print (URL)

def GetTitels():    #Haalt filmtitel op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('titel'):
        titel = link.string
        print (titel)

def GetCovers():    #Haalt film cover op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('cover'):
        cover = link.string
        print (cover)

def GetLengtes():   #Haal filmlengte op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('duur'):
        duur = link.string
        print (duur)

def GetLinks(): #Haal link op naar de FilmTotaal pagina
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('ft_link'):
        ft_link = link.string
        print (ft_link)

def GetStart(): #Haal film starttijd op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('starttijd'):
        starttijd = link.string
        print (starttijd)

def GetZenders():   #Haal zenders (aanbieders?) op
    source_code = requests.get(URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('zender'):
        zender = link.string
        print (zender)

print("Hieronder alle titels die vandaag draaien:")
GetTitels()
print("\n hieronder worden de links van de covers benoemd:")
GetCovers()
print("\n Hieronder vermelden we hoelang een film duurt:")
GetLengtes()
print("\n De namen van de aanbieders staan hieronder:")
GetZenders()