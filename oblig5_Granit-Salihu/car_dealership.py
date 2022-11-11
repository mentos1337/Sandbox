from datetime import date 
class car_register1:
    def __init__(self,car,brand,model,price,year,month,new,km):
        self.car = car
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km
        def print_car_information(self):
            pass
        def get_car_age(self):
            "holder også å bruke print(car.age)"
            pass
        def rent_car_monthly_price(self):
            pass
        def next_eu_control(self):
            pass
        def calculate_total_price(self):
            pass


car_register = { 
    "toyotaBZ4X": { 
            "brand": "Toyota", 
            "model": "Corolla", 
            "price": 96_000, 
            "year": 2012, 
            "month": 8, 
            "new": False, 
            "km": 163_000 
    }, 
    "pugeot408": { 
            "brand": "Pugeot", 
            "model": "408", 
            "price": 330_000, 
            "year": 2019, 
            "month": 1, 
            "new": False, 
            "km": 40_000 
    }, 
    "audiRS3": { 
            "brand": "Audi", 
            "model": "RS3", 
            "price": 473_000, 
            "year": 2022, 
            "month": 2, 
            "new": True, 
            "km": 0 
    }, 
}
 
NEW_CAR_REGISTRATION_FEE = 8745 
RENT_CAR_PERCENTAGE = 0.4 
RENT_NEW_CAR__FEE = 1000 
 
    # Oppgave 3.1 
def print_car_information(car): 
    for key in car:
        print("{}: {}".format(key,car[key]))



def create_car(car_register, brand, model, price, year, month, new, km):
    car_register["{}{}".format(brand,model)] = {"brand":brand, "model":model,"price":price,"year":year,"month":month,"new":new,"km":km}
    return car_register


    #Oppgave 3.3
def get_car_age(car): 
    today_year = date.today()
    car_age = car["year"]
    return today_year.year - car_age



    # Oppgave 3.4 
def next_eu_control(car):
    dagens = date.today()
    car_age = date(car["year"],car["month"],1)
    while dagens >= car_age:
        car_age = car_age.replace(year = car_age.year + 2)
        return car_age

    # Oppgave 3.5 
def rent_car_monthly_price(car): 
    if car["new"] == True:
        return round(car["price"] / 12 * 0.4 + 1000,2)
    else:
        return round(car["price"] / 12 * 0.4,2)

print("Monthly price: ",rent_car_monthly_price(car_register["toyotaBZ4X"]))

    # Oppgave 3.6 
def calculate_total_price(car): 
    if car["new"] == True:
        return car["price"] + 10783
    elif get_car_age(car) >= 0 and get_car_age(car) <= 3:
        return car["price"] + 6681
    elif get_car_age(car) >= 4 and get_car_age(car) <= 11:
        return car["price"] + 4034
    elif get_car_age(car) >= 12 and get_car_age(car) <= 29:
        return car["price"] + 1729
    else:
        return car["price"]

 
def is_new(car): 
    return car['new'] 
 
if __name__ == '__main__': 
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0) 
 
 
toyota = car_register['toyotaBZ4X'] 
 
print_car_information(toyota) 

print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.") 
print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}") 
print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.") 
print()
print()
audi = car_register['audiRS3'] 

print_car_information(audi) 

print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.") 
print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}") 
print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")