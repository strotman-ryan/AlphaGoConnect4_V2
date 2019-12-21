

import numpy as np

from Result import Result
from AbstractGameState import AbstractGameState
import copy

class Connect4GameState(AbstractGameState):

    def __init__(self,rep_of_board):
        self.board = rep_of_board

        
        
    '''
    return array of next possible states - impossible moves have placeholder of current state
    return array of probabilities produced by NN and renormalized
    '''
    def GetNextStatesWithProbabilites(self, neuralNetworks):
        probabilities = neuralNetworks.GetMoveProbabilites(self)
        children = []
        validProbabilities = []
        validMoves = self.getPossibleMoves()
        for move in validMoves:
            newBoard = self.addPlayerMove(move)
            children.append(Connect4GameState(newBoard))
            validProbabilities.append(probabilities[move])
        validProbabilities = validProbabilities / sum(validProbabilities) #renormalize
        return (children, validProbabilities)
        
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
        return np.array_equal(self.board, gameState.board)
    
    '''
    returns what NN determines
    if a terminal node returns the value with respect to whos turn it is
    '''
    def ProbabilityOfWinning(self,neuralNetworks):
        if not self.IsTerminal():
            return neuralNetworks.GetProbabilityOfWinning(self)
        print("Error - looking at terminal node in ProbabilityOfWinning")   
        
    '''
    return a value between [0,1] that determines the value of the end game with respct to current player
    '''
    def ValueOfWinner(self):
        if not self.IsTerminal():
            print("Error - looking at NON-terminal node in ValueOfWinner")
        board_state = self.EvaluateBoard()
        player = self.whosMove()
        if (player == 1 and board_state == Result.Player1Win):
            return 1
        if (player == -1 and board_state == Result.Player2Win):
            return 1
        if (board_state == Result.Tie):
            return .5
        return 0



    '''
    given the probilities of moves add in 0s where moves are impossible
    '''
    def CompletePi(self, arrayOfProbabilites):
        possibleMoves = self.getPossibleMoves()
        for move in range(0,7):
            if move not in possibleMoves:
                arrayOfProbabilites.insert(move,0)
        return arrayOfProbabilites
        
    '''
    returns 1 if its Player1's turn, -1 if its Player2's turn
    Can be used to simply place the correct chip as well as determine current player
    '''
    def whosMove(self):
        return 1 if sum([sum(row) for row in self.board]) == 0 else -1
        
    def GetNextStateFromHuman(self):
        self.PrintBoard()
        column = int(input("Input Valid Move From 0-6: "))
        newBoard = self.addPlayerMove(column)
        return Connect4GameState(newBoard)

    def PrintBoard(self):
        print('---------------')
        for row in range(6):
            rowString = "|"
            for column in range(7):
                if self.board[row][column] == 1:
                    rowString += "O"
                elif self.board[row][column] == -1:
                    rowString += "X"
                else:
                    rowString += " "
                rowString += "|"
            print(rowString)
            print('---------------')
                    
    def checkVertical(self, result):
        for column in range(7):
            if result != Result.NotFinished:
                break
            for row in range(3):
                if result != Result.NotFinished:
                    break
                if self.board[row][column] != 0:
                    if self.board[row][column] == self.board[row+1][column] == self.board[row+2][column] == self.board[row+3][column]:
                        if self.board[row][column] == 1:
                            result = Result.Player1Win
                        else:
                            result = Result.Player2Win
        return result

    def checkHorizontal(self,result):
        if result == Result.NotFinished:
            for row in range(6):
                if result != Result.NotFinished:
                    break
                for column in range(4):
                    if result != Result.NotFinished:
                        break
                    if self.board[row][column] != 0:
                        if self.board[row][column] == self.board[row][column+1] == self.board[row][column+2] == self.board[row][column+3]:
                            if self.board[row][column] == 1:
                                result = Result.Player1Win
                            else:
                                result = Result.Player2Win
        return result

    def checkDiagonalDownRight(self,result):
        if result == Result.NotFinished:
            for row in range(3):
                if result != Result.NotFinished:
                    break
                for column in range(4):
                    if result != Result.NotFinished:
                        break
                    if self.board[row][column] != 0:
                        if self.board[row][column] == self.board[row+1][column+1] == self.board[row+2][column+2] == self.board[row+3][column+3]:
                            if self.board[row][column] == 1:
                                result = Result.Player1Win
                            else:
                                result = Result.Player2Win
        return result

    def checkDiagonalUpRight(self,result):
        if result == Result.NotFinished:
            for row in range(3,6):
                if result != Result.NotFinished:
                    break
                for column in range(4):
                    if result != Result.NotFinished:
                        break
                    if self.board[row][column] != 0:
                        if self.board[row][column] == self.board[row-1][column+1] == self.board[row-2][column+2] == self.board[row-3][column+3]:
                            if self.board[row][column] == 1:
                                result = Result.Player1Win
                            else:
                                result = Result.Player2Win
        return result

    def checkTie(self, result):
        if result == Result.NotFinished and self.isBoardFilled():
            result = Result.Tie
        return result

    #returns an enum from Result based on board state
    def EvaluateBoard(self):
        result = Result.NotFinished;
        result = self.checkVertical(result)
        result = self.checkHorizontal(result)
        result = self.checkDiagonalDownRight(result)
        result = self.checkDiagonalUpRight(result)
        result = self.checkTie(result)
        return result
    
    #returns a set of columns that have at least one open spot
    def getPossibleMoves(self):
        moves = []
        for column in range(7):
            if self.board[0][column] == 0:
                moves.append(column)
        return moves
        
    #Update the board 
    #Assume the move is legal
    # do not alter board game
    def addPlayerMove(self,column):
        newBoard = copy.deepcopy(self.board)
        for row in range(5,-1,-1):
            if self.board[row][column] == 0:
                newBoard[row][column] = self.whosMove()
                return newBoard
        print("ERRROR")
        
    def isBoardFilled(self):
        for col in range(7):
            if self.board[0][col]==0:
                return False
        return True
    