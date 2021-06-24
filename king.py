
class King(object):
    def __init__(self):
        self.inCheck = False
        self.isMovedb = False
        self.isMovedw = False
        self.isCastled = False

    def castle(self, location, board, wRook1, wRook2, bRook1, bRook2):
        validMoves = [] 

        if board[location[0]][location[1]].isupper():
            if (board[7][5] == "*" and board[7][6] == "*") and (self.isMovedw == False and wRook2 == False):
                validMoves.append((7,6))
                #move()

            if (board[7][1] == "*" and board[7][2] == "*" and board[7][3] == "*") and not (self.isMovedw and wRook1):
                validMoves.append((7,2))

        if board[location[0]][location[1]].islower():
            if (board[0][5] == "*" and board[0][6] == "*") and not (self.isMovedb and bRook2):
                validMoves.append((0,6))

            if (board[0][1] == "*" and board[0][2] == "*" and board[0][3] == "*") and not (self.isMovedb and bRook1):
                validMoves.append((0,2))

        print(validMoves)
        return validMoves

    def validMoves(self, location, board):
        validMoves = [] 
        # check if moved
        if board[location[0]][location[1]].islower():
            self.isMovedb = True

        if board[location[0]][location[1]].isupper():
            self.isMovedw = True

        # moves 
        piece = board[location[0]][location[1]]

        if location[0]+1 <= 7:
            if board[location[0]+1][location[1]].isalpha() and board[location[0]+1][location[1]].islower() != piece.islower():
                validMoves.append((location[0]+1, location[1]))
            elif board[location[0]+1][location[1]] == "*":
                validMoves.append((location[0]+1, location[1]))

        if location[0]-1 >= 0:
            if board[location[0]-1][location[1]].isalpha() and board[location[0]-1][location[1]].islower() != piece.islower():
                validMoves.append((location[0]-1, location[1]))
            elif board[location[0]-1][location[1]] == "*":
                validMoves.append((location[0]-1, location[1]))

        if location[1]+1 <= 7:
            if board[location[0]][location[1]+1].isalpha() and board[location[0]][location[1]+1].islower() != piece.islower():
                validMoves.append((location[0], location[1]+1))
            elif board[location[0]][location[1]+1] == "*":
                validMoves.append((location[0], location[1]+1))

        if location[1]-1 >= 0:
            if board[location[0]][location[1]-1].isalpha() and board[location[0]][location[1]-1].islower() != piece.islower():
                validMoves.append(location[0], location[1]-1)
            elif board[location[0]][location[1]-1] == "*":
                validMoves.append((location[0], location[1]-1))
       
        if location[0]-1 >= 0 and location[1]+1 <= 7:
            if board[location[0]-1][location[1]+1].isalpha() and board[location[0]-1][location[1]+1].islower() != piece.islower():
                validMoves.append((location[0]-1, location[1]+1))
            elif board[location[0]-1][location[1]+1] == "*":
                validMoves.append((location[0]-1, location[1]+1))

        if location[0]-1 >= 0 and location[1]-1 >= 0:
            if board[location[0]-1][location[1]-1].isalpha() and board[location[0]-1][location[1]-1].islower() != piece.islower():
                validMoves.append((location[0]-1, location[1]-1))
            elif board[location[0]-1][location[1]-1] == "*":
                validMoves.append((location[0]-1, location[1]-1))

        if location[0]+1 <= 7 and location[1]+1 <= 7:
            if board[location[0]+1][location[1]+1].isalpha() and board[location[0]+1][location[1]+1].islower() != piece.islower():
                validMoves.append((location[0]+1, location[1]+1))
            elif board[location[0]+1][location[1]+1] == "*":
                validMoves.append((location[0]+1, location[1]+1))

        if location[0]+1 <= 7 and location[1]-1 >= 0:
            if board[location[0]+1][location[1]-1].isalpha() and board[location[0]+1][location[1]-1].islower() != piece.islower():
                validMoves.append((location[0]+1, location[1]-1))
            elif board[location[0]+1][location[1]-1] == "*":
                validMoves.append((location[0]+1, location[1]-1))

        print(validMoves)
        return validMoves

