import blackjack_module as bjm

player_hand = {}
player_value = 0
dealer_hand = {}
dealer_value = 0

if player_value == 21:
    print("Du har blackjack")
elif player_value >= 21:
    print("1- Hit")
    print("2- Stand")
    player_choice = input()
    print(f"You chose to {player_choice}")
    if player_choice == 1:
        print("cool")
    elif player_choice == 2:
        print(f"Dealer had {dealer_hand} with a value of {dealer_value}")