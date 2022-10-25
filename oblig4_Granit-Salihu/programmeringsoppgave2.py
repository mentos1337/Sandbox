from random import randrange
import blackjack_module as bjm
card_list = bjm.get_new_shuffled_deck()
player_hand = []
player_value = 0
dealer_hand = []
dealer_value = 0

def dealer_draw_card():
    card_name = card_list[randrange(0, len(card_list))]
    card_number = bjm.get_card_value(card_name)
    dealer_hand.append(card_name)
    dealer_value += card_number



dealer_draw_card()
print(dealer_hand,dealer_value)

# if player_value == 21:
#     print("Du har blackjack")
# elif player_value > 21:
#     print("1- Hit")
#     print("2- Stand")
#     player_choice = input()
#     print(f"You chose to {player_choice}")
#     if player_choice == 1:
#         print("cool")
#     elif player_choice == 2:
#         print(f"Dealer had {dealer_hand} with a value of {dealer_value}")