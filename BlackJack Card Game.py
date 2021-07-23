from Players import Player, Dealer
from utils.dealer import clr, sum_of_card, win_lose_pass_after_stand
from utils.dealer import win_lose_pass_before_stand, cards_show
from ExceptionHandling.errors import player_input, coin_add, game_repeat, round_repeat, money_or_no_money

if __name__ == "__main__":

    player, money = player_input()
    player = Player(player, int(money))
    dealer = Dealer()
    black_jack_game = True

    while black_jack_game:  # at_game_is_on
        dealer.add_and_shuffle()
        player_cards_in_hand = []
        dealer_cards_in_hand = []

        coin_value = coin_add(player)

        if player.bank_acc < coin_value:
            add_more_money = money_or_no_money(player, coin_value)
            if not add_more_money:
                print(f"Thant you for playing this game, u can now withdraw {player.bank_acc}$ money ")
                black_jack_game = False
                break

        # dealer split cards
        for _ in range(2):
            player_cards_in_hand.append(dealer.deal_one())
            dealer_cards_in_hand.append(dealer.deal_one())

        # BlackJack, player win! - if dealer gives 21 in splitting cards
        cards_show(player, player_cards_in_hand, dealer_cards_in_hand)
        black_jack_game = win_lose_pass_before_stand(player, dealer_cards_in_hand, player_cards_in_hand, coin_value)
        if not black_jack_game:
            black_jack_game = game_repeat()
            continue
        hit_stand = round_repeat()

        # if player want another cards to add to his hand
        while hit_stand and black_jack_game:
            player_cards_in_hand.append(dealer.deal_one())
            clr()
            cards_show(player, player_cards_in_hand, dealer_cards_in_hand)
            black_jack_game = win_lose_pass_before_stand(player, dealer_cards_in_hand, player_cards_in_hand, coin_value)
            # pass ???
            if not black_jack_game:
                break
            hit_stand = round_repeat()

        # when player stands, dealer takes turn and takes add his cards to beet the player
        else:
            while sum_of_card(dealer_cards_in_hand) <= sum_of_card(player_cards_in_hand):
                dealer_cards_in_hand.append(dealer.deal_one())
            if sum_of_card(dealer_cards_in_hand) == sum_of_card(player_cards_in_hand):
                clr()
                print('\nPASS')
                cards_show(player, player_cards_in_hand, dealer_cards_in_hand, len(dealer_cards_in_hand))
                continue
            black_jack_game = win_lose_pass_after_stand(player, dealer_cards_in_hand, player_cards_in_hand, coin_value)

        if not black_jack_game:
            black_jack_game = game_repeat()

    print(f"Thant you for playing this game, u can now withdraw {player.bank_acc}$ money ")
