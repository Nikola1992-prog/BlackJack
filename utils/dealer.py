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


def round_repeat():
    return int(input("if you want to hit for another card press (1) or (0) for stand = "))


def game_repeat():
    return int(input("if you want to play for another round (1) or (0) for stand = "))


def clr(lines=10):
    print('\n' * lines)
