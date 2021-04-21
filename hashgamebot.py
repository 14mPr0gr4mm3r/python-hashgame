"""
Python Hash Game Bot Test
@author: Gustavo-Sampaio (14mPr0gr4mm3r)
@description: a bot to play Python Hash Game (created by me too)
"""
#import math
import random
from time import sleep


class Bot():
    def __init__(self, hshgrid, uservalue, botvalue):
        self.hashgrid = hshgrid
        self.uservalue = uservalue
        self.myvalue = botvalue
    def updateGrid(self, grid):
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
        for t in tests:
            if self.hashgrid[t[0]] == self.uservalue and self.hashgrid[t[1]] == self.uservalue and self.hashgrid[t[2]] == ' ':
                choice = t[2]
            elif self.hashgrid[t[0]] == self.uservalue and self.hashgrid[t[1]] == ' ' and self.hashgrid[t[2]] == self.uservalue:
                choice = t[1]
            elif self.hashgrid[t[0]] == ' ' and self.hashgrid[t[1]] == self.uservalue and self.hashgrid[t[2]] == self.uservalue:
                choice = t[0]
        for t in tests:
            if self.hashgrid[t[0]] == self.myvalue and self.hashgrid[t[1]] == self.myvalue and self.hashgrid[t[2]] == ' ':
                choice = t[2]
            elif self.hashgrid[t[0]] == self.myvalue and self.hashgrid[t[1]] == ' ' and self.hashgrid[t[2]] == self.myvalue:
                choice = t[1]
            elif self.hashgrid[t[0]] == ' ' and self.hashgrid[t[1]] == self.myvalue and self.hashgrid[t[2]] == self.myvalue:
                choice = t[0]
        while self.hashgrid[choice] != ' ':
            choice = random.randint(1, 9)
        return choice
        
