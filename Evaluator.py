# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:17:58 2019

@author: strotman.7
"""
from Game_Final import Game_Final
from AIPlayer import AIPlayer
from MCTS import MCTS
from DummyGameNN import PolicyNN, DummyGameNN, MoveNN
from DummyGame import DummyGame


class Evaluator:
    
    def __init__(self, neuralNetwork1, neuralNetwork2, game):
        self.neuralNetwork1 = neuralNetwork1
        self.neuralNetwork2 = neuralNetwork2
        self.game = game
        
    '''
    true if nn2 is statistically better
    '''
    def IsNN2BetterThanNN1(self,gamesToPlay):
        nn1WinCount = 0
        nn2WinCount = 0
        for num in range(gamesToPlay):
            if num % 2 ==0:
                player1 = AIPlayer(self.neuralNetwork1, MCTS(), 1)
                player2 = AIPlayer(self.neuralNetwork2, MCTS(), 1)
            else:
                player1 = AIPlayer(self.neuralNetwork2, MCTS(), 1)
                player2 = AIPlayer(self.neuralNetwork1, MCTS(), 1)
                
            game = Game_Final(player1, player2, self.game)
            
            winner = game.PlayGame()
            
            if num % 2 == 0 and winner == 1:
                nn1WinCount += 1
            if num % 2 == 0 and winner == 0:
                nn2WinCount += 1
            if num % 2 != 0 and winner ==1:
                nn2WinCount += 1
            if num % 2 != 0 and winner == 0:
                nn1WinCount += 1
        return nn2WinCount > nn1WinCount
'''
evaluator = Evaluator(DummyGameNN(),DummyGameNN(),DummyGame() )
x = evaluator.IsNN2BetterThanNN1(100)
'''         

