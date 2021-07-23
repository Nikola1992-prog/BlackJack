def player_input():
    while True:
        try:
            player_name, money_to_bet = input('Please enter your name, and much money you want to bet'
                                              ' with space between( Name amount_of_money ) = ').split(' ')
            if not isinstance(int(money_to_bet), int):
                raise TypeError('Dont use only numbers for name,and string inside money')
            if player_name[0].isnumeric():
                raise TypeError('Dont use  non_string values before your name,'
                                ' u need to Enter name (John) or (john123)')
            if int(money_to_bet) < 10:
                print('Please more money, not less than 10 $')
                continue
            return player_name, int(money_to_bet)
        except (TypeError, ValueError) as e:
            print(e, '\n')


def money_or_no_money(player, coin_to_play):
    while True:
        try:
            more_money = input("You dont have money in ur acc, if you want to play more type Yes to add"
                               " money or Exit for exiting the game = ")
            if more_money.isnumeric():
                raise TypeError('Write string values not numbers')
            if more_money.lower() not in ['y', 'e', 'yes', 'exit']:
                print('You must enter Yes or just Y, and Exit or just E')
                continue
            if more_money[0].lower() == 'y':
                while more_money.lower() == 'y':
                    try:
                        money_to_acc_add = int(input("how much money you want to add ( 0 for exit ) = "))
                        if money_to_acc_add == 0:
                            return False
                        if money_to_acc_add < coin_to_play:
                            print(f"u need to add more than {coin_to_play}!")
                            continue
                        else:
                            player.add_money_to_acc(money_to_acc_add)
                            return True
                    except (TypeError, ValueError):
                        print("Must use Number values of just 0 for EXIT")
            return False
        except TypeError:
            print("Must use Number values and amount larger than coin to bet value")


def coin_add(player):
    while True:
        try:
            coins = int(input(f'{player.name} has {player.bank_acc}$ on acc. Please enter your bet for this round '
                              f'( 10, 20, 30 50 ) = '))
            if coins not in range(10, 50):
                print("You can only bet form 10 to 50 $ at one hand")
                continue
            return coins
        except (TypeError, ValueError) as e:
            print(e, '\n')


def round_repeat():
    while True:
        try:
            round_answer = input("if you want to hit for another card press (Hit) or (Stand) for stand = ")
            if round_answer.isnumeric():
                raise TypeError('Write string values not numbers')
            if round_answer.lower() not in ['h', 's', 'hit', 'stand']:
                print('You must enter Hit or just H, and Stand or just S')
                continue
            if round_answer[0].lower() == 's':
                return False
            return True
        except TypeError as t:
            print(t, '\n')


def game_repeat():
    while True:
        try:
            game_answer = input("if you want to play for another round (Yes) or (Exit) for exiting the game = ")
            if game_answer.isnumeric():
                raise TypeError('Write string values not numbers')
            if game_answer.lower() not in ['y', 'e', 'yes', 'exit']:
                print('You must enter Yes or just Y, and Exit or just E')
                continue
            if game_answer[0].lower() == 'y':
                return True
            return False
        except TypeError as t:
            print(t, '\n')
