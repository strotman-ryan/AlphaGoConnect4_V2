# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:10:17 2019

@author: strotman.7
"""

import numpy as np
from TrainingExample import TrainingExample


class TrainingGame:
    
    
    def __init__(self, aiPlayer, gameType):
        self.ai = aiPlayer
        self.gameState = gameType.GetStartingBoard()
        self.trainingData = []
        
    def PlayGame(self):
        while not self.gameState.IsTerminal():
            #print(self.gameState.board)
            previousGameState = self.gameState
            self.gameState, pi = self.ai.MakeMove(self.gameState)
            self.trainingData.append(TrainingExample(previousGameState, pi))
        
        result = self.gameState.ValueOfWinner()
        for state in reversed(self.trainingData):
            result = 1 - result
            state.AddResult(result)
        
    def GetTraingData(self):
        return self.trainingData