# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:43:46 2019

@author: strotman.7
"""
from HumanPlayer import HumanPlayer
from Connect4NN import Connect4NN
from AIPlayerFactory import AIPlayerFactory
from Connect4GameType import Connect4GameType

class RealGame:
    
    
    def __init__(self, player1, player2, gameType):
        self.player1 = player1
        self.player2 = player2
        self.gameState = gameType.GetStartingBoard()
        
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
player1 = HumanPlayer()
nn = Connect4NN()
nn.Load("NN")
player2 = AIPlayerFactory().GetPlayHumanAI(nn)
game = RealGame(player1, player2, Connect4GameType())
game.PlayGame()
'''
