class Restaurant:
    def __init__(self, restaurant_name,cusine_type,number_served = 0):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = number_served
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cusine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")
    def set_number_served(self,served):
        self.number_served = served
    def increment_number_served(self, served):
        self.number_served += served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cusine_type, flavour = [], number_served=0):
        super().__init__(restaurant_name, cusine_type, number_served)
        self.flavour = flavour
    def describe_icecream_falvors(self):
        print("We have these flavours available")
        for flav in self.flavour:
            print(flav)

if __name__ == "__main__":
    italiano = Restaurant("Italiano","Italian")
    Indian = Restaurant("Curry","Indian")
    Sweburger = Restaurant("Sweburger", "Fast food")
    print()
    Indian.describe_restaurant()
    italiano.describe_restaurant()
    Sweburger.describe_restaurant()
    print()
    mexicano = Restaurant("Mexicano","Mexican")
    print("Number served",mexicano.number_served)
    print()
    mexicano = Restaurant("Mexicano", "Mexican", 54)
    print("Number served",mexicano.number_served)
    print()
    mexicano.set_number_served(15)
    print("Number served",mexicano.number_served)
    mexicano.increment_number_served(15)
    print("Number served",mexicano.number_served)
    print()



    lots_of_ice = IceCreamStand("Lots of ice","Ice Cream",["Chocolate","Strawberry","Vanilla"])

    lots_of_ice.describe_icecream_falvors()