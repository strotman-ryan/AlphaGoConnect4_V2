# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:12:27 2019

@author: strotman.7
"""
from DummyGameState import DummyGameState
import numpy as np
from AbstractGameType import AbstractGameType

class DummyGameType(AbstractGameType):
    
    def __init__(self):
        pass
    
    def GetStartingBoard(self):
        return DummyGameState(np.array([0,0,0,0]))