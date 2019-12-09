# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:10:17 2019

@author: strotman.7
"""

import numpy as np
from TrainingExample import TrainingExample


class TrainingGame:
    
    
    def __init__(self, aiPlayer, game):
        self.ai = aiPlayer
        self.gameState = game.GetStartingBoard()
        self.trainingData = np.array([])
        
    def PlayGame(self):
        while not self.gameState.IsTerminal():
            previousGameState = self.gameState
            self.gameState, pi = self.ai.MakeMove(self.gameState)
            self.trainingData = np.append(self.trainingData, TrainingExample(previousGameState, pi))
        
        result = self.gameState.ValueOfWinner()
        for state in np.flip(self.trainingData):
            result = 1 - result
            state.AddResult(result)
        
    def GetTraingData(self):
        return self.trainingData