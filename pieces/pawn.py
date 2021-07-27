
class Pawn(object):
    def __init__(self):
        pass

    def validMoves(self, location, board, captures=False): # the location of the piece (tuple d2,d4)
        validMoves = []
        piece = board[location[0]][location[1]]

        # valid moves
        if not captures: # checking if the pawn can go forward
            if piece.isupper(): # white
                if board[location[0]-1][location[1]] == "*":
                    validMoves.append((location[0]-1, location[1]))
                    if board[location[0]-2][location[1]] == "*" and location[0] == 6:
                        validMoves.append((location[0]-2, location[1]))

            else: # black
                if board[location[0] + 1][location[1]] == "*":
                    validMoves.append((location[0]+1, location[1]))
                    if board[location[0]+2][location[1]] == "*" and location[0] == 1:
                        validMoves.append((location[0]+2, location[1]))

            if board[location[0]][location[1]].islower(): # black
                if location[0]+1 <= 7 and location[1]+1 <= 7:
                    if piece.islower() != board[location[0]+1][location[1]+1].islower() and board[location[0]+1][location[1]+1].isalpha(): # checks for different colors
                        validMoves.append((location[0]+1,location[1]+1))
                if location[0]+1 <= 7 and location[1]-1 <= 0:
                    if piece.islower() != board[location[0]+1][location[1]-1].islower() and board[location[0]+1][location[1]-1].isalpha():
                        validMoves.append((location[0]+1,location[1]-1))

            else: #white
                if location[0]-1 >= 0 and location[1]-1 >= 0:
                    if piece.isupper() != board[location[0]-1][location[1]-1].isupper() and board[location[0]-1][location[1]-1].isalpha(): # checks for different colors
                        validMoves.append((location[0]-1,location[1]-1))
                if location[0]-1 >= 0 and location[1]+1 <= 7:
                    if piece.isupper() != board[location[0]-1][location[1]+1].isupper() and board[location[0]-1][location[1]+1].isalpha():
                        validMoves.append((location[0]-1,location[1]+1))

        # available captures depending on the piece color
        if captures:
            if board[location[0]][location[1]].islower(): # black
                if (location[0]+1 <= 7 and location[1]+1 <= 7) and (location[0]+1 <= 7 and location[1]-1 >= 0):
                    validMoves.append((location[0]+1,location[1]+1))
                    validMoves.append((location[0]+1,location[1]-1))
            else:
                if (location[0]-1 >= 0 and location[1]+1 <= 7 and captures) and (location[0]-1 >= 0 and location[1]-1 >= 0):
                    validMoves.append((location[0]-1,location[1]+1))
                    validMoves.append((location[0]-1,location[1]-1))

        print(f"pawn moves: {validMoves}")
        return validMoves

    def promotion(self, location, board):
        piece = board[location[0]][location[1]]
        
        if piece.isupper():
            if location[0] == 0:
                return True
        else:
            if location[0] == 7:
                return True
