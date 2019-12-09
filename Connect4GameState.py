import numpy as np
import copy

import Result

class Connect4GameState(AbstractGameState):

	def __init__(self,rep_of_board):
        self.board = rep_of_board

	'''
	Returns an empty representation of the game
	'''
	def GetStartingBoard():
		rows = 6
		columns = 7
		return Connect4GameState(np.zeros((rows,columns)))
		
		
	'''
    return array of next possible states - impossible moves have placeholder of current state
    return array of probabilities produced by NN and renormalized
    '''
    def GetNextStatesWithProbabilites(self, neuralNetworks):
        probabilities = neuralNetworks.GetProbabilities(self.board)
		children = np.array()
		validMoves = self.getPossibleMoves()
		for move in range(0,7):
			newBoard = self.board.copy()
			newGameState = Connect4GameState(newBoard)
			
			if move in validMoves:
				newGameState.addPlayerMove(move)
			children.append(newGameState)
		return (children, probabilities)
		
	'''
    returns true if end of game
    '''
    def IsTerminal(self):
		return self.EvaluateBoard() != Result.NotFinished
		
	'''
    determines if two games states are the same
    return boolean
    '''
    def IsSameAs(self, gameState):
        return np.equal(self.board, gameState.board)
	
    '''
    returns what NN determines
    if a terminal node returns the value with respect to whos turn it is
    '''
    def ProbabilityOfWinning(self,neuralNetworks):
        board_state = self.EvaluateBoard()
		player = whosTurn()
		if !self.IsTerminal():
            return neuralNetworks.GetProbOfWinning(self.board)
		print("Error - looking at terminal node in ProbabilityOfWinning")
		if (player == 1 and board_state == Result.Player1Win):
			return 1
		if (player == -1 and board_state == Result.Player2Win):
			return 1
		if (board_state == Result.Tie)
			return .5
		return 0		
		
	'''
    return a value between [0,1] that determines the value of the end game with respct to current player
    '''
    @abstractmethod
    def ValueOfWinner(self):
		if !self.IsTerminal():
			print("Error - looking at NON-terminal node in ValueOfWinner")
            return neuralNetworks.GetProbOfWinning(self.board)
		board_state = self.EvaluateBoard()
		player = whosTurn()
        if (player == 1 and board_state == Result.Player1Win):
			return 1
		if (player == -1 and board_state == Result.Player2Win):
			return 1
		if (board_state == Result.Tie)
			return .5
		return 0
    
    
    '''
    determines if two games states are the same
    return boolean
    '''
    def IsSameAs(self, gameState):
		return np.equal(self.board, gameState.board)
    
    '''
    given the probilities of moves add in 0s where moves are impossible
    '''
    def CompletePi(self, arrayOfProbabilites):
		possibleMoves = self.getPossibleMoves()
		for move in range(0,7):
			if move not in possibleMoves:
				arrayOfProbabilites[move] = 0
        pass
		
	'''
	returns 1 if its Player1's turn, -1 if its Player2's turn
	Can be used to simply place the correct chip as well as determine current player
	'''
	def whosMove(self):
        return 1 if self.board.board.sum() == 0 else -1
		
	def GetNextStateFromHuman(self):
        print(self.board)
        column = int(input("Input Valid Move From 0-6: "))
		newGameState = Connect4GameState(self.board.copy())
		newGameState.addPlayerMove(column)
        return newGameState
	
	
	#returns an enum from Result based on board state
    def EvaluateBoard(self):
        result = Result.NotFinished;
        #Check Vertical 
        for column in range(7):
            if result != Result.NotFinished:
                break
            for row in range(3):
                if result != Result.NotFinished:
                    break
                if self.board[row, column] != 0:
                    if self.board[row, column] == self.board[row+1, column] and self.board[row, column] == self.board[row+2, column] and self.board[row, column] == self.board[row+3, column]:
                        if self.board[row, column] == 1:
                            result = Result.Player1Win
                        else:
                            result = Result.Player2Win
                            
        #Check Horizontal
        if result == Result.NotFinished:
            for row in range(6):
                if result != Result.NotFinished:
                    break
                for column in range(4):
                    if result != Result.NotFinished:
                        break
                    if self.board[row, column] != 0:
                        if self.board[row, column] == self.board[row, column+1] and self.board[row, column] == self.board[row, column+2] and self.board[row, column] == self.board[row, column+3]:
                            if self.board[row, column] == 1:
                                result = Result.Player1Win
                            else:
                                result = Result.Player2Win
                        
        #Check Diagonal going up right
        if result == Result.NotFinished:
            for row in range(3):
                if result != Result.NotFinished:
                    break
                for column in range(4):
                    if result != Result.NotFinished:
                        break
                    if self.board[row, column] != 0:
                        if self.board[row, column] == self.board[row+1, column+1] and self.board[row, column] == self.board[row+2, column+2] and self.board[row, column] == self.board[row+3, column+3]:
                            if self.board[row, column] == 1:
                                result = Result.Player1Win
                            else:
                                result = Result.Player2Win
        
        #Check Diagonal going down right
        if result == Result.NotFinished:
            for row in range(3,6):
                if result != Result.NotFinished:
                    break
                for column in range(4):
                    if result != Result.NotFinished:
                        break
                    if self.board[row, column] != 0:
                        if self.board[row, column] == self.board[row-1, column+1] and self.board[row, column] == self.board[row-2, column+2] and self.board[row, column] == self.board[row-3, column+3]:
                            if self.board[row, column] == 1:
                                result = Result.Player1Win
                            else:
                                result = Result.Player2Win        

        #Check Stalemate
        if result == Result.NotFinished and self.IsBoardFilled():
            result = Result.Tie
        
        return result	
	
	#returns a set of columns that have at least one open spot
	def getPossibleMoves(self):
		moves = set()
		var i = 0
		for column in range(7):
			if (len(np.where(self.board[:,column] == 0)) == 0):
				moves.push(column)
		
		return moves
		
	#Update the board 
    #Assume the move is legal
    def addPlayerMove(self,column):
        row = np.max(np.where(self.board[:,column] == 0))
        self.board[row,column] = self.whosMove()
    