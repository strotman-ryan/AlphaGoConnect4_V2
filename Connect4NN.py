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
		return self.movesNN.Predict(transformedRep)
	
	def GetProbabilityOfWinning(self, gameState):
		board_rep = gameState.board.copy()
		transformedRep = self.transformBoard(board_rep)
		return self.movesNN.Predict(transformedRep)
	
	def Train(self, trainingExamples):
		results = np.array([])
		pis = np.array([])
		boards = np.array([])
		for example in trainingExamples:
			results = np.append(results, example.result)
			pis = np.append(pis, example.pi)
			board_rep = example.gameState.board.copy()
			boards = np.append(boards, self.transformBoard(board_rep))
		self.winNN.Train(boards, results)
		self.movesNN.Train(boards, pis)
	
	def Save(self, fileName):
		fileNames = fileName.split()
        self.policyNN.Save(fileNames[0])
        self.movesNN.Save(fileNames[1])
	
	def Load(self, fileName):
		fileNames = fileName.split()
        self.policyNN.Load(fileNames[0])
        self.movesNN.Load(fileNames[1])
		
	def transformBoard(self, board_rep):
		board_rep1 = numpy.reshape(board_rep.copy(), 42)
		board_rep2 = numpy.reshape(board_rep.copy(), 42)
		board_rep1[board_rep1 != 1] = 0
		board_rep2[board_rep2 != -1] = 0
		return np.append(board_rep1, board_rep2)
		
		
class Connect4WinNN:

	def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(units = 100, activation = 'relu', input_dim = 84))
        self.model.add(Dense(units = 20, activation = 'relu'))
        self.model.add(Dense(units = 1, activation = 'softmax'))
        self.model.compile(loss = 'mean_squared_error', optimizer = 'sgd', metrics = ['accuracy'])
	
	def Predict(self, board_rep):
		return self.model.predict(board_rep)[0][0]
		
	def Train(self, board_reps, outcomes):
		self.model.fit(board_reps, outcomes, epochs = 20, batch_size = 50)
		
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
        self.model.add(Dense(units = 20,activation = 'relu'))
        self.model.add(Dense(units = 7, activation = 'softmax'))
        self.model.compile(loss = 'categorical_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])
	
	def Predict(self, board_rep):
		return self.model.predict(board_rep)[0]
		
	def Train(self, board_reps, pis):
		self.model.fit(board_reps, pis, epochs = 20, batch_size = 8)
		
	def Save(self, fileName):
		fileName = fileName + '.h5'
        self.model.save(fileName)
	
	def Load(self, fileName):
		fileName = fileName + '.h5'
        self.model = load_model(fileName)
		