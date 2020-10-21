
import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
Waldo = "Waldo"

#matched_indexes = []
i = 0
length = len(people)
while i < length:
    if Waldo == people[i]:
        seat = people.index(Waldo)
        print("seat : "+ str(seat+1))

    i+=1

print(people)
#
#        matched_indexes.append(i)
#    i += 1
#if 'Waldo' in people :
#    print(f'{Waldo} zit op plaats {matched_indexes} \nde zit plaatsen \n{people}')

#else :
#    print("wacht waar is hij heen?")
#
