print("-----First List------")
firstList= ["Sheep", "Pig", "Cow","Chicken", "Horse", "Cat"]
secondList = firstList[:]
secondList.append("Bulls")
secondList.append("Llama")
secondList.append("Dog")
secondList.append("Cattle")
secondList.sort()
firstList.sort()
print(firstList)

print("-----Second List------")
print(secondList)


print("The first three items in the list are:", secondList[:3])
print("Three items from the middle of the list are:", secondList[3:6])

print("The last three items in the list are:", secondList[-3:])