from random import randrange
from time import sleep

resultat = 0
for en_spiller in range(3):
    resultat += randrange(0,61)
print("Poengsum =",resultat)


dynamisk_resultat = 0
Spiller = 0

for result in range(int(input("Hvor mange spillere?: "))):
    for rng in range(3):
        dynamisk_resultat += randrange(0,61)
    Spiller += 1
    print("Spiller", Spiller, "poengsum =", dynamisk_resultat)
    dynamisk_resultat = 0
    sleep(0.5)