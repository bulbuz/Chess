import colorama
from colorama import Fore
from colorama import Style
from pawn import Pawn
from rook import Rook 
from king import King 
from queen import Queen 
from knight import Knight 
from bishop import Bishop
from board import Board
colorama.init()

err = Fore.RED + Style.BRIGHT + "ERROR" + Style.RESET_ALL
def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:  
        return newstring + s
    if index > len(s):
        return s + newstring

    return s[:index] + newstring + s[index + 1:]

class Main(object):
    def __init__(self):
        self.board = Board()
        self.rook = Rook()
        self.pawn = Pawn()
        self.king = King()
        self.queen = Queen()
        self.bishop = Bishop()
        self.knight = Knight()

    def takeInp(self):
        inp = input("\nEnter your pieces location > ")
        temp = input("\nEnter your destination > ") 
        return [inp, temp]
 
    def validInp(self, inp):
        return True
    '''
        if len(inp) != 2:
            return False
        elif inp[0].isalpha() and (inp[1] >= 0 and inp[1] <= 8):
            return True
        else:
            return False
    ''' 
    def piece(self, coordinates):
        if self.board.pieceType(coordinates) == 'p':
            print(f"pawn: {self.pawn.validMoves(coordinates, self.board.theBoard)}") 
            if (coordinates[2], coordinates[3]) in self.pawn.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates)
            else:
                print(f"{err}: That's not a valid move!")

        elif self.board.pieceType(coordinates) == 'b':
            print(f"bishop: {self.bishop.validMoves(coordinates, self.board.theBoard)}") 
            if (coordinates[2], coordinates[3]) in self.bishop.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates)
            else:
                print(f"{err}: That's not a valid move!")

        elif self.board.pieceType(coordinates) == 'k':
            self.board.move(self.board.theBoard, coordinates)
        
        elif self.board.pieceType(coordinates) == 'n':
            #if (coordinates[2], coordinates[3]) in self.knight.validMoves(coordinates, self.board.theBoard):
            print(self.knight.validMoves(coordinates, self.board.theBoard))
            self.board.move(self.board.theBoard, coordinates)

        elif self.board.pieceType(coordinates) == 'q':
            print(f"queen: {self.queen.validMoves(coordinates, self.board.theBoard)}")
            if (coordinates[2], coordinates[3]) in self.queen.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates)
            else:
                print(f"{err}: That's not a valid move!")

        elif self.board.pieceType(coordinates) == 'r':
            print(f"rook: {self.rook.validMoves(coordinates, self.board.theBoard)}")
            if (coordinates[2], coordinates[3]) in self.rook.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates)
            else:
                print(f"{err}: That's not a valid move!")

print("""
    WELCOME TO CHESS IN THE TERMINAL!
=========================================
        """)

if __name__ == "__main__":
    main = Main()
    while True:
        player = main.board.currentPlayer()
        main.board.printBoard(main.board.theBoard)
        x = main.takeInp()
        if main.validInp(x):
            coordinates = main.board.convertCoordinate(x)
            if main.board.validPiece(coordinates, main.board.theBoard):
                if main.board.validateTurn(coordinates):
                    main.piece(coordinates)
                else:
                    print(f"{err}: That's not valid, try again!")
                    continue
            else:
                print(f"{err}: The selected piece is not valid")
                continue
        else:
            print(f"{err}: Enter a valid option!")

