print("Enter 's' to STOP.\n")

while True:
    try:
        x = input("\nEnter first number: ")
        if x == 's':
            break

        x = int(x)

        y = input("Enter second number: ")
        if y == 's':
            break

        y = int(y)

    except ValueError:
        print("Sorry, ERROR.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")
        print("Thanks for playing! Enter 's' to STOP.\n")   
    
   
        
    