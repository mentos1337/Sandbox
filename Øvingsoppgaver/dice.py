from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_dice(self,kast):
        for kas in range(kast):
            print(randint(1,self.sides))

terning10 = Die(10)
terning20 = Die(20)
terning10.roll_dice(10)
terning20.roll_dice(20)