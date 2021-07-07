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
            if (coordinates[2], coordinates[3]) in self.king.castle(coordinates, self.board.theBoard, self.rook.wRook1, self.rook.wRook2, self.rook.bRook1, self.rook.bRook2):
                if self.board.theBoard[coordinates[0]][coordinates[1]].islower():
                    self.king.isMovedb = True

                if self.board.theBoard[coordinates[0]][coordinates[1]].isupper(): self.king.isMovedw = True 
                self.board.move(self.board.theBoard, coordinates)

                # move the rook
                if (coordinates[2], coordinates[3]) == (7,6):
                    self.board.move(self.board.theBoard, (7,7,7,5), add=False) 
                    self.rook.wRook2 = True

                if (coordinates[2], coordinates[3]) == (7,2):
                    self.board.move(self.board.theBoard, (7,0,7,3), add=False) 
                    self.rook.wRook1 = True
                
                if (coordinates[2], coordinates[3]) == (0,6):
                    self.board.move(self.board.theBoard, (0,7,0,5), add=False)
                    self.rook.bRook2 = True

                if (coordinates[2], coordinates[3]) == (0,2):
                    self.board.move(self.board.theBoard, (0,0,0,3), add=False)
                    self.rook.bRook1 = True
                 
            elif (coordinates[2], coordinates[3]) in self.king.validMoves(coordinates, self.board.theBoard):

                print(self.board.theBoard[coordinates[0]][coordinates[1]])

                if self.board.theBoard[coordinates[0]][coordinates[1]].islower():
                    self.king.isMovedb = True

                if self.board.theBoard[coordinates[0]][coordinates[1]].isupper():
                    self.king.isMovedw = True

                self.board.move(self.board.theBoard, coordinates)

            else:
                print(f"{err}: That's not a valid move!")
        
        elif self.board.pieceType(coordinates) == 'n':
            print(self.knight.validMoves(coordinates, self.board.theBoard))
            if (coordinates[2], coordinates[3]) in self.knight.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates)
            else:
                print(f"{err}: That's not a valid move!")

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
        
    def occupiedSquares(self, team): # team refers to black or white
        validMovesw = []
        validMovesb = []

        for i in range(8):
            for j in range(8):
                piece = self.board.theBoard[i][j]
                if not piece.isalpha(): 
                    continue
                
                coordinates = (i,j) 

                if piece.islower():
                    if piece == 'p':
                        if len(self.pawn.validMoves(coordinates, self.board.theBoard, True)) > 0:
                            validMovesb.append(self.pawn.validMoves(coordinates, self.board.theBoard))
                    
                    elif piece == 'n':
                        if len(self.knight.validMoves(coordinates, self.board.theBoard)) > 0:
                            validMovesb.append(self.knight.validMoves(coordinates, self.board.theBoard))
                
                    elif piece == 'b':
                        if len(self.bishop.validMoves(coordinates, self.board.theBoard)) > 0:
                            validMovesb.append(self.bishop.validMoves(coordinates, self.board.theBoard))

                    elif piece == 'q':
                        if len(self.queen.validMoves(coordinates, self.board.theBoard)) > 0:
                            validMovesb.append(self.queen.validMoves(coordinates, self.board.theBoard))
                    
                    elif piece == 'r':
                        if len(self.rook.validMoves(coordinates, self.board.theBoard)) > 0: 
                            validMovesb.append(self.rook.validMoves(coordinates, self.board.theBoard))

                else:
                    if piece == 'P':
                        if len(self.pawn.validMoves(coordinates, self.board.theBoard, True)) > 0:
                           validMovesw.append(self.pawn.validMoves(coordinates, self.board.theBoard))
                    
                    elif piece == 'N':
                        if len(self.knight.validMoves(coordinates, self.board.theBoard)) > 0:
                            validMovesw.append(self.knight.validMoves(coordinates, self.board.theBoard))
                
                    elif piece == 'B':
                        if len(self.bishop.validMoves(coordinates, self.board.theBoard)) > 0:
                            validMovesw.append(self.bishop.validMoves(coordinates, self.board.theBoard))

                    elif piece == 'Q':
                        if len(self.queen.validMoves(coordinates, self.board.theBoard)) > 0:
                            validMovesw.append(self.queen.validMoves(coordinates, self.board.theBoard))
                    
                    elif piece == 'R':
                        if len(self.rook.validMoves(coordinates, self.board.theBoard)) > 0: 
                            validMovesw.append(self.rook.validMoves(coordinates, self.board.theBoard))

        validMovesb = [item for sublist in validMovesb for item in sublist] 
        validMovesw = [item for sublist in validMovesw for item in sublist] 
        
        if team:
            return validMovesw
        else:
            return validMovesb

print("""
    WELCOME TO CHESS IN THE TERMINAL!
=========================================
        """)

main = Main()

def start():
    while True:
        print(main.occupiedSquares(True))
        player = main.board.currentPlayer()
        main.board.printBoard(main.board.theBoard)
        #main.occupiedSquares(True)
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

if __name__ == "__main__":
    start()

