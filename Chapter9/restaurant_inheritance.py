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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant, cuisine='ice_cream'):
        super().__init__(restaurant, cuisine)
        self.flavors = []

    def show_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor}")
        print("\nThere are so many flavors available:")

print("*******9-6*********")

restaurant = IceCreamStand('the cold cup')
restaurant = ["sherbert", 'vanilla', "Cookies n Cream", "pistachio", "cupcake"]
  

