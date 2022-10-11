from random import randrange
from time import sleep

def fin_print():
    for x in range(5):
        print("**********")
        print("***",randrange(0,101),"***")
        print("**********")
        sleep(0.5)

fin_print()