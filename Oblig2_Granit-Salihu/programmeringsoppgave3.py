bok_liste = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

print("De to første og de to siste bøkene:", {bok_liste [0]}, {bok_liste [1]}, {bok_liste [5]}, {bok_liste [6]})

bok_liste.append ("The Silmarillion ") 
bok_liste.append ("Unfinished Tales")
bok_liste [2] = "Lord of the rings: The Fellowship of the Ring"
bok_liste [3] = "Lord of the rings: The Two Towers"
bok_liste [4] = "Lord of the rings: The Return of the King"
bok_liste.sort()
print("Oppdatert bokliste:", (bok_liste))