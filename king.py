
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

    def validMoves(self, location, board, player, wRook1, wRook2, bRook1, bRook2):
        validMoves = [] 
        # check if moved
        if board[location[0]][location[1]].islower():
            self.isMovedb = True

        if board[location[0]][location[1]].isupper():
            self.isMovedw = True

        # castling
        
        if player.lower() == 'w':
            if (board[7][5] == "*" and board[7][6] == "*") and not (self.isMovedw and wRook2):
                validMoves.append((7,6))

            if (board[7][1] == "*" and board[7][2] == "*" and board[7][3] == "*") and not (self.isMovedw and wRook1):
                validMoves.append((7,2))

        if player.lower() == 'b':
            if (board[0][5] == "*" and board[0][6] == "*") and not (self.isMovedb and bRook2):
                validMoves.append((0,6))

            if (board[0][1] == "*" and board[0][2] == "*" and board[0][3] == "*") and not (self.isMovedb and bRook1):
                validMoves.append((0,2))

        # moves
        piece = board[location[0]][location[1]]
        down = board[location[0]+1][location[1]]
        up = board[location[0]][location[1]-1]
        right = board[location[0]][location[1]+1]
        left = board[location[0]][location[1]-1] 
        upRight = board[location[0]-1][location[1]+1]
        upLeft = board[location[0]-1][location[1]-1]
        downRight = board[location[0]+1][location[1]+1]
        downRight = board[location[0]+1][location[1]-1]

        if location[0]+1 <= 7:
            if down.alpha() and down.lower() != piece.lower():
                validMoves.append((location[0]+1, location[1]))
            elif down == "*":
                validMoves.append((location[0]+1, location[1]))

        if location[0]-1 >= 0:
            if up.alpha() and up.lower() != piece.lower():
                validMoves.append((location[0]-1, location[1]))
            elif up == "*":
                validMoves.append((location[0]-1, location[1]))

        if location[1]+1 <= 7:
            if right.alpha() and right.lower() != piece.lower():
                validMoves.append((location[0], location[1]+1))
            elif right == "*":
                validMoves.append((location[0], location[1]+1))

        if location[1]-1 >= 0:
            if left.alpha() and left.lower() != piece.lower():
                validMoves.append(location[0], location[1]-1)
       
        if location[0]-1 >= 0 and location[1]+1 <= 7:
            if upRight.alpha() and upRight.lower() != piece.lower():
                valdiMoves.append((location[0]-1, location[1]+1))
        


        print(validMoves)
        return validMoves

