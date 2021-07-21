from BlackJack import Table


class Dealer(Table):

    def __init__(self):
        super().__init__()  # This is how u call the init method of super-class

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
        self.bank_acc += money_to_add

    def win_round_money(self, bet_deal, percent=0.0):
        print(f'{self.name} bank_acc = {self.bank_acc} $ +  {bet_deal} $ = {self.bank_acc + bet_deal} $')
        self.bank_acc += (bet_deal + (bet_deal * percent))

    def lose_round_money(self, bet_deal):
        print(f'{self.name} bank_acc = {self.bank_acc} $ -  {bet_deal} $ = {self.bank_acc - bet_deal} $')
        self.bank_acc -= bet_deal

