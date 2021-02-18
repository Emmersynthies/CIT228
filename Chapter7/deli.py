print("******7-8*******")
sandwich_order = ["tuna", "BLT", "grilled cheese", "ruben", "pastrami","salami","turkey","pastrami"]
finished_sandwich = []

while sandwich_order:
    sandwich = sandwich_order.pop()
    
    print(f"Making Sandwiches: {sandwich.title()}")
    finished_sandwich.append(sandwich)
    
print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwich:
    print(finished_sandwich.title())



print("******7-9*******")
sandwich_order = ["tuna", "BLT", "grilled cheese", "ruben", "pastrami","salami","turkey","pastrami"]
finished_sandwich = []

while "pastrami" in sandwich_order:
    sandwich_order.remove("pastrami")
while sandwich_order:
    sandwich = sandwich_order.pop()
    
    print(f"Making Sandwiches: {sandwich.title()}")
    finished_sandwich.append(sandwich)
    
print("\nThe following sandwiches are finished:")
for finished_sandwich in finished_sandwich:
    print(finished_sandwich.title())