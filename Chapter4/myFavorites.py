food = ["soup", "salmon", "pull pork", "sushi", "chicken", "ham"]
number =[1,7,14,23,56,72]
movies = ["Fast & Furious", "Mr. Right", "Snowden"]
favorite= ["salmon", "pull pork",7,14,"Mr. Right", "Snowden"]
print("--------------#1----------------------")
print (food)
print (number)
print (movies)
print (favorite)

print (food[-1])
print("2nd =", number[1])
print("4th =", number[3])
print("6th =", number[5])
print (movies[0])
print (movies[1])
print (movies[2])
print ("First food, first number, first movie=", favorite[0],favorite[2],favorite[4])
print("--------------#2----------------------")

movies.append("fluke")
print(movies)

number.insert(3,82)
print ("item added to 3 ", number)

food.insert(5,"smoothies")
print("item added to 5 ", food)

del food[0]
print(food)

number.pop()
print("deleted a number from the end",number)

number.pop(2)
print("deleted #2" ,number)

print("--------------#3----------------------")

movies.sort()
print("Sorted movies", movies)

food.sort()
print("Sorted movies", food)

print("temp sort", sorted(number))
print(number)

movies.reverse()
print("Reversed sorting", movies)

print("-----------Chapter 4, #1-------")

print ("Food List")
print ("-----------------------")
for things in food:
    print (things)

print ("Number List")
print ("-----------------------")
for things in number:
    print (things)


print ("Movie List")
print ("-----------------------")
for things in movies:
    print (things)

print ("Favorites List")
print ("-----------------------")
for things in favorite:
    print (things)