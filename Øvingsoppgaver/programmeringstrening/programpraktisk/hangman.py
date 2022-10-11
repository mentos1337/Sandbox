from operator import index, indexOf
import random
from tkinter import INSERT

words = ["Apekatt", "Sushi", "Kebab", "Armadillo"]

wordToGuess = words[random.randrange(0, len(words))]
wordToGuessList = list(wordToGuess)
print(wordToGuessList)
hint = ["_"] * len(wordToGuess)
print(hint)
print()

lives = 6

while "_" in hint and lives >= 1:
    print("".join(hint).capitalize())
    print("liv igjen", lives)
    guessLetter = input("Guess a letter: ") 
    if guessLetter.lower() in wordToGuessList:
        for index in range(len(wordToGuessList)):
            if guessLetter.lower() == wordToGuessList[index].lower():
                hint[index] = guessLetter
    else:
        lives -= 1