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



game = True
#Game flow
while game == True:
    player_hand = []
    dealer_hand = []
    player_value = 0
    dealer_value = 0
    while len(player_hand) < 2:
        player_draw_card()
    while len(dealer_hand) < 2:
        dealer_draw_card()
    print(f"Dealer has a {dealer_hand[0]}")
    print(f"You have {player_hand} with a combined value of {player_value}")
    print("1- Hit \n2- Stand" )
    player_choice = input()
    if player_choice == "1":
        player_draw_card()
        if player_value == 21:
            print("Du har blackjack")
        elif player_value > 21:
            print("You busted")
        elif player_value < 21:
            print(player_value)
            print("1- Hit \n2- Stand" )
    elif player_choice == "2":
        print(f"You had {player_hand} with a value of {player_value}")
        print(f"Dealer had {dealer_hand} with a value of {dealer_value}")
        bjm.print_result(dealer_value,player_value)
        play_again = print(input("Would you like to play again? (Y/N)"))