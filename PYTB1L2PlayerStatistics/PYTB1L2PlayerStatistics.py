#maakt variablen met de stats van de player
name = "Aidan"
weight = "medium"
length = "1,80"
doublejump = True
charactertype = "defender"
accuracy = "[██████-----]"
speed = "       [████████---]"
sneek = "       [███--------]"
healt = "      [██████-----]"

#laat de stats zien van de player
print("name: " , name)
print("size: " , weight)
print("length: " , length)
print("class: " , charactertype)
print("ability to doublejump: " , doublejump)
print ("health: " , healt)
print("gun accuracy: " , accuracy)
print("speed: " , speed)
print("sneak: " , sneek)
print(" ")
#klein grapje met dat je het karater kan kiezen of niet maar het komt nooit tot een game
kiezen = input("press A to choose or B to denie:")
if kiezen == "A":
    print(" ")
    print("lets go")
    print(" ")
    print("couldn't find a game...")
elif kiezen == "B":
    print(" ")
    print("failed to load more characters for the game :(")
else:
    print(" ")
    print("or not")
