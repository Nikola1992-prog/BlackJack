from utils.constants import RANKS, SUITS, VALUES
from random import shuffle


class Card:

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.card_value = VALUES[rank]


class Table:

    def __init__(self):
        self.table_cards = []

    def add_and_shuffle(self):
        for suit in SUITS:
            for rank in RANKS:
                self.table_cards.append(Card(suit, rank))

        shuffle(self.table_cards)