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


def clr(lines=10):
    print('\n' * lines)


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


def win_lose_pass_before_stand(player, dealer_cards, player_cards, coin_price):
    if sum_of_card(player_cards) == 21:
        clr()
        cards_show(player, player_cards, dealer_cards, len(dealer_cards))
        print(f"\nBlackJACK, {player.name} wins!")
        player.win_round_money(coin_price, 0.5)
        return False
    elif sum_of_card(player_cards) > 21:
        clr()
        cards_show(player, player_cards, dealer_cards, len(dealer_cards))
        print("\nBUST, DEALER WINS")
        player.lose_round_money(coin_price)
        return False
    else:
        return True


def win_lose_pass_after_stand(player, dealer_cards, player_cards, coin_price):
    if sum_of_card(dealer_cards) > 21:
        clr()
        cards_show(player, player_cards, dealer_cards, len(dealer_cards))
        print(f"\n{player.name} wins, dealer bust!")
        player.win_round_money(coin_price)
        return False
    elif sum_of_card(dealer_cards) > sum_of_card(player_cards):
        clr()
        cards_show(player, player_cards, dealer_cards, len(dealer_cards))
        print("\nDealer Win")
        player.lose_round_money(coin_price)
        return False
    else:
        return True
