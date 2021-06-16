class Pawn(object):
    def __init__(self):
        pass    

    def validMoves(self, location, board): # the location of the piece (tuple d2,d4)
        validMoves = []
        piece = board[location[0]][location[1]]
       
        # valid moves
        if board[location[0]][location[1]].isupper(): # white
            if board[location[0] - 1][location[1]] == "*" and board[location[0] - 2][location[1]] == "*":
                validMoves.append((location[0]-1, location[1]))
                validMoves.append((location[0]-2, location[1]))
                if location[0] == 6:
                    validMoves.append((location[0] - 2, location[1]))
            elif not board[location[0]-1].isalpha():
                validMoves.append((location[0]-1, location[1]))

        else: # black
            if board[location[0] + 1][location[1]] == "*" and board[location[0] + 2][location[1]] == "*":
                validMoves.append((location[0]+1, location[1]))
                if location[0] == 1:
                    validMoves.append((location[0] + 2, location[1]))
        
        # available captures depending on the piece color
        if board[location[0]][location[1]].islower():
            if piece.islower() != board[location[0]+1][location[1]+1].islower() and board[location[0]+1][location[1]+1].isalpha(): # checks for different colors
                validMoves.append((location[0]+1,location[1]+1))
            if piece.islower() != board[location[0]+1][location[1]-1].islower() and board[location[0]+1][location[1]-1].isalpha():
                validMoves.append((location[0]+1,location[1]-1))
        else: #white
            if piece.isupper() != board[location[0]-1][location[1]-1].isupper() and board[location[0]-1][location[1]-1].isalpha(): # checks for different colors
                validMoves.append((location[0]-1,location[1]-1))
            if piece.isupper() != board[location[0]-1][location[1]+1].isupper() and board[location[0]-1][location[1]+1].isalpha():
                validMoves.append((location[0]-1,location[1]+1))

        return validMoves

    def promotion(self, location, board):
        pass
