#random importen om iedereen een random volgorde te geven
import random
#een list met alle mensen
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
#hier husselt hij ze door elkaar
random.shuffle(people)
#maakt een waldo variabel niet echt nodig maar wel handig
Waldo = "Waldo"

#maakt i 0 voor een while loop 
i = 0
#kijkt naar hoeveel mensen er in de list zitten
length = len(people)
#maakt een while loop zolang length korter is als i
while i < length:
    #als waldo in de list zit doe
    if Waldo == people[i]:
        #kijk welke stoel hij zit
        seat = people.index(Waldo)
        #print welke stoel hij zit +1 voor het tellen vanaf 1
        print("seat : "+ str(seat+1))
    #als hij door de loop heen komt maakt het i 1 zodat hij stopt
    i+=1
#laat zien wat de volgorde was
print(people)
