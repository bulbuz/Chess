
class Bishop(object):
    def __init__(self):
        self.theBoard = [
            #01234567
            '********',#0 
            '********',#1
            '********',#2
            '********',#3
            '********',#4
            '********',#5
            '*B******',#6
            '********',#7
        ]

    def validMoves(self, location, board):
        validMoves = []

        # moves
        i = 0 
        while i < 7:
            i += 1 
            if location[0]-i > 0 and location[1]+i < 7:
                validMoves.append((location[0]-i, location[1]+i))

            if location[0]+i < 7 and location[1]-i > 0:
                validMoves.append((location[0]+i, location[1]-i))

            if location[0]+i < 7 and location[1]+i < 7:
                validMoves.append((location[0]+i, location[1]+i))

            if location[0]-i > 0 and location[1]-i > 0:
                validMoves.append((location[0]-i, location[1]-i))
            
            else:
                break
            
        # captures

        
        return validMoves

b = Bishop()
loc = [6,1]
print(b.validMoves(loc, b.theBoard))



