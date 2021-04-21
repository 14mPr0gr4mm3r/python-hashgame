"""
Python HashGame - Test
@author: Gustavo-Sampaio (14mPr0gr4mm3r)
@description: the classic hash game developed with Python
"""

from time import sleep
import sys
import hashgamebot as gbot

GRID = '\n {} | {} | {}\n___|___|___\n {} | {} | {}\n___|___|___\n {} | {} | {}\n   |   |\n'
DEFAULT_VALUE = ' '
PLAYER1_VALUE = 'O'
PLAYER2_VALUE = 'X'

game = False

hashgrid = {1: DEFAULT_VALUE, 2: DEFAULT_VALUE, 3: DEFAULT_VALUE,
            4: DEFAULT_VALUE, 5: DEFAULT_VALUE, 6: DEFAULT_VALUE,
            7: DEFAULT_VALUE, 8: DEFAULT_VALUE, 9: DEFAULT_VALUE}


def show_hashgrid():
    global GRID
    print(
        GRID.format(
            hashgrid[1], hashgrid[2], hashgrid[3],
            hashgrid[4], hashgrid[5], hashgrid[6],
            hashgrid[7], hashgrid[8], hashgrid[9]
        )
          )


def verify_results():
    global hashgrid, game
    tests = [
        (1, 2, 3),
        (1, 5, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 5, 7),
        (3, 6, 9),
        (4, 5, 6),
        (7, 8, 9)
        ]
    for t in tests:
        if hashgrid[t[0]] == PLAYER1_VALUE and hashgrid[t[1]] == PLAYER1_VALUE and hashgrid[t[2]] == PLAYER1_VALUE:
            show_hashgrid()
            print('Player 1 is the winner!')
            game = False
        elif hashgrid[t[0]] == PLAYER2_VALUE and hashgrid[t[1]] == PLAYER2_VALUE and hashgrid[t[2]] == PLAYER2_VALUE:
            show_hashgrid()
            print('Player 2 is the winner!')
            game = False
    if game == True:
        try:
            i = list(hashgrid.values()).index(DEFAULT_VALUE)
        except ValueError:
            show_hashgrid()
            print('Match ended in a tie!')
            sys.exit()

def start_game_player():
    global game
    game = True
    time = 1
    while game == True:
        show_hashgrid()
        if time == 1:
            player = int(str(input(f'PLAYER{time} - Enter a position: ')))
            if hashgrid[player] == DEFAULT_VALUE:
                hashgrid[player] = PLAYER1_VALUE
                verify_results()
            else:
                print('This space has already been filled')
                sleep(2)
            time = 2
        elif time == 2:
            player = int(str(input(f'PLAYER{time} - Enter a position: ')))
            if hashgrid[player] == DEFAULT_VALUE:
                hashgrid[player] = PLAYER2_VALUE
                verify_results()
            else:
                print('This space has already been filled')
                sleep(2)
            time = 1


def start_game_bot():
    global game
    cpu = gbot.Bot(hashgrid, PLAYER1_VALUE, PLAYER2_VALUE)
    game = True
    time = 1
    while game == True:
        show_hashgrid()
        if time == 1:
            player = int(str(input(f'PLAYER{time} - Enter a position: ')))
            if hashgrid[player] == DEFAULT_VALUE:
                hashgrid[player] = PLAYER1_VALUE
                cpu.updateGrid(hashgrid)
                verify_results()
            else:
                print('This space has already been filled')
                sleep(2)
            time = 2
        elif time == 2:
            print('Waiting for CPU decision...')
            #bot choice
            hashgrid[cpu.makeChoice()] = PLAYER2_VALUE
            verify_results()
            time = 1


def authenticate_answer():
    global bot
    if bot == 'Y':
        start_game_bot()
    elif bot == 'N':
        start_game_player()
    else:
        while bot != 'Y' and bot != 'N':
            bot = str(input('Versus CPU?[Y/N] ')).strip().upper()
            authenticate_answer()


bot = str(input('Versus CPU?[Y/N] ')).strip().upper()
authenticate_answer()
    
