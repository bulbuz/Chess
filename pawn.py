
class Pawn(object):
    def __init__(self):
        self.isMoved = False 

    def validMoves(self, location, board): # the location of the piece (tuple d2,d4)
        validMoves = []

        if board[location[0] + 1][location[1]] == "*" and board[location[0] + 2][location[1]] == "*":
            validMoves.append((location[0]+1, location[1]))
            if not self.isMoved:
                validMoves.append((location[0] + 1, location[1]))
                validMoves.append((location[0] + 2, location[1]))

        return validMoves

# development purposes

p = Pawn()
loc = (6,3)
print(p.validMoves(loc))

