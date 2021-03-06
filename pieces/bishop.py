
class Bishop(object):
    def __init__(self):
        pass

    def validMoves(self, location, board, captures=False):
        validMoves = []

        # moves and captures
        i = 0
        blockedPathx = False
        blockedPathy = False
        while i < 8: # right diagonal
            i += 1
            if location[0]-i >= 0 and location[1]+i <= 7 and not blockedPathx: # up right
                if board[location[0]-i][location[1]+i].isalpha() and board[location[0]][location[1]].islower() != board[location[0]-i][location[1]+i].islower():
                    validMoves.append((location[0]-i, location[1]+i))
                    blockedPathx = True
                    
                    if captures:
                        if board[location[0]-i][location[1]+i].lower() == "k":
                            blockedPathx = False
                    else:
                        blockedPathx = True

                elif board[location[0]-i][location[1]+i].isalpha() and board[location[0]][location[1]].islower() == board[location[0]-i][location[1]+i].islower():
                    blockedPathx = True

                elif not board[location[0]-i][location[1]+i].isalpha():
                    validMoves.append((location[0]-i, location[1]+i))
                
                if captures:
                    validMoves.append((location[0]-i, location[1]+i))

            if location[0]+i <= 7 and location[1]-i >= 0 and not blockedPathy: # down left
                if board[location[0]+i][location[1]-i].isalpha() and board[location[0]][location[1]].islower() != board[location[0]+i][location[1]-i].islower():
                    validMoves.append((location[0]+i, location[1]-i))
                    blockedPathy = True
                    
                    if captures:
                        if board[location[0]+i][location[1]-i].lower() == "k":
                            blockedPathy = False
                    else:
                        blockedPathy = True

                elif board[location[0]+i][location[1]-i].isalpha() and board[location[0]][location[1]].islower() == board[location[0]+i][location[1]-i].islower():
                    blockedPathy = True

                elif not board[location[0]+i][location[1]-i].isalpha():
                    validMoves.append((location[0]+i, location[1]-i))
                
                if captures:
                    validMoves.append((location[0]+i, location[1]-i))

        j = 0
        blockedx = False
        blockedy = False
        while j < 8: # left diagonal
            j += 1

            if location[0]+j <= 7 and location[1]+j <= 7 and not blockedx:
                if board[location[0]+j][location[1]+j].isalpha() and board[location[0]][location[1]].islower() != board[location[0]+j][location[1]+j].islower():
                    validMoves.append((location[0]+j, location[1]+j))
                    blockedx = True
                    
                    if captures:
                        if board[location[0]+j][location[1]+j].lower() == "k":
                            blockedx = False
                    else:
                        blockedx = True

                elif board[location[0]+j][location[1]+j].isalpha() and board[location[0]][location[1]].islower() == board[location[0]+j][location[1]+j].islower():
                    blockedx = True

                elif not board[location[0]+j][location[1]+j].isalpha():
                    validMoves.append((location[0]+j, location[1]+j))
                
                if captures:
                    validMoves.append((location[0]+j, location[1]+j))

            if location[0]-j >= 0 and location[1]-j >= 0 and not blockedy:
                if board[location[0]-j][location[1]-j].isalpha() and board[location[0]][location[1]].islower() != board[location[0]-j][location[1]-j].islower():
                    validMoves.append((location[0]-j, location[1]-j))
                    blockedy = True
                    
                    if captures:
                        if board[location[0]-j][location[1]-j].lower() == "k":
                            blockedy = False
                    else:
                        blockedy = True

                elif board[location[0]-j][location[1]-j].isalpha() and board[location[0]][location[1]].islower() == board[location[0]-j][location[1]-j].islower():
                    blockedy = True

                elif not board[location[0]-j][location[1]-j].isalpha():
                    validMoves.append((location[0]-j, location[1]-j))
                
                if captures:
                    validMoves.append((location[0]-j, location[1]-j))

        return validMoves
