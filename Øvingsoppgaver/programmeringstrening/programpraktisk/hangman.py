import random

#liste med ord
words = ["Apekatt", "Sushi", "Kebab", "Armadillo"]

#tar et random ord fra lista
wordToGuess = words[random.randrange(0, len(words))]

#lager liste av ordet
wordToGuessList = list(wordToGuess)

#lager string (_) ut av ordet som ble valgt ut
hint = ["_"] * len(wordToGuess)

lives = 6

while "_" in hint and lives > 0:
    print("".join(hint).capitalize())
    print("liv igjen", lives)
    guessLetter = input("Guess a letter: ")
    if not guessLetter.isalpha():
        print("You cannt guess anything other than letters")
        continue

    for character in guessLetter:
        if guessLetter.lower() in wordToGuess.lower():
            for index in range(len(wordToGuessList)):
                if guessLetter.lower() == wordToGuessList[index].lower():
                    hint[index] = guessLetter
        else:
            lives -= 1

    if "_" not in hint:
        print(f"Du vant med {lives} liv igjen")
        print(f"du gjettet ordet riktig {wordToGuess}")
    elif lives == 0:
        print(f"Du tapte med {lives} liv igjen")
        print(f"Du gjettet: {''.join(hint).capitalize()}")
        print(f"du gjettet ordet feil ordet var: {wordToGuess}")