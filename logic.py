import random, os

field = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

turns_dict = {'1a': 0, '2a': 1, '3a': 2,
              '1b': 3, '2b': 4, '3b': 5,
              '1c': 6, '2c': 7, '3c': 8}

bot_mark, player_mark = '', ''
run = True

def ascii_field():
    print(f'  1   2   3\na {field[0]} | {field[1]} | {field[2]} \n ---+---+--- \nb {field[3]} | {field[4]} | {field[5]} \n ---+---+--- \nc {field[6]} | {field[7]} | {field[8]}')


def clear():
    os.system(['clear','cls'][os.name == 'nt'])


def start():
    while True:
        print('Start new game? (y/n)')
        command = input()
        match command:
            case 'y':

                while True:
                    print('Your mark is O or X? (o/x)')
                    command = input()
                    match command:
                        case 'x':
                            game(mark='X')
                            break
                        case 'o':
                            game(mark='O')
                            break
                        case _:
                            continue

            case 'n':
                exit()
            case _:
                continue


def game(mark):
    global field, bot_mark, player_mark, turns_dict, run
    field = [' ',' ',' ',
             ' ',' ',' ',
            ' ',' ',' ']
    run = True
    clear()
    player_mark = mark
    if mark == 'O':
        bot_mark = 'X'
    else:
        bot_mark = 'O'

    while run:
        ascii_field()
        print("Your's turn! (example: 1a)")
        player_turn()
        clear()
        ascii_field()

        checking = check_field()
        if checking == 's':
            run = False
            break    

        bot_turn()
        ascii_field()
        checking = check_field()
        clear()


def player_turn():
    global field, player_mark, turns_dict, ascii_field
    while True:
        turn = input()
        print(f"Your's turn is {turn}")
        if turn in turns_dict.keys():
            turn = turns_dict.get(turn)
            if field[turn] == " ":
                field[turn] = player_mark
                break
    clear()
    ascii_field()
    input()


def bot_turn(mode='easy'):
    input('Bot turn..')
    global field, bot_mark, turns_dict
    match mode:
        case 'easy':
            '''Easy mode'''
            while True:
                turn = random.randint(0, 8)
                if field[turn] == " ":
                    field[turn] = bot_mark
                    break

        case 'normal':
            pass
        case 'hard':
            pass
    clear()
    

def end(win):
    global field, run
    clear()
    run = False
    if win == 'player':
        ascii_field()
        print('You are the Winner!')
        input()
    elif win == 'bot':
        ascii_field()
        print('You lose...')
        input()
    else:
        ascii_field
        print('Nobody won...')
        input()
    clear()


def check_field():
    global field, player_mark, bot_mark

    ## check horizontals
    for i in range(0, 8, 3):
        if field[0+i] == field[1+i] == field[2+i] != ' ':
            if player_mark == field[0+i]:
                end('player')
                return 's'
            elif bot_mark == field[0+i]:
                end('bot')
                return 's'

    ## check verticals
    for i in range(1, 3):
        if field[0+i] == field[3+i] == field[6+i] != ' ':
            if player_mark == field[0+i]:
                end('player')
                return 's'
            elif bot_mark == field[0+i]:
                end('bot')
                return 's'

    ## check diagonals
    if field[0] == field[4] == field[8] != ' ':
        if player_mark == field[0]:
            end('player')
            return 's'
        elif bot_mark == field[0]:
            end('bot')
            return 's'

    if field[2] == field[4] == field[6] != ' ':
        if player_mark == field[2]:
            end('player')
            return 's'
        elif bot_mark == field[2]:
            end('bot')
            return 's'

    ## check fields for free mark
    if not ' ' in field:
        end('nobody')
        return 's'
            
