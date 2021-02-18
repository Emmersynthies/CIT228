number =int(input("Please enter a number, and I'll tell you if it can be multiple by 10: "))


if number % 10 == 0:
    print(f"\nThe number", number, " is multiple of 10.")
else:
    print(f"\nThe number ", number, "is not multipled by 10.")