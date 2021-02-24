class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print (f"{self.restaurant_name} has amazing {self.cuisine_type}.")
        

    def open_restaurant(self):
        print (f"{self.restaurant_name} is very welcoming and always open!")
        
print("*******9-1*********")

restaurant = Restaurant("Chuck Wagon", "pizza")
print("The best ", restaurant.cuisine_type)
print(" is located in ludington at ", restaurant.restaurant_name )

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("********9-2*********")

restaurant = Restaurant("Olive garden", "Italian")
restaurant.describe_restaurant()

restaurant = Restaurant("Texas Roadhouse", "American")
restaurant.describe_restaurant()

restaurant = Restaurant("On the border", "Mexican")
restaurant.describe_restaurant()






