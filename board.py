import colorama
from colorama import Fore
from colorama import Style
colorama.init()

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:  
        return newstring + s
    if index > len(s):
        return s + newstring

    return s[:index] + newstring + s[index + 1:]

class Board(object):
    def __init__(self):
        self.theBoard = [
            #01234567
            'rnbqkbnr',#0
            'pppppppp',#1
            '********',#2
            '********',#3
            '***r****',#4
            '********',#5
            'PPPPPPPP',#6
            'RNBQKBNR']#7 
        self.lexographic = {'a': 0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
        self.moves = 0 # keeps track of the moves
        self.player = 0 # 0 is white

    def printBoard(self, board):
        print(Fore.GREEN + Style.BRIGHT + "\n\t    A B C D E F G H\n" + Style.RESET_ALL)
        for i in range(len(board)):
            print(f'\t{8-i}', end='   ')

            for j in range(len(board[i])):
                print(f"{board[i][j]}", end=' ')
            print(f'  {8-i}', end='   ')
            print()
        print(Fore.GREEN + Style.BRIGHT + "\n\t    A B C D E F G H\n" + Style.RESET_ALL)

    def pieceType(self, location):
        piece = self.theBoard[location[0]][location[1]]
        return piece.lower()

    def convertCoordinate(self, position): # inputs a list [d2, d4]
        row = position[0][0]
        column = position[0][1]

        destRow = position[1][0]
        destColumn = position[1][1]

        newColumn = 8 - int(column)
        destColumn = 8 - int(destColumn)

        newRow = self.lexographic[row] 
        destRow = self.lexographic[destRow]

        return newColumn, newRow, destColumn, destRow 

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

        self.moves += 1 # add everytime a player moves
        return board

    def validateTurn(self, move): # takes in the coordinates of the piece
        if self.moves % 2 == 0:
            self.player = 0
        
        elif self.moves % 2 == 1:
            self.player = 1

        if self.moves % 2 == 0 and self.player == 0:
            if self.theBoard[move[0]][move[1]].isupper():
                return True
        elif self.moves % 2 == 1 and self.player == 1:
            if self.theBoard[move[0]][move[1]].islower():
                return True
        else:
            return False
    

    def validPiece(self, location, board):
        if not board[location[0]][location[1]].isalpha():
            return False
        else:
            return True

    def currentPlayer(self):
        if self.moves % 2 == 0:
            print("White's Turn")
        else:
            print("Black's Turn")

    def stalemate(self):
        pass

    def checkMate(self):
        pass



