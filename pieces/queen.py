
class Queen(object):
    def __init__(self):
        pass

    def validMoves(self, location, board, captures=False):
        validMoves = []
        
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
    
        blockedPath1 = False
        blockedPath2 = False
        blockedPath3 = False
        blockedPath4 = False
        m = 0
        while m < 8:
            m+=1
            if location[0]-m >= 0 and not blockedPath1: # up
                if board[location[0]-m][location[1]].isalpha() and board[location[0]][location[1]].islower() != board[location[0]-m][location[1]].islower():
                    validMoves.append((location[0]-m, location[1]))
                    blockedPath1 = True
                    if captures:
                        if board[location[0]-m][location[1]].lower() == "k":
                            blockedPath1 = 0
                    else:
                        blockedPath1 = 1

                elif board[location[0]-m][location[1]].isalpha() and board[location[0]][location[1]].islower() == board[location[0]-m][location[1]].islower():
                    blockedPath1 = True
                
                elif not board[location[0]-m][location[1]].isalpha():
                    validMoves.append((location[0]-m, location[1]))
                
                if captures:
                    validMoves.append((location[0]-m, location[1]))

            if location[0]+m <= 7 and not blockedPath2: # down
                if board[location[0]+m][location[1]].isalpha() and board[location[0]+m][location[1]].islower() != board[location[0]][location[1]].islower():
                    validMoves.append((location[0]+m,location[1]))
                    blockedPath2 = 1
                    
                    if captures:
                        if board[location[0]+m][location[1]].lower() == "k":
                            blockedPath2 = 0
                    else:
                        blockedPath2 = 1

                elif board[location[0]+m][location[1]].isalpha() and board[location[0]][location[1]].islower() == board[location[0]+m][location[1]].islower():
                    blockedPath2 = 1

                elif not board[location[0]+m][location[1]].isalpha():
                    validMoves.append((location[0]+m,location[1]))
                
                if captures:
                    validMoves.append((location[0]+m,location[1]))

        n = 0
        while n < 8:
            n+=1
            if location[1]+n <= 7 and not blockedPath3:# right
                if board[location[0]][location[1]+n].isalpha() and board[location[0]][location[1]].islower() != board[location[0]][location[1]+n].islower():
                    validMoves.append((location[0],location[1]+n))
                    blockedPath3 = True
                    
                    if captures:
                        if board[location[0]][location[1]+n].lower() == "k":
                            blockedPath3 = False
                    else:
                        blockedPath3 = True

                elif board[location[0]][location[1]+n].isalpha() and board[location[0]][location[1]].islower() == board[location[0]][location[1]+n].islower():
                    blockedPath3 = True

                elif not board[location[0]][location[1]+n].isalpha():
                    validMoves.append((location[0],location[1]+n))
                
                if captures:
                    validMoves.append((location[0],location[1]+n))

            if location[1]-n >= 0 and not blockedPath4: # left
                if board[location[0]][location[1]-n].isalpha() and board[location[0]][location[1]].islower() != board[location[0]][location[1]-n].islower():
                    validMoves.append((location[0], location[1]-n))
                    blockedPath4 = 1
                    
                    if captures:
                        if board[location[0]][location[1]-n].lower() == "k":
                            blockedPath4 = False
                     
                elif board[location[0]][location[1]-n].isalpha() and board[location[0]][location[1]].islower() == board[location[0]][location[1]-n].islower():
                    blockedPath4 = 1

                elif not board[location[0]][location[1]-n].isalpha():
                    validMoves.append((location[0], location[1]-n))
                
                if captures:
                    validMoves.append((location[0], location[1]-n))

        return validMoves
