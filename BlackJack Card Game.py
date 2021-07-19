# @TODO  Constants should me uppercase
from Players import Player, Dealer
from utils.dealer import cards_show, game_repeat, win_lose_pass, round_repeat, clr, sum_of_card


if __name__ == "__main__":

    player, money = input('Please enter your name and money (name,money) = ').split(',')

    player = Player(player, int(money))
    # player = Player('player', 100)
    dealer = Dealer()
    black_jack_game = True

    while black_jack_game:

        dealer.add_and_shuffle()
        player_cards_in_hand = []
        dealer_cards_in_hand = []

        coin_value = int(input(f'{player.name} has {player.bank_acc}$ on acc. Please enter your bet for this round '
                               f'( 10, 20, 30 50 ) = '))

        if player.bank_acc < coin_value:
            game_on = int(input("u dont have money in ur acc, if u want to play more add money yes = 1, no = 0"))
            while game_on:
                money_to_acc_add = int(input("how much money you want to add = "))
                if money_to_acc_add < coin_value:
                    print(f"u need to add more than {coin_value}!")
                    continue
                else:
                    player.add_money_to_acc(money_to_acc_add)
                    break

            else:
                print("Tnx for playing the game!")
                black_jack_game = False
                break

        # dealer split cards
        for _ in range(2):
            player_cards_in_hand.append(dealer.deal_one())
            dealer_cards_in_hand.append(dealer.deal_one())

        cards_show(player, player_cards_in_hand, dealer_cards_in_hand)
        black_jack_game = win_lose_pass(player, dealer_cards_in_hand, player_cards_in_hand, coin_value, True)

        if not black_jack_game:
            black_jack_game = game_repeat()
            if black_jack_game:
                continue
            else:
                break

        hit_stand = round_repeat()

        while hit_stand != 0:
            player_cards_in_hand.append(dealer.deal_one())
            clr()
            cards_show(player, player_cards_in_hand, dealer_cards_in_hand)
            black_jack_game = win_lose_pass(player, dealer_cards_in_hand, player_cards_in_hand, coin_value, True)

            if black_jack_game == False:
                break

            hit_stand = round_repeat()

        if black_jack_game and hit_stand == 0:

            if sum_of_card(dealer_cards_in_hand) > sum_of_card(player_cards_in_hand):
                clr()
                print("\nDealer win!")
                cards_show(player, player_cards_in_hand, dealer_cards_in_hand, len(dealer_cards_in_hand))
                player.lose_round_money(coin_value)
                black_jack_game = game_repeat()
                if black_jack_game:
                    continue
                else:
                    break

            while sum_of_card(dealer_cards_in_hand) <= 21:
                dealer_cards_in_hand.append(dealer.deal_one())
                # logika da ne ide dalje! da ne prelazi 21

            if sum_of_card(dealer_cards_in_hand) > 21:
                clr()
                print("\nDealer bust")
                cards_show(player, player_cards_in_hand, dealer_cards_in_hand, len(dealer_cards_in_hand))
                player.win_round_money(coin_value)
                black_jack_game = game_repeat()
                if black_jack_game:
                    continue
                else:
                    break
        else:
            black_jack_game = game_repeat()
            if black_jack_game:
                continue
            else:
                break
