# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:44:55 2019

@author: strotman.7
"""

from MCTS import MCTS
from AIPlayer import AIPlayer

class AIPlayerFactory:
    
    
    def __init__(self):
        pass
    
    
    def GetSelfPlayAI(self,neuralNetworks):
        return AIPlayer(neuralNetworks, MCTS(), 1, 100)
    
    def GetEvaluatorAI(self,neuralNetworks):
        return AIPlayer(neuralNetworks, MCTS(), .1, 100)
    
    def GetPlayHumanAI(self,neuralNetworks):
        return AIPlayer(neuralNetworks, MCTS(), .1, 1000)