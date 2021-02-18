import random
problems=int(input("How many math problems would you like to practice?"))
keepGoing = True
numberCorrect=0
while keepGoing != "g":
    randNumber1= random.randrange(1,1000)
    randNumber2=random.randrange(1,1000)
    correctAnswer = int(randNumber1+randNumber2)
    yourAnswer = int(input(f"what is the integar value of {randNumber1}+{randNumber2}?"))
    if correctAnswer == yourAnswer:
        print("Great job, you answered correctly!")
        numberCorrect +=1
    else:
        print("Oops, the correct answer is ",correctAnswer)
    if keepGoing:
        print("Would you like to keep playing? Type a g to leave, any key to keep going...")

print("You answered", numberCorrect, "question correctly!")
print("Thanks for playing!")