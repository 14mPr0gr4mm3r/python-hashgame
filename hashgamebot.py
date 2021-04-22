"""
Python Hash Game Bot Test
@author "Gustavo-Sampaio (14mPr0gr4mm3r)"
@description "a bot to play Python Hash Game (created by me too)"
"""
#import math
import random
from time import sleep
from defs import Sign


class Bot():
    hashgrid: dict
    uservalue: Sign
    myvalue: Sign

    def __init__(self, hashgrid, uservalue, botvalue):
        self.hashgrid = hashgrid
        self.uservalue = uservalue
        self.myvalue = botvalue

    def updateGrid(self, grid: dict):
        self.hashgrid = grid

    def makeChoice(self):
        sleep(random.random() * random.randint(1, 3))
        choice = random.randint(1, 9)
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
        for value in [self.uservalue, self.myvalue]:
            for t in tests:
                if self.hashgrid[t[0]] == value and self.hashgrid[t[1]] == value and self.hashgrid[t[2]] == ' ':
                    choice = t[2]
                elif self.hashgrid[t[0]] == value and self.hashgrid[t[1]] == ' ' and self.hashgrid[t[2]] == value:
                    choice = t[1]
                elif self.hashgrid[t[0]] == ' ' and self.hashgrid[t[1]] == value and self.hashgrid[t[2]] == value:
                    choice = t[0]

        while self.hashgrid[choice] != ' ':
            choice = random.randint(1, 9)

        return str(choice)
