# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:59:13 2019

@author: strotman.7
"""

#testing Connect4GameState.py

from HumanPlayer import HumanPlayer
from Connect4GameType import Connect4GameType
from RealGame import RealGame
from Connect4GameState import Connect4GameState
import numpy as np


class nn_test:
    
    def __init__(self):
        pass
    
    def GetProbabilities(self, board):
        return np.array([.1,.1,.1,.1,.1,.1,.4])
    
    def ProbabilityOfWinning(self, board):
        return .5

'''
game = RealGame(HumanPlayer(), HumanPlayer(),Connect4GameType())
print(game.PlayGame())
'''

state = Connect4GameState(np.zeros((6,7)))
states, probs = state.GetNextStatesWithProbabilites(nn_test())
print(states)
for s in states:
    print(s.board)


