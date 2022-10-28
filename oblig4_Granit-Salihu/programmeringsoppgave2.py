from random import randrange
import blackjack_module as bjm
card_list = bjm.get_new_shuffled_deck()

def draw_card():
    card_name = card_list[randrange(0, len(card_list))]
    card_number = bjm.get_card_value(card_name)
    card_list.remove(card_name)
    return {"navn":card_name, "verdi":card_number}


def dealer_draw_card():
    dealer_card = draw_card()
    global dealer_value
    dealer_value = dealer_value + dealer_card["verdi"] 
    dealer_hand.append(dealer_card["navn"])


def player_draw_card():
    player_card = draw_card()
    global player_value
    player_value = player_value + player_card["verdi"] 
    player_hand.append(player_card["navn"])

def playagain():
    play_again = print(input("Would you like to play again? (Y/N)"))
    if play_again == "Y" or play_again == "y":
        return "y"




while True:
    #Player values
    player_hand = []
    dealer_hand = []
    player_value = 0
    dealer_value = 0

    #Draw cards
    while len(player_hand) < 2:
        player_draw_card()
    while len(dealer_hand) < 2:
        dealer_draw_card()

    #Game flow
    if dealer_value >= 21 or player_value >= 21:
        print(f"Dealer has {dealer_hand} with a combined value of {dealer_value}")
        print(f"You have {player_hand} with a combined value of {player_value}")
        bjm.print_result(dealer_value,player_value)
        if playagain().lower() == "y":
            continue
        else:
            break
    elif dealer_value or player_value < 21:
        print(f"Dealer has a {dealer_hand[0]}")
        print(f"You have {player_hand} with a combined value of {player_value}")
        print("1- Hit \n2- Stand" )
        player_choice = input()
        if player_choice == "1":
            print("You chose to Hit")
            player_draw_card()
            dealer_draw_card()
        elif player_choice == "2":
            print("You chose to Stand")
            print(f"You had {player_hand} with a value of {player_value}")
            print(f"Dealer had {dealer_hand} with a value of {dealer_value}")
            bjm.print_result(dealer_value,player_value)
            if playagain() == "y":
                continue
            else:
                break