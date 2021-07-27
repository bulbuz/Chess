
def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:
        return newstring + s
    if index > len(s):
        return s + newstring

    return s[:index] + newstring + s[index + 1:]

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

        return validMoves

    def promotion(self, location, board):

        while True: 
            piece = board[location[0]][location[1]]
            idx = location[1]
            if piece.isupper():
                if location[0] == 0:
                    inp = input("What do you want to promote to? [Q/R/B/N] > ")

                    if inp.isalpha() and inp.islower() in ["q", "r", "b", "n"]:
                        if inp == "q":
                            replacer(board[0], "q", idx)
                            break
                        
                        elif inp == "r":
                            replacer(board[0], "r", idx)
                            break

                        elif inp == "b":
                            replacer(board[0], "b", idx)
                            break
                        
                        elif inp == "n":
                            replacer(board[0], "n", idx)
                            break
            else:
                if location[0] == 7:
                    return True
