Store = ["Tomatos", "Apples", "Beef","Pork","Chicken","Chips","Dip", "Plates","Paper towels","Soup","Eggs"]
print(Store)

Store.append("Peaches")
print(Store)

Store.insert(3,"Bread")
print(Store)
Store.insert(5,"Rolls")
print(Store)

del Store[2]
print(Store)

Store.pop()
print(Store)

Store.sort()
print(Store)

print(sorted(Store))
print(Store)

Store.reverse()
print(Store)

removedStore = 'Apples'
Store.remove(removedStore)
print(Store)
print(removedStore)


print("the list of items left", len(Store))