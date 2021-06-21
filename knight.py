from piece import Piece
from board import Board

class Knight(Piece):
    def __init__(self):
        pass

    def validMoves(self, location, board):
        validMoves = []
       
        if location[0]+2 <= 7 location[1]+2 <= 7:
            if board[location[0]][location[1]].islower(): # black
                if board[location[0]+2][location[1]+1].isalpha() and board[location[0]+2][location[1]+1].islower() != board[location[0]][location[1]].islower():
                    validMoves.append(board[location[0]+2][location[1]+1])
                elif board[location[0]+2][location[1]+1]
                    pass
            else: # white
                pass

        return validMoves

loc = [3,3]
b = Board()
k = Knight()
print(k.validMoves(loc, b.theBoard))
