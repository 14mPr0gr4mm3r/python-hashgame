"""
Copyright (c) 2021, Gustavo Sampaio

The classic hash game (tic-tac-toe) in a
command-line form, developed with Python
"""

import sys
from time import sleep

from typing import Union, Literal

from defs import GRID
from defs import DEFAULT_VALUE, PLAYER1_VALUE, PLAYER2_VALUE
from defs import Sign

import hashgamebot as gbot


game = False

hashgrid = {position: DEFAULT_VALUE for position in range(1, 10)}


def print_hashgrid():
    print(
        GRID.format(*hashgrid.values())
    )


def is_hashgrid_on_default_state() -> bool:
    return all(field == DEFAULT_VALUE for field in hashgrid.values())


def verify_results():
    global game

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
        if all(hashgrid[t[s]] == PLAYER1_VALUE for s in range(len(t))):
            print_hashgrid()
            print('Player 1 is the winner!')
            game = False
        elif all(hashgrid[t[s]] == PLAYER2_VALUE for s in range(len(t))):
            print_hashgrid()
            print('Player 2 is the winner!')
            game = False

    if game == True:
        try:
            _ = list(hashgrid.values()).index(DEFAULT_VALUE)
        except ValueError:
            print_hashgrid()
            print('Match ended in a tie!')
            sys.exit()


def get_sign_to_place(current_turn: int) -> str:
    return PLAYER1_VALUE if current_turn == 1 else PLAYER2_VALUE


def next_turn(current_turn: int) -> int:
    return 2 if current_turn == 1 else 1


def insert_sign_on_space(hashgrid: dict, space: int, sign: Sign) -> Union[dict, None]:
    if hashgrid[space] != DEFAULT_VALUE:
        print('This space has already been filled')
        return None

    return {**hashgrid, space: sign}


def start_game_with_player():
    global game, hashgrid
    game = True
    turn = 1
    response: Union[str, None] = None

    while game:
        if response or is_hashgrid_on_default_state():
            print_hashgrid()

        response = input(f'Player {turn} - Enter a position: ').strip()

        if response:
            space = int(response)
            sign = get_sign_to_place(turn)

            new_grid = insert_sign_on_space(hashgrid, space, sign)

            if new_grid is not None:
                hashgrid = new_grid
                verify_results()

            turn = next_turn(turn)


def start_game_with_bot():
    global game, hashgrid
    cpu = gbot.Bot(hashgrid, PLAYER1_VALUE, PLAYER2_VALUE)
    BOT_TURN = 2
    game = True
    turn = 1
    response: Union[str, None] = None

    while game:
        if response or is_hashgrid_on_default_state():
            print_hashgrid()

        if turn != BOT_TURN:
            response = input(f'Player {turn} - Enter a position: ').strip()
        else:
            print('Waiting for CPU choice...')
            response = cpu.makeChoice()

        if response:
            space = int(response)
            sign = get_sign_to_place(turn)

            new_grid = insert_sign_on_space(hashgrid, space, sign)

            if new_grid is not None:
                hashgrid = new_grid
                cpu.updateGrid(hashgrid)
                verify_results()

                turn = next_turn(turn)


def main():
    while (use_bot := input('Versus CPU? [y/N]').strip().lower()[:1]) not in ['', 'y', 'n']:
        pass

    start_game = start_game_with_bot if use_bot == 'y' else start_game_with_player

    start_game()


if __name__ == '__main__':
    main()
