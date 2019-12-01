#Title: Main game of connect 4
#Synopsis: Make the main game loop for connect 4

from Game import Game
from HumanPlayer import HumanPlayer
from GameManager import GameManager
from RandomPlayer import RandomPlayer

numOfHumans = int(input("Enter the number of human players (0, 1 or 2): "))

if numOfHumans == 0:
	player1 = RandomPlayer()
	player2 = RandomPlayer()
elif numOfHumans == 1:
	goesFirst = input("Would you like to go first? (y or n): ")
	if goesFirst == "y":
		player1 = HumanPlayer()
		player2 = RandomPlayer()
	else:
		player1 = RandomPlayer()
		player2 = HumanPlayer()
else:
	player1 = HumanPlayer()
	player2 = HumanPlayer()

game = Game(player1, player2,7,6)

manager = GameManager(game)
manager.RunGame()





    


