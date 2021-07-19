# import os
# def clear(): os.system('cls') #on Windows System

from random import shuffle

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.card_value = values[rank]


class Table:

    def __init__(self):
        self.table_cards = []

    def add_and_shuffle(self):

        for suit in suits:
            for rank in ranks:
                self.table_cards.append(Card(suit, rank))

        shuffle(self.table_cards)


class Dealer(Table):

    def deal_one(self):
        return self.table_cards.pop()

    def dealer_move(self):
        pass


class Player:

    def __init__(self, name, bank_acc):
        self.name = name
        self.bank_acc = bank_acc

    def add_money_to_acc(self, money_to_add):
        print(f'{self.name} bank_acc + {money_to_add} = {self.bank_acc + money_to_add} $')
        self.bank_acc += money

    def win_round_money(self, bet_deal, percent=0.0):
        print(f'{self.name} bank_acc = {self.bank_acc} $ +  {bet_deal} $ = {self.bank_acc + bet_deal} $')
        self.bank_acc += (bet_deal + (bet_deal * percent))

    def lose_round_money(self, bet_deal):
        print(f'{self.name} bank_acc = {self.bank_acc} $ -  {bet_deal} $ = {self.bank_acc - bet_deal} $')
        self.bank_acc -= bet_deal


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


def round_repeat():
    return int(input("if you want to hit for another card press (1) or (0) for stand = "))


def game_repeat():
    return int(input("if you want to play for another round (1) or (0) for stand = "))


# win bust blackjack pass
def win_lose_pass(dealer_cards, player_cards, coin_price, before_stand=True):
    if before_stand:
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

    else:
        if sum_of_card(dealer_cards) > 21 and sum_of_card(player_cards) <= 21:
            clr()
            print("\nPlayer win, dealer bust")
            cards_show(player_cards, dealer_cards, len(dealer_cards))
            player.win_round_money(coin_price)
            return False
        elif sum_of_card(dealer_cards) > sum_of_card(player_cards):
            clr()
            print("\nDealer win!")
            player.lose_round_money(coin_value)
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


def clr(lines=10):
    print('\n' * lines)


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

        cards_show(player_cards_in_hand, dealer_cards_in_hand)
        black_jack_game = win_lose_pass(dealer_cards_in_hand, player_cards_in_hand, coin_value, True)

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
            cards_show(player_cards_in_hand, dealer_cards_in_hand)
            black_jack_game = win_lose_pass(dealer_cards_in_hand, player_cards_in_hand, coin_value, True)

            if black_jack_game == False:
                break

            hit_stand = round_repeat()

        if black_jack_game and hit_stand == 0:

            if sum_of_card(dealer_cards_in_hand) > sum_of_card(player_cards_in_hand):
                clr()
                print("\nDealer win!")
                cards_show(player_cards_in_hand, dealer_cards_in_hand, len(dealer_cards_in_hand))
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
                cards_show(player_cards_in_hand, dealer_cards_in_hand, len(dealer_cards_in_hand))
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
