print("------------3-4-----------")
guestList= ["Melissa McCarthy","Matthew McConaughey","Jennifer Hewitt"]
print(guestList[0],", can you make it to dinner on Thursday?")
print(guestList[1],", can you make it to dinner on Thursday?")
print(guestList[2],", can you make it to dinner on Thursday?")

print("------------3-5-----------")
print(guestList[2],", can't make it to dinner.")
guestList[2] = "Liam Neeson"
print(guestList[0],", can you make it to dinner on Thursday?")
print(guestList[1],", can you make it to dinner on Thursday?")
print(guestList[2],", can you make it to dinner on Thursday?")

print("------------3-6-----------")
print("Got a new table, extending the new guestList")
print("The number of items in your list is: ",len(guestList))
guestList.insert(0,"Jennifer Aniston")
guestList.insert(2,"David Schwimmer")
guestList.insert(4,"Courteney Cox")

print(guestList[0],", can you make it to dinner on Friday?")
print(guestList[1],", can you make it to dinner on Friday?")
print(guestList[2],", can you make it to dinner on Friday?")
print(guestList[3],", can you make it to dinner on Friday?")
print(guestList[4],", can you make it to dinner on Friday?")
print(guestList[5],", can you make it to dinner on Friday?")

print("------------3-7-----------")

print("Sorry to say but I can only invite 2 people. My dinner table is late.")

guestList.pop(2)
print(guestList[2],",So sorry but I can't invite you to dinner. Maybe another time?")
guestList.pop(3)
print(guestList[3],",So sorry but I can't invite you to dinner. Maybe another time?")
guestList.pop(4)
print(guestList[4],",So sorry but I can't invite you to dinner. Maybe another time?")
guestList.pop(5)
print(guestList[5],",So sorry but I can't invite you to dinner. Maybe another time?")

print(guestList[0],", Hope you are still able to make it?")
print(guestList[1],", Hope you are still able to make it?")

del guestList[0]
del guestList[1]
print(guestList)