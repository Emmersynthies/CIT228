import random
counter=0
numberCorrect=0
numberWrong=0
while counter < 10:
    randNumber1= random.randrange(1,1000)
    randNumber2=random.randrange(1,1000)
    correctAnswer = int(randNumber1+randNumber2)
    yourAnswer = int(input(f"what is the integar value of {randNumber1}+{randNumber2}?"))
    if correctAnswer == yourAnswer:
        print("Great job, you answered correctly!")
        numberCorrect +=1
    else:
        print("Oops, the correct answer is ",correctAnswer)
    counter+=1
    print("Oops, Thats wrong ", numberWrong)
    
        if yourAnswer == numberWrong:
            print(numberWrong)
            break
            
        else:
            print(numberWrong>5, "please see a tutor.")
        numberWrong+=1
           


print("You answered", numberCorrect, "question correctly!")
print("You answered", numberWrong, "question wrong!")
print("Thanks for playing!")