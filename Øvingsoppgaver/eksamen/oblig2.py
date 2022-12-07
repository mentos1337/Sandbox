import random

tall = int(input("Hva er meningen med livet? "))
if tall == 42:
    print("Det stemmer, meningen med livet er 42!")
elif tall >= 30 and tall <= 50:
    print("Nærme men feil")
else:
    print("FEIL")

for oddetall in range(9,101,2):
    print(oddetall)

oddetall = 9

while oddetall <= 101:
    print(oddetall)
    oddetall += 2


tolkein = ["The Hobbit","Farmer Giles Of Ham","The Fellowship of the Ring","The Two Towers","The Return of the King","The Adventures of Tom Bombadil","Tree and Leaf"]
print(tolkein[0:2])
print(tolkein[5:7])

tolkein.append("The Silmarillion")
tolkein.append("Unfinished Tales")
tolkein[0] = ["Lord of the Rings The Hobbit"]
tolkein[2] = ["Lord of the Rings The Fellowship of the Ring"]
tolkein[4] = ["Lord of the Rings The Return of the King"]
tolkein.sort
print(tolkein)

tomlist = []

for boker in tolkein:
    if "Lord of the Rings The Return of the King" in boker:
        tomlist.append(boker)
    elif "Lord of the Rings The Hobbit" in boker:
        tomlist.append(boker)
    elif "Lord of the Rings The Fellowship of the Ring" in boker:
        tomlist.append(boker)

for books in tomlist:
    print(books)

score = 0
for kast in range(3):
    score += random.randrange(0,61)

print(score)

score2 = 0
for piler in range(int(input("spillere? "))):
    for kast in range(3):
        score2 += random.randrange(0,61)
    print(score2)

x = True
package = []
while x == True:
    print("(s)top (a)dd (r)emove (p)rint list")
    userinput = input()
    if userinput == "s":
        x = False
    elif userinput == "a":
        package.append(input())
    elif userinput == "r":
        package.remove(input())
    elif userinput == ("p"):
        print(package)