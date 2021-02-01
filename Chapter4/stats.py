import random

number = random.randrange(10,100)
numList = list(range(number))
print(numList)

print("Largest number: ", max(numList))
print("Smallest number: ", min(numList))
print("Total numbers: ", sum(numList))
print("The average number: ", sum(numList)/len(numList))
