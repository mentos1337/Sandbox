from random import randrange
from time import sleep

antall_darts = int(input("Antall kast per spiller? "))
resultat = 0
spiller = 0


for antall_spillere in range(int(input("Hvor mange spillere?: "))):
    for rng in range(antall_darts):
        dice = randrange(0,6)
        if dice == 0:
            resultat += 0
        elif dice == 1:
            resultat += randrange(1,20)            
        elif dice == 2:
            resultat += randrange(1,20) * 2
        elif dice == 3:
            resultat += randrange(1,20) * 3
        elif dice == 4:
            resultat += 25
        elif dice == 5:
            resultat += 50
    spiller += 1
    print("Spiller", spiller, "poengsum =", resultat)
    resultat = 0
    sleep(0.5)
