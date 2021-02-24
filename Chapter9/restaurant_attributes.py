class Restaurant:
    def __init__(self,restaurant_name,cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print (f"{self.restaurant_name} has amazing {self.cuisine_type}.")
        
    def open_restaurant(self):
        print (f"{self.restaurant_name} is very welcoming and always open!")
    
    def set_number_served(self, served):
        self.number_served=int(served)

    def increment_number_served(self, served):
        self.number_served += int(served)

print("*******9-4*********")

restaurant = Restaurant("Chuck Wagon", "pizza", 10)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("Customers initially served is ", restaurant.number_served)
restaurant.number_served=25
print("New number of customers is ", restaurant.number_served)
served=input("What is the number of customers you've served?")
restaurant.set_number_served(served)
print("Customers initially served is ", restaurant.number_served)
served=input("What is the additional number of customers you've served?")
restaurant.increment_number_served
print("Total number of customers served is ", restaurant.number_served)