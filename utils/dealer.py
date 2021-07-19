# @TODO Move methods that are not for dealer in another files (if needed)
def sum_of_card(cards_holding):
    sum_of_cards = sum(card.card_value for card in cards_holding)
    number_of_aces = 0

    # Searching for "ACE"
    for ace in cards_holding:
        if "Ace" in ace.rank:
            number_of_aces += 1

    if sum_of_cards <= 11 and number_of_aces == 1:
        return sum_of_cards + 10
    elif sum_of_cards <= 21 and number_of_aces > 1:
        return sum_of_cards + 11
    else:
        return sum_of_cards


def cards_show(player, player_show, dealer_show, dealer_to_show=-1):
    print('\n')

    for p_card in player_show:
        print(f"{player.name} hes = {p_card.suit} - {p_card.rank}")
    else:
        print(f"and sum of all cards in hand is = {sum_of_card(player_show)}")

    print('\n')

    for d_card in dealer_show[:dealer_to_show]:
        print(f"Dealer hes = {d_card.suit} - {d_card.rank} ")
    else:
        print(f"Dealer card value = {sum_of_card(dealer_show[:dealer_to_show])}\n")


def round_repeat():
    return int(input("if you want to hit for another card press (1) or (0) for stand = "))


def game_repeat():
    return int(input("if you want to play for another round (1) or (0) for stand = "))


def _human_player(player_cards, dealer_cards, coin_price):
    if sum_of_card(player_cards) == 21:
        clr()
        print("\nBlackJACK, u win!")
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        player.win_round_money(coin_price, 0.5)
        return False

    elif sum_of_card(player_cards) > 21:
        clr()
        print("\nBUST, Game over, DEALER WIN")
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        player.lose_round_money(coin_price)
        return False
    else:
        return True

def _pc_player(player_cards, dealer_cards, coin_price):
    if sum_of_card(dealer_cards) > 21 >= sum_of_card(player_cards):
        clr()
        print("\nPlayer win, dealer bust")
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        player.win_round_money(coin_price)
        return False
    elif sum_of_card(dealer_cards) > sum_of_card(player_cards):
        clr()
        print("\nDealer win!")
        player.lose_round_money(coin_price)
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        return False
    elif sum_of_card(player_cards) < sum_of_card(dealer_cards) <= 21:
        clr()
        print("\nDealer win")
        player.lose_round_money(coin_price)
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        return False
    elif sum_of_card(dealer_cards) == sum_of_card(player_cards):
        clr()
        print('\nPASS')
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        return True

# win bust blackjack pass
def win_lose_pass(player, dealer_cards, player_cards, coin_price, before_stand=True):
    if before_stand:  # Human playe
        _human_player(player_cards, dealer_cards, coin_price)  # And the same for PC player
     else:  # PC player
        _pc_player(player_cards, dealer_cards, coin_price)  # This is the way to spliit logic into smaller pieces


def clr(lines=10):
    print('\n' * lines)