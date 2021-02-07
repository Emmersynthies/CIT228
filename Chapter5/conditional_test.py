
number1= 10
number2= (3)
number3= 5
number4= 11
color = ("Purple", "pink")
food = "Steak"
animal= ("tiger", "pig")


print("-------True Tests--------")

print("pink" in color)
print(number3,"<",number4,"and", number1,"<", number4)
print(color[1],"==", color[1])
print("steak ==steak", food.lower()=="steak") 
print(number1,">=", number2)
"Purple" in color

print("---------False Tests--------")
print(number1,"=<", number2, "or", number3,"=<", number2) 
print("pink","!=", "Purple")
print(number1,"=<", number3)
if color != "yellow":
    print("Yellow is in color list")
print("tiger" in food)