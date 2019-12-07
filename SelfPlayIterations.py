# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 21:47:03 2019

@author: strotman.7
"""


from SelfPlay import SelfPlay
from TestGameNN import TestGameNN, PolicyNN
from TestBoard import TestBoard
import numpy as np

policyNN = PolicyNN()
nn = TestGameNN(policyNN)
board = TestBoard(np.array([0,0,0,0]), nn)

for x in range(10):
    print(board)
    sp = SelfPlay(nn, board)
    train_examples = sp.PlayGames()
    nn.Train(train_examples)