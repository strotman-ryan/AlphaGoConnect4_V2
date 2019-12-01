#contains enums for state of board


from enum import Enum

class Result(Enum):
    Player1Win = 0
    Player2Win = 1
    Tie = 2
    NotFinished = 3