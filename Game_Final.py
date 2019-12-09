# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:43:46 2019

@author: strotman.7
"""

from MCTS import MCTS
from DummyGameNN import PolicyNN, DummyGameNN, MoveNN
from AIPlayer import AIPlayer
from DummyGame import DummyGame
from HumanPlayer import HumanPlayer

class Game_Final:
    
    
    def __init__(self, player1, player2, game):
        self.player1 = player1
        self.player2 = player2
        self.gameState = game.GetStartingBoard()
        
    '''
    returns 1 if player1 won
    returns 0 if player 2 won
    returns .5 for tie
    '''
    def PlayGame(self):
        while not self.gameState.IsTerminal():
            self.gameState, _ = self.player1.MakeMove(self.gameState)
            if self.gameState.IsTerminal():
                #from player 2s view
                return 1 - self.gameState.ValueOfWinner()
            self.gameState, _ = self.player2.MakeMove(self.gameState)
           
        #from player1s view
        result = self.gameState.ValueOfWinner()
        return result
'''
player1 = AIPlayer(DummyGameNN(PolicyNN(),MoveNN()),MCTS(), 1)
player2 = HumanPlayer()
game = Game_Final(player1, player2,DummyGame() )
game.PlayGame()
'''