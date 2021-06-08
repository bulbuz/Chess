
class Bishop(object):
    def __init__(self):
        self.theBoard = [
            #01234567
            '********',#0
            '********',#1
            '********',#2
            '********',#3
            '********',#4
            '**B*****',#5
            '********',#6
            '********',#7
        ]

    def validMoves(self, location, board):
        validMoves = []

        if board[location[0]][location[1]].isupper(): # white
            i = 0
            while True:
                if location[0] > 0 and location[1] > 0 and location[0] < 7 and location[1] < 7:
                    i += 1
                    validMoves.append((location[0] + i, location[1]-i)) # up-right
                else:
                    break
        else:
            pass

        return validMoves

b = Bishop()
loc = [5,2]
print(b.validMoves(loc, b.theBoard))



