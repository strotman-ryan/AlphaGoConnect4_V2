# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:00:46 2019

@author: strotman.7
"""
from abc import ABC, abstractmethod 

class AbstractNeuralNetwork(ABC):
    
    @abstractmethod
    def GetMoveProbabilites(self, gameState):
        pass
    
    @abstractmethod
    def GetProbabilityOfWinning(self, gameState):
        pass
    
    @abstractmethod
    def Train(self, trainingExamples):
        pass
    
    @abstractmethod
    def Save(self, fileName):
        pass
    
    @abstractmethod
    def Load(self, fileName):
        pass