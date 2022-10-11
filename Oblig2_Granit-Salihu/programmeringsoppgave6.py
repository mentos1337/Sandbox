Pakkeliste = []
Pakkelisteprogram = True
print("==== Valg alternativer ===="), print("|Legge til i pakkeliste   1|"), print("|Slette fra pakkeliste    2|"), print("|Printe pakkeliste        3|"), print("|Avslutte pakkeliste      4|")

while Pakkelisteprogram == True:
    user_input = int(input())
    if user_input == 1:
        print(("Hva vil du legge til?: "))
        Pakkeliste.append(input())
        print("Nåværende liste:", Pakkeliste)
        print("==== Valg alternativer ===="), print("|Legge til i pakkeliste   1|"), print("|Slette fra pakkeliste    2|"), print("|Printe pakkeliste        3|"), print("|Avslutte pakkeliste      4|")
    elif user_input == 2:
        print("Hva vil du fjerne?: ")
        Pakkeliste.remove(input())
        print("Nåværende liste:", Pakkeliste)
        print("==== Valg alternativer ===="), print("|Legge til i pakkeliste   1|"), print("|Slette fra pakkeliste    2|"), print("|Printe pakkeliste        3|"), print("|Avslutte pakkeliste      4|")
    elif user_input ==3:
        print(Pakkeliste)
        print("==== Valg alternativer ===="), print("|Legge til i pakkeliste   1|"), print("|Slette fra pakkeliste    2|"), print("|Printe pakkeliste        3|"), print("|Avslutte pakkeliste      4|")
    elif user_input == 4:
        print("Pakkelisten er nå avsluttet")
        print("Din pakkeliste:", Pakkeliste)
        print("God tur")
        Pakkelisteprogram = False
    else:
        print("Ikke en valgmulighet, prøv igjen"), print("==== Valg alternativer ===="), print("|Legge til i pakkeliste   1|"), print("|Slette fra pakkeliste    2|"), print("|Printe pakkeliste        3|"), print("|Avslutte pakkeliste      4|")