import random
import os
filename = "Chapter10/guests.txt"
if os.path.exists(filename):
    os.remove(filename)
room=[]
with open(filename, 'w') as guestFile:
    guest = input("What's your name(s to stop)? ")
    while guest != "s":
        number=random.randint(1,50)
        while number in room:
            number=random.randint(1,50)
        print(f"{guest} your room# is {number}")
        room.append(number)
        guest+=", room#" + str(number) + "\n"
        guestFile.write(guest)
        guest = input("What's your name(s to stop)? ")
with open(filename) as guestFile:
    print("---Guest Name----")
    for line in guestFile:
        print(line)
        