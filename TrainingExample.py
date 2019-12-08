# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 21:44:56 2019

@author: strotman.7
"""

class TrainingExample:
    
    def __init__(self, gameState, pi):
        self.gameState = gameState
        self.pi = pi
        
    def AddResult(self,result):
        self.result = result