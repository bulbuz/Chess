
class Bishop(object):
    def __init__(self):
        self.theBoard = [
            #01234567
            '*i*****i',#0 
            '**i***i*',#1
            '***i*i**',#2
            '****B***',#3
            '***i*i**',#4
            '**i***i*',#5
            '*i*****i',#6
            'i*******',#7
        ]

    def validMoves(self, location, board):
        validMoves = []

        # moves
        i = 0 
        while i < 8: # right diagonal
            i += 1 
            if location[0]-i >= 0 and location[1]+i <= 7: # up right
                validMoves.append((location[0]-i, location[1]+i))
             
            if location[0]+i <= 7 and location[1]-i >= 0: # down left
                validMoves.append((location[0]+i, location[1]-i))

        j = 0
        while j < 8: # left diagonal
            j += 1
            
            if location[0]+j <= 7 and location[1]+j <= 7:
                validMoves.append((location[0]+j, location[1]+j))

            if location[0]-j >= 0 and location[1]-j >= 0:
                validMoves.append((location[0]-j, location[1]-j))
    
            
        # captures
        return validMoves

b = Bishop()
loc = [3,4]
print(b.validMoves(loc, b.theBoard))

