import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras import losses

from AbstractNeuralNetwork import AbstractNeuralNetwork

class Connect4NN(AbstractNeuralNetwork):

    def __init__(self):
        self.winNN = Connect4WinNN()
        self.movesNN = Connect4MoveNN()

    def GetMoveProbabilites(self, gameState):
        board_rep = gameState.board.copy()
        transformedRep = self.transformBoard(board_rep)
        return self.movesNN.Predict(np.array([transformedRep]))

    def GetProbabilityOfWinning(self, gameState):
        board_rep = gameState.board.copy()
        transformedRep = self.transformBoard(board_rep)
        return self.winNN.Predict(np.array([transformedRep]))

    def Train(self, trainingExamples):
        results = []
        pis = []
        boards = []
        for example in trainingExamples:
            results.append(example.result)
            pis.append(example.pi)
            board_rep = example.gameState.board
            boards.append(self.transformBoard(board_rep))
        pis = np.array(pis) 
        boards = np.array(boards)
        self.winNN.Train(boards, results)
        self.movesNN.Train(boards, pis)

    def Save(self, fileName):
        self.winNN.Save(fileName + "_policy")
        self.movesNN.Save(fileName + "_moves")

    def Load(self, fileName):
        self.winNN.Load(fileName + "_policy")
        self.movesNN.Load(fileName + "_moves")
        
    def transformBoard(self, board_rep):
        board_rep1 = np.reshape(board_rep.copy(), 42)
        board_rep2 = np.reshape(board_rep.copy(), 42)
        board_rep1[board_rep1 != 1] = 0
        board_rep2[board_rep2 != -1] = 0
        return np.append(board_rep1, board_rep2)
        
        
class Connect4WinNN:

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(units = 100, activation = 'relu', input_dim = 84))
        self.model.add(Dense(units = 20, activation = 'relu'))
        self.model.add(Dense(units = 1, activation = 'sigmoid'))
        self.model.compile(loss = 'mean_squared_error', optimizer = 'sgd', metrics = ['accuracy'])
    def Predict(self, board_rep):
        return self.model.predict(board_rep)[0][0]
        
    def Train(self, board_reps, outcomes):
        self.model.fit(board_reps, outcomes, epochs = 10, batch_size = 50)
        
    def Save(self, fileName):
        fileName = fileName + '.h5'
        self.model.save(fileName)
    def Load(self, fileName):
        fileName = fileName + '.h5'
        self.model = load_model(fileName)
        
class Connect4MoveNN:

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(units = 100, activation = 'relu', input_dim = 84))
        #self.model.add(Dense(units = 70,activation = 'relu'))  #added this line
        self.model.add(Dense(units = 20,activation = 'relu'))  
        self.model.add(Dense(units = 7, activation = 'softmax'))  
        self.model.compile(loss = 'categorical_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])
    def Predict(self, board_rep):
        return self.model.predict(board_rep)[0]
        
    def Train(self, board_reps, pis):
        self.model.fit(board_reps, pis, epochs = 10, batch_size = 50)
        
    def Save(self, fileName):
        fileName = fileName + '.h5'
        self.model.save(fileName)

    def Load(self, fileName):
        fileName = fileName + '.h5'
        self.model = load_model(fileName)
        





        