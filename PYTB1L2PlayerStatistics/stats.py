name = "Aidan"
weight = "medium"
length = "average"
doublejump = True
charactertype = "defender"
accuracy = "[██████-----]"
speed = "       [████████---]"
sneek = "       [███--------]"
healt = "      [██████-----]"

print("name: " , name)
print("size: " , weight)
print("class: " , charactertype)
print("ability to doublejump: " , doublejump)
print ("health: " , healt)
print("gun accuracy: " , accuracy)
print("speed: " , speed)
print("sneak: " , sneek)
print(" ")
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
