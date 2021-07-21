# @TODO  Constants should me uppercase
from Players import Player, Dealer
from utils.dealer import game_repeat, round_repeat, clr, sum_of_card


def cards_show(player_show, dealer_show, dealer_to_show=-1):
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


def win_lose_pass_before_stand(dealer_cards, player_cards, coin_price):
    if sum_of_card(player_cards) == 21:
        clr()
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        print(f"\nBlackJACK, {player.name} wins!")
        player.win_round_money(coin_price, 0.5)
        return False
    elif sum_of_card(player_cards) > 21:
        clr()
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        print("\nBUST, DEALER WINS")
        player.lose_round_money(coin_price)
        return False
    else:
        return True


def win_lose_pass_after_stand(dealer_cards, player_cards, coin_price):
    if sum_of_card(dealer_cards) > 21:
        clr()
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        print(f"\n{player.name} wins, dealer bust!")
        player.win_round_money(coin_price)
        return False
    elif sum_of_card(dealer_cards) > sum_of_card(player_cards):
        clr()
        cards_show(player_cards, dealer_cards, len(dealer_cards))
        print("\nDealer Win")
        player.lose_round_money(coin_price)
        return False
    else:
        return True


if __name__ == "__main__":

    # player, money = input('Please enter your name and money (name,money) = ').split(',')
    # player = Player(player, int(money))
    player = Player('player', 100)
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

        # BlackJack, player win! - if dealer gives 21 in splitting cards
        cards_show(player_cards_in_hand, dealer_cards_in_hand)
        black_jack_game = win_lose_pass_before_stand(dealer_cards_in_hand, player_cards_in_hand, coin_value)
        hit_stand = round_repeat()

        # if player want another cards to add to his hand
        while hit_stand and black_jack_game:
            player_cards_in_hand.append(dealer.deal_one())
            clr()
            cards_show(player_cards_in_hand, dealer_cards_in_hand)
            black_jack_game = win_lose_pass_before_stand(dealer_cards_in_hand, player_cards_in_hand, coin_value)

            if not black_jack_game:
                break
            hit_stand = round_repeat()

        # when player stands, dealer takes turn and takes add his cards to beet the player
        else:
            while sum_of_card(dealer_cards_in_hand) <= sum_of_card(player_cards_in_hand):
                dealer_cards_in_hand.append(dealer.deal_one())

            black_jack_game = win_lose_pass_after_stand(dealer_cards_in_hand, player_cards_in_hand, coin_value)

            if sum_of_card(dealer_cards_in_hand) == sum_of_card(player_cards_in_hand):
                clr()
                print('\nPASS')
                cards_show(player_cards_in_hand, dealer_cards_in_hand, len(dealer_cards_in_hand))
                continue

        if not black_jack_game:
            black_jack_game = game_repeat()
