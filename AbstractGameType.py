# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:12:38 2019

@author: strotman.7
"""
from abc import ABC, abstractmethod

class AbstractGameType(ABC):
    
    @abstractmethod
    def GetStartingBoard(self):
        pass
    
    def GetNewNeuralNetwork(self):
        pass
