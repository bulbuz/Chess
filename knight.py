from piece import Piece
from main import Main

class Knight(Piece):
    def __init__(self):
        pass

    def validMoves(self, location, board):
        validMoves = []

        x = 0
        y = 0
        
        for i in range(8):
            if board[location[0]][location[0]].islower(): # down left
                if location[0]+2 <= 8 and location[1] <=8:
                    if board[location[0]+2][location[1]+1].isalpha() and board[location[0]][location[1]].islower() != board[location[0]+2][location[1]+1].islower():
                        validMoves.append((location[0]+2, location[1]+1))
        print(validMoves)
        return validMoves
       
m = Main()
k = Knight()
k.validMoves()
