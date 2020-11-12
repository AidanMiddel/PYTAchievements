#import time om mooie sleeps toe te passen
import time
#begint met uitleg van het verhaaltje
print("Hallo welkom bij: HET DAGELIJKS LEVEN....")
print("")
time.sleep(1)
print("klinkt eng of niet zeker?")
print("")
time.sleep(1)
print("laten we maar beginnen...")
print("")
time.sleep(1)

#uitleg vraag 1
print("")
print("je ligt lekker in bed te slapen tot je ineens een geluid hoort \neehhh eeehhh eehhhh eehh eehhh \nhet is je wekker....")
print("wat doe je?")
print("A. zet hem op snooze en wordt de volgende keer wakker \nB. ga je bed uit" )
print("")

#systeem om vraag 1 antwoorden te laten geven
wakkerworden = input("A of B(let op hoofdletters): ")
if wakkerworden == "A":
    print("")
    print("ah jij blijft nog lekker even liggen zeker....")
elif wakkerworden == "B":
    print("")
    print("ochtend mens? of gewoon zin in de dag?")
else:
    print("")
    print("let op hoofdletters! maar ik ga wel verder")
print("")
time.sleep(1)

#uitleg vraag 2
print("dus je bent je bed uit \nnou is de vraag, ga je douchen?")
print("A. nee niet nu \nB. ja ik ga nu even douchen")
print("")

#systeem om vraag 2 antwoorden te laten geven
douchen = input("A of B(let op hoofdletters): ")
if douchen == "A":
    print("")
    print("oh oké, zolang je het maar vanavond doet")
elif douchen == "B":
    print("")
    print("lekker even in de ochtend douchen")
else:
    print("")
    print("let op hoofdletters! maar ik ga wel verder")
print("")
time.sleep(1)

#uitleg vraag 3
print("oké je bent nu beneden en ga ontbijten \nwat neem je als ontbijt?")
print("A. muslie \nB. lekker een boterham \nC. geen ontbijt")
print("")

#systeem om vraag 3 antwoorden te laten geven
ontbijt = input("A of B of C(let op hoofdletters): ")
if ontbijt == "A":
    print("")
    print("lekker moet je doen")
elif ontbijt == "B":
    print("")
    print("altijd goed")
elif ontbijt == "C":
    print("")
    print("niet goed voor je hè, maar ja")
else:
    print("")
    print("let op hoofdletters! maar ik ga wel verder")
print("")
time.sleep(1)

#uitleg vraag 4
print("zo je hebt net lekker ontbeten (of niet) \nhoe ga je vandaag naar school toe")
print("A. fiets \nB. openbaar vervoer \nC. auto")
print("")

#systeem om vraag 4 antwoorden te laten geven
reis = input("A of B of C(let op hoofdletters): ")
if reis == "A":
    print("")
    print("gezond lekker fietsen (of je woont dicht bij school)")
elif reis == "B":
    print("")
    print("Ja lekker zitten terwijl je naar je locatie wordt gebracht")
elif reis == "C":
    print("")
    print("lekker door je moeder op school worden afgezet")
else:
    print("")
    print("let op hoofdletters! maar ik ga wel verder")
print("")
time.sleep(1)

#uitleg vraag 5
print("zo je bent op school aangekomen en loopt naar je klas \nga je voor of achterin van de klas zitten?")
print("A. voorin \nB. achtering")
print("")

#systeem om vraag 5 antwoorden te laten geven
zitten = input("A of B (let op hoofdletters): ")
if zitten == "A":
    print("")
    print("ja je mag de docent wel? of moet je voorin zitten van de docent?")
elif zitten == "B":
    print("")
    print("lekker een beetje klooien achterin, kan geen kwaad toch")
else:
    print("")
    print("let op hoofdletters! maar ik ga wel verder")
