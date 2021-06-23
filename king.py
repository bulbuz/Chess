
def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:  
        return newstring + s
    if index > len(s):
        return s + newstring

    return s[:index] + newstring + s[index + 1:]

def move(self, board, position): 
    column = position[0]
    row = position[1]
    destColumn = position[2]
    destRow = position[3]
    piece = board[column][row]
    
    # remove the piece and replace it with an empty slot
    newRow = replacer(board[column], '*', row)
    board[column] = newRow
    
    # put the piece at the wanted position 

    dest = replacer(board[destColumn], piece, destRow) 
    board[destColumn] = dest

    return board

class King(object):
    def __init__(self):
        self.inCheck = False
        self.isMovedb = False
        self.isMovedw = False
        self.isCastled = False

    def castle(self, location, board, wRook1, wRook2, bRook1, bRook2):
        validMoves = [] 


        if board[location[0]][location[1]].islower():
            if (board[7][5] == "*" and board[7][6] == "*") and not (self.isMovedw and wRook2):
                validMoves.append((7,6))
                #move()

            if (board[7][1] == "*" and board[7][2] == "*" and board[7][3] == "*") and not (self.isMovedw and wRook1):
                validMoves.append((7,2))

        if board[location[0]][location[1]].islower().islower() == 'b':
            if (board[0][5] == "*" and board[0][6] == "*") and not (self.isMovedb and bRook2):
                validMoves.append((0,6))

            if (board[0][1] == "*" and board[0][2] == "*" and board[0][3] == "*") and not (self.isMovedb and bRook1):
                validMoves.append((0,2))

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

