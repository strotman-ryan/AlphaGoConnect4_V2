# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:17:58 2019

@author: strotman.7
"""
from RealGame import RealGame
from AIPlayerFactory import AIPlayerFactory


class Evaluator:
    
    def __init__(self, neuralNetwork1, neuralNetwork2, gameType):
        self.neuralNetwork1 = neuralNetwork1
        self.neuralNetwork2 = neuralNetwork2
        self.gameType = gameType
        self.aiFactory = AIPlayerFactory()
        
    '''
    true if nn2 is statistically better
    '''
    def IsNN2BetterThanNN1(self,gamesToPlay):
        nn1WinCount = 0
        nn2WinCount = 0
        for num in range(gamesToPlay):
            if num % 2 ==0:
                player1 = self.aiFactory.GetEvaluatorAI(self.neuralNetwork1)
                player2 = self.aiFactory.GetEvaluatorAI(self.neuralNetwork2)
            else:
                player1 = self.aiFactory.GetEvaluatorAI(self.neuralNetwork2)
                player2 = self.aiFactory.GetEvaluatorAI(self.neuralNetwork1)
                
            game = RealGame(player1, player2, self.gameType)
            
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

