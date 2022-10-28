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


def calculate_result(dealer, player, bet_amount, player_coin):
    if player > dealer and player <= 21:
        print("Player won")
        if player == 21:
            return (bet_amount * 2) + player_coin
        else:
            return bet_amount + player_coin
    elif dealer > player and dealer > 21:
        print("Player won")
        return bet_amount + player_coin
    elif player == dealer:
        print("No one won")
    elif dealer > player and dealer <= 21:
        print("Dealer won")
        return player_coin - bet_amount
    elif player > dealer and player > 21:
        print("Dealer won")
        return player_coin - bet_amount
    elif dealer > 21:
        print("Dealer has more than 21 and lost\nPlayer Won")
        return bet_amount + player_coin

def play_again():
    while True:
        ask = input("Would you like to play again? (Y/N)").lower()

        if ask == "y":
            print("Playing a new game! ")
            break
        elif ask == "n":
            print("You have chosen to exit the game, Good Bye! ")
            exit()
        else:
            print("Please enter yes or no!")
    return True

while True:
    global isAce
    #Player values
    player_hand = []
    dealer_hand = []
    player_value = 0
    dealer_value = 0
    player_coin = 5
    while player_coin > 0:
        print(f"You have {player_coin} Coins")
        bet_amount = int(input("How much would you like to bet? "))
        if player_coin < 0 or player_coin < bet_amount:
            print("You don't have enough coins")
            break
        #Draw cards
        while len(player_hand) < 2:
            player_draw_card()
        while len(dealer_hand) < 2:
            dealer_draw_card()

        #Game flow
        if dealer_value > 21:
            if any("Ace" in s for s in dealer_hand):
                dealer_value -= 10
                continue
        if player_value > 21:
            if any("Ace" in s for s in player_hand):
                player_value -= 10
                continue
        if dealer_value >= 21 or player_value >= 21:
            print(f"Dealer has {dealer_hand} with a combined value of {dealer_value}")
            print(f"You have {player_hand} with a combined value of {player_value}")
            player_coin = calculate_result(dealer_value, player_value, bet_amount, player_coin)
            break

        elif dealer_value < 21 and player_value < 21:
            print(f"Dealer has a {dealer_hand[0]}")
            print(f"You have {player_hand} with a combined value of {player_value}")
            print("1- Hit \n2- Stand" )
            player_choice = input()
            if player_choice == "1":
                print("You chose to Hit")
                player_draw_card()
                while dealer_value < 17:
                    dealer_draw_card()
                    if dealer_value > 17:
                        continue
            elif player_choice == "2":
                while dealer_value < 17:
                    dealer_draw_card()
                    continue
        print("You chose to Stand")
        print(f"You had {player_hand} with a value of {player_value}")
        print(f"Dealer had {dealer_hand} with a value of {dealer_value}")
        player_coin = calculate_result(dealer_value, player_value, bet_amount, player_coin)


        if play_again():
            player_hand = []
            dealer_hand = []
            player_value = 0
            dealer_value = 0
            continue
