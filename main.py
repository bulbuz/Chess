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
        main.board.printBoard(main.board.theBoard)
        x = main.takeInp()
        coordinates = main.board.convertCoordinate(x)
        print(coordinates)
        if main.board.validateTurn(coordinates):
            main.board.move(main.board.theBoard, coordinates)


