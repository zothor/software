__author__ = 'jouke-bouwe'

__author__ = 'anonymous'
import csv
import random

naam = ["test","nog","een"]
for i in naam:
    print(i)

fieldnames = ['Kluisnummer', 'Code']
naam = "jan"
salaris = 2000
print("Het salaris van {0:10s} is {1:5d}".format(naam,salaris))
def welkom():
    print("1: Ik wil een nieuwe kluist\n")
    print("2: Ik wil mijn kluis openen \n")
    print("3: Ik geef mijn kluis terug \n")
    print("4: Ik wil weten hoeveel kluizen er nog vrij zijn \n")
    optie = input()
    if optie == str(1):
        o_een()
    elif optie == str(2):
        o_twee()
    elif optie == str(3):
        o_drie()
    elif optie == str(4):
        o_vier()
    else:
        print("Geen juist nummer gekozen probeer nogmaals \n")
        welkom()


def o_een():
    x = aantal()
    code = ""
    while len(code) < 4:
        code += str(random.randrange(0, 9))


    bestand = open('kluisjes.csv', 'a')
    writer = csv.DictWriter(bestand, delimiter=',', fieldnames=fieldnames)
    writer.writerow({'Kluisnummer': x+1, 'Code': str(code)})
    if x < 12:
        print("Uw nieuwe kluisnummer is nummer " + str(x+1) + " met code "+ str(code))
    else:
        print("Er zijn helaas geen kluizen meer over")
    bestand.close()


def o_twee():
    code = input("Geef uw code op")
    bestand = open("kluisjes.csv", 'r')
    reader = csv.DictReader(bestand, delimiter=',')
    for row in reader:
        if row['Code'] == code:
            print(row)


def o_drie():
    pass


def o_vier():
    over = 12 - aantal()
    print("Er zijn nog " + str(over) + " kluizen over")

def aantal():
    bestand = open("kluisjes.csv", 'r')
    reader = csv.DictReader(bestand, delimiter=',', fieldnames=['Kluisnummer', 'Code'])
    counter = 0
    for row in reader:
        counter += 1
    bestand.close()
    return counter


welkom()
