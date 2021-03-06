
class King(object):
    def __init__(self):
        self.inCheckw = False
        self.inCheckb = False
        self.isMovedb = False
        self.isMovedw = False

    def castle(self, location, board, wRook1, wRook2, bRook1, bRook2, enemySquares):
        validMoves = []

        if board[location[0]][location[1]].isupper():
            if (board[7][5] == "*" and board[7][6] == "*") and (self.isMovedw == False and wRook2 == False):
                if (7,5) not in enemySquares and (7,6) not in enemySquares:
                    print(f"enemy square {enemySquares}")
                    validMoves.append((7,6))

            if (board[7][1] == "*" and board[7][2] == "*" and board[7][3] == "*") and (self.isMovedw == False and wRook1 ==  False):
                if (7,1) not in enemySquares and (7,2) not in enemySquares and (7,3) not in enemySquares:
                    validMoves.append((7,2))

        if board[location[0]][location[1]].islower():
            if (board[0][5] == "*" and board[0][6] == "*") and not (self.isMovedb and bRook2):
                if (0,5) not in enemySquares and (0,6) not in enemySquares:
                    validMoves.append((0,6))

            if (board[0][1] == "*" and board[0][2] == "*" and board[0][3] == "*") and (self.isMovedb == False and bRook1 == False):
                if (0,1) not in enemySquares and (0,2) not in enemySquares and (0,3) not in enemySquares:
                    validMoves.append((0,2))

        return validMoves

    def validMoves(self, location, board, occupiedSquares=[]):
        validMoves = []

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
                validMoves.append((location[0], location[1]-1))
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

        temp = []
        for i in range(len(validMoves)):
            if validMoves[i] in occupiedSquares:
                temp.append(validMoves[i])

        #print(f"validMoves before: {validMoves}")
        print(f"occupiedSquares: {occupiedSquares}")
        print(f"temp: {temp}")
        for mv in temp:
            if mv in validMoves:
                validMoves.remove(mv)

        print(validMoves) 
        
        return validMoves

    def getPos(self, board, color):
        for i in range(len(board)):
            for j in range(len(board)):
                if color:
                    if board[i][j] == "K":
                        return (i,j)
                else:
                    if board[i][j] == "k":
                        return (i,j)
        return 1
