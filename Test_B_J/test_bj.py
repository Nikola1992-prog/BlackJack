import unittest
from BlackJack import Card
from Players import Player
from utils.dealer import sum_of_card, win_lose_pass_before_stand, win_lose_pass_after_stand


class TestDealer(unittest.TestCase):
    player = Player('Player_test', 100)
    coin_value = 20

    player_cards_hand = [[Card('Spades', 'Queen'), Card('Hearts', 'Ace')],
                         [Card('Hearts', 'Three'), Card('Clubs', 'Ace')],
                         [Card('Hearts', 'King'), Card('Clubs', 'King')],
                         [Card('Hearts', 'Ace'), Card('Clubs', 'Ace')],
                         [Card('Hearts', 'King'), Card('Hearts', 'Queen'), Card('Spades', 'Queen')],
                         [Card('Hearts', 'Three'), Card('Clubs', 'Three')]]

    dealer_cards_hand = [[Card('Spades', 'Queen'), Card('Hearts', 'Ace')],  # True PASS 21==21
                         [Card('Hearts', 'King'), Card('Clubs', 'Ace')],  # False 14 < 21 dealer win
                         [Card('Hearts', 'King'), Card('Clubs', 'Three')],  # False 20 > 13 dealer lose
                         [Card('Hearts', 'King'), Card('Clubs', 'Five')],  # False dealer win
                         [Card('Hearts', 'King'), Card('Hearts', 'Three')],  # False, Dealer win
                         [Card('Hearts', 'Jack'), Card('Hearts', 'Queen'),
                          Card('Spades', 'Queen')]]  # False dealer lose

    # Cards for tasting sum of all cards
    all_cases = player_cards_hand + dealer_cards_hand

    def test_sum_of_cards_in_hand(self):
        result_all_cases = [21, 14, 20, 13, 30, 6, 21, 21, 13, 15, 13, 30]

        for index, player_cards in enumerate(self.all_cases):
            result = sum_of_card(player_cards)
            self.assertEqual(result, result_all_cases[index])

    def test_win_lose_before_stand(self):
        result_win_lose_before_stand = [False, True, True, True, False, True]  # BJ, <21, <21, <21, >21, <21
        for index, (player_hand, dealer_hand) in enumerate(zip(self.player_cards_hand, self.dealer_cards_hand)):
            print(index)
            result = win_lose_pass_before_stand(self.player, dealer_hand, player_hand, self.coin_value)
            self.assertEqual(result, result_win_lose_before_stand[index])

    def test_win_lose_pass_after_stand(self):
        result_win_lose_after_stand = [True, False, True, False, True, False]
        for index, (player_hand, dealer_hand) in enumerate(zip(self.player_cards_hand, self.dealer_cards_hand)):
            print(index)
            result = win_lose_pass_after_stand(self.player, dealer_hand, player_hand, self.coin_value)
            self.assertEqual(result, result_win_lose_after_stand[index])


if __name__ == "__main__":
    unittest.main()
