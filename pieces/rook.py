
class Rook(object):
    def __init__(self):
        # check if moved
        self.wRook1 = False # left rook
        self.wRook2 = False # right rook
        self.bRook1 = False # left rook
        self.bRook2 = False # right rook

    def validMoves(self, location, board, captures=False):
        validMoves = []

        blockedPath1 = False
        blockedPath2 = False
        blockedPath3 = False
        blockedPath4 = False

        i = 0
        while i < 8:
            i+=1
            if location[0]-i >= 0 and not blockedPath1: # up
                if board[location[0]-i][location[1]].isalpha() and board[location[0]][location[1]].islower() != board[location[0]-i][location[1]].islower():
                    validMoves.append((location[0]-i, location[1]))
                    blockedPath1 = True
                    
                    if captures:
                        if board[location[0]-i][location[1]].lower() == "k":
                            blockedPath1 = 0
                    else:
                        blockedPath1 = 1

                elif board[location[0]-i][location[1]].isalpha() and board[location[0]][location[1]].islower() == board[location[0]-i][location[1]].islower():
                    blockedPath1 = True

                elif not board[location[0]-i][location[1]].isalpha():
                    validMoves.append((location[0]-i, location[1]))

                if captures:
                    validMoves.append((location[0]-i, location[1]))

            if location[0]+i <= 7 and not blockedPath2: # down
                if board[location[0]+i][location[1]].isalpha() and board[location[0]+i][location[1]].islower() != board[location[0]][location[1]].islower():
                    validMoves.append((location[0]+i,location[1]))
                    blockedPath2 = 1
                    if captures:
                        if board[location[0]+i][location[1]].lower() == "k":
                            blockedPath2 = 0
                    else:
                        blockedPath2 = 1

                elif board[location[0]+i][location[1]].isalpha() and board[location[0]][location[1]].islower() == board[location[0]+i][location[1]].islower():
                    blockedPath2 = 1

                elif not board[location[0]+i][location[1]].isalpha():
                    validMoves.append((location[0]+i,location[1]))
                
                if captures:
                    validMoves.append((location[0]+i,location[1]))

        j = 0
        while j < 8:
            j+=1
            if location[1]+j <= 7 and not blockedPath3:# right
                if board[location[0]][location[1]+j].isalpha() and board[location[0]][location[1]].islower() != board[location[0]][location[1]+j].islower():
                    validMoves.append((location[0],location[1]+j))

                    blockedPath3 = True
                    if captures:
                        if board[location[0]][location[1]+j].lower() == "k":
                            blockedPath3 = False
                    else:
                        blockedPath3 = True

                elif board[location[0]][location[1]+j].isalpha() and board[location[0]][location[1]].islower() == board[location[0]][location[1]+j].islower():
                    blockedPath3 = True

                elif not board[location[0]][location[1]+j].isalpha():
                    validMoves.append((location[0],location[1]+j))

                if captures:
                    validMoves.append((location[0],location[1]+j))

            if location[1]-j >= 0 and not blockedPath4: # left
                if board[location[0]][location[1]-j].isalpha() and board[location[0]][location[1]].islower() != board[location[0]][location[1]-j].islower():
                    validMoves.append((location[0], location[1]-j))
                    blockedPath4 = 1
                    if captures:
                        if board[location[0]][location[1]-j].lower() == "k":
                            blockedPath4 = False
                    else:
                        blockedPath4 = True

                elif board[location[0]][location[1]-j].isalpha() and board[location[0]][location[1]].islower() == board[location[0]][location[1]-j].islower():
                    blockedPath4 = 1

                elif not board[location[0]][location[1]-j].isalpha():
                    validMoves.append((location[0], location[1]-j))
                
                if captures:
                    validMoves.append((location[0], location[1]-j))

        print(f"rook's validmoves: {validMoves}")
        return validMoves
