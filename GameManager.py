#Game Manager
from Result import Result


class GameManager:
    
    
    
    def __init__(self,game):
        self.game = game
        
    def RunGame(self):
        gameStatus = Result.NotFinished
        while(gameStatus == Result.NotFinished):
            self.game.PrintBoard()
            self.game.Move()
            self.game.ChangePlayerTurn()
            gameStatus = self.game.EvaluateBoard()
        self.game.PrintBoard()
        print(self.game.EvaluateBoard())