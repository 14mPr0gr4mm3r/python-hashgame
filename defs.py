from typing import Literal

GRID_ROW = '\n{:^3}|{:^3}|{:^3}'
GRID = (GRID_ROW
        + '\n___|___|___'
        + GRID_ROW
        + '\n___|___|___'
        + GRID_ROW
        + '\n   |   |   \n')

DEFAULT_VALUE = ' '
PLAYER1_VALUE = 'O'
PLAYER2_VALUE = 'X'
Sign = Literal['O', 'X']
