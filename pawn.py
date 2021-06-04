from board import Board 

class Pawn(object):
    def __init__(self):
        self.isMoved = False 

    def validMoves(self, location, board): # the location of the piece (tuple d2,d4)
        validMoves = []
        piece = board[location[0]][location[1]]
        
        if board[location[0]][location[1]].isupper():
            if board[location[0] - 1][location[1]] == "*" and board[location[0] - 2][location[1]] == "*":
                validMoves.append((location[0]-1, location[1]))
                if not self.isMoved:
                    validMoves.append((location[0] - 2, location[1]))
        else:
            if board[location[0] + 1][location[1]] == "*" and board[location[0] + 2][location[1]] == "*":
                validMoves.append((location[0]+1, location[1]))
                if not self.isMoved:
                    validMoves.append((location[0] + 2, location[1]))
        
        if piece.islower() != board[location[0]+1][location[1]+1].islower() and board[location[0]+1][location[1]+1].isalpha(): # checks for different colors
            validMoves.append((location[0]+1,location[1]+1))
        if piece.islower() != board[location[0]+1][location[1]-1].islower() and board[location[0]+1][location[1]-1].isalpha():
            validMoves.append((location[0]+1,location[1]-1))

        return validMoves

# development purposes
board = Board()
p = Pawn()
loc = (1,4)
print(p.validMoves(loc, board.theBoard))

