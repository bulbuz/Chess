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
            'rnbqkbnr',
            'pppppppp',
            '********',
            '********',
            '********',
            '********',
            'pppppppp',
            'RNBQKBNR'] 
        self.lexographic = {'a': 0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
        
    def printBoard(self, board):
        print(Fore.GREEN + Style.BRIGHT + "\n\t    A B C D E F G H\n" + Style.RESET_ALL)
        for i in range(len(board)):
            print(f'\t{8-i}', end='   ')

            for j in range(len(board[i])):
                print(f"{board[i][j]}", end=' ')
            print(f'  {8-i}', end='   ')
            print()
        print(Fore.GREEN + Style.BRIGHT + "\n\t    A B C D E F G H\n" + Style.RESET_ALL)

    def getCoordinate(self, piecePos):
        x = piecePos[1]
        y = piecePos[0]

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
        row = position[1]
        column = position[0]
        destRow = position[3]
        destColumn = position[2]
        piece = board[column][row]
        
        # remove the piece and replace it with an empty slot
        newRow = replacer(board[column], '*', row)
        board[column] = newRow
        
        # put the piece at the wanted position 

        dest = replacer(board[destColumn], piece, destRow) 
        board[destColumn] = dest

        return board
    
    def checkPiece(self, board, move):
        pass
