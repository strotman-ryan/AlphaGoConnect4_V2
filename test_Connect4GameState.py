# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:59:13 2019

@author: strotman.7
"""

#testing Connect4GameState.py

from HumanPlayer import HumanPlayer
from Connect4GameType import Connect4GameType
from RealGame import RealGame

game = RealGame(HumanPlayer(), HumanPlayer(),Connect4GameType())
game.PlayGame()