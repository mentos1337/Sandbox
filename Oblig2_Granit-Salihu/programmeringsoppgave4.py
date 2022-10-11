bok_liste = []

bok_liste.append ("Lord of the rings: The Fellowship of the Ring"), ("Lord of the rings: The Two Towers"), ("Lord of the rings: The Return of the King")
bok_liste.append ("Lord of the rings: The Two Towers")
bok_liste.append ("Lord of the rings: The Return of the King")
print("============ Alternativ 1 ============")
for triology in bok_liste:
    print(triology)

print("============ Alternativ 2 ============")
for bokstavprint in "Lord of the rings: The Fellow ship of the Ring":
    print([bokstavprint])   #brackets fordi det er kult

print("============ Alternativ 3 ============")
for spesifikstop in bok_liste:
    print(spesifikstop)
    if spesifikstop == "Lord of the rings: The Two Towers":
        break

print("============ Alternativ 4 ============")
for listeskip in bok_liste:
    if listeskip == "Lord of the rings: The Two Towers":
        continue
    print(listeskip)