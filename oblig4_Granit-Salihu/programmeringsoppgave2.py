class moneyHandler:
    def __init__(self, money):
        self.money = money
    def moneyAdd(self,x):
        x + self.money
    def moneySubtract(self,x):
        x - self.money

class cardHandler:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def cardRand(self):
        print(f"You drew {self.value} of {self.type}")
    def cardPoints(self):
        return self.value + self.value