from pawn import Pawn
from rook import Rook
from king import King
from queen import Queen
from knight import Knight
from bishop import Bishop
from board import Board

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

    def takeInp(self):
        inp = input("\nEnter your pieces location > ")
        temp = input("\nEnter your destination > ") 
        return [inp, temp]

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
        coordinates = main.board.convertCoordinate(x)
        if main.board.validPiece(coordinates, main.board.theBoard):
            if main.board.validateTurn(coordinates):

                if main.board.pieceType(coordinates) == 'p':
                    #print(coordinates[2],coordinates[3])
                    #print(main.pawn.validMoves(coordinates, main.board.theBoard))
                    if (coordinates[2], coordinates[3]) in main.pawn.validMoves(coordinates, main.board.theBoard):
                        main.board.move(main.board.theBoard, coordinates)
                        main.pawn.isMoved = True
                    else:
                        print("That's not a valid move!")

                elif main.board.pieceType(coordinates) == 'b':
                    main.board.move(main.board.theBoard, coordinates)

                elif main.board.pieceType(coordinates) == 'k':
                    main.board.move(main.board.theBoard, coordinates)
                
                elif main.board.pieceType(coordinates) == 'n':
                    main.board.move(main.board.theBoard, coordinates)

                elif main.board.pieceType(coordinates) == 'q':
                    main.board.move(main.board.theBoard, coordinates)

                elif main.board.pieceType(coordinates) == 'r':
                    main.board.move(main.board.theBoard, coordinates)

            else:
                print("That's not valid, try again!")
                continue
        else:
            print("The selected piece is not valid")
            continue

