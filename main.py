from typing import Coroutine
import colorama
from colorama import Fore 
from colorama import Style
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.king import King
from pieces.queen import Queen
from pieces.knight import Knight
from pieces.bishop import Bishop
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
        inp1 = input("\nEnter your destination > ")
        return [inp, inp1]

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

    def piece(self, coordinates, add=True):
    
        if self.board.pieceType(coordinates) == 'p':
            if (coordinates[2] == 0 or coordinates[2] == 7) and (coordinates[2], coordinates[3]) in self.pawn.validMoves(coordinates, self.board.theBoard):
                    pieceType = self.pawn.promotion()
                    if self.board.theBoard[coordinates[0]][coordinates[1]].isupper():
                        self.board.move(self.board.theBoard, coordinates, newPiece=pieceType.upper())
                    else:
                        self.board.move(self.board.theBoard, coordinates, newPiece=pieceType)
                    return True

            elif (coordinates[2], coordinates[3]) in self.pawn.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates, add)
                return True

            else:
                print(f"{err}: That's not a valid move!")


        elif self.board.pieceType(coordinates) == 'b':
            if (coordinates[2], coordinates[3]) in self.bishop.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates, add)
            else:
                print(f"{err}: That's not a valid move!")

        elif self.board.pieceType(coordinates) == 'k':
            team = False
            player = True
            if self.board.theBoard[coordinates[0]][coordinates[1]].islower():
                team = True
                player = False
            
            occupiedSquares = self.occupiedSquares(team)

            if (coordinates[2], coordinates[3]) in self.king.castle(coordinates,
            self.board.theBoard, self.rook.wRook1, self.rook.wRook2, self.rook.bRook1, self.rook.bRook2, occupiedSquares) and not self.check(self.board.theBoard, player):
                if self.board.theBoard[coordinates[0]][coordinates[1]].islower():
                    self.king.isMovedb = True

                if self.board.theBoard[coordinates[0]][coordinates[1]].isupper():
                    self.king.isMovedw = True

                self.board.move(self.board.theBoard, coordinates, add)

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

            elif (coordinates[2], coordinates[3]) in self.king.validMoves(coordinates, self.board.theBoard, occupiedSquares = occupiedSquares):

                if self.board.theBoard[coordinates[0]][coordinates[1]].islower():
                    self.king.isMovedb = True

                if self.board.theBoard[coordinates[0]][coordinates[1]].isupper():
                    self.king.isMovedw = True

                self.board.move(self.board.theBoard, coordinates, add)
                
                return True
            else:
                print(f"{err}: That's not a valid move!")
                return False

        elif self.board.pieceType(coordinates) == 'n':
            if (coordinates[2], coordinates[3]) in self.knight.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates, add)
                return True
            else:
                print(f"{err}: That's not a valid move!")
                return False

        elif self.board.pieceType(coordinates) == 'q':
            if (coordinates[2], coordinates[3]) in self.queen.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates, add)
                return True
            else:
                print(f"{err}: That's not a valid move!")
                return False 

        elif self.board.pieceType(coordinates) == 'r':
            if (coordinates[2], coordinates[3]) in self.rook.validMoves(coordinates, self.board.theBoard):
                self.board.move(self.board.theBoard, coordinates, add)

                if (coordinates[0], coordinates[1]) == (7,7):
                    self.rook.wRook2 = True

                if (coordinates[0], coordinates[1]) == (7,0):
                    self.rook.wRook1 = True

                if (coordinates[0], coordinates[1]) == (0,7):
                    self.rook.bRook2 = True

                if (coordinates[0], coordinates[1]) == (0,0):
                    self.rook.bRook1 = True
                return True
            
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
                if not team:
                    if piece.islower():
                        if piece == 'p':
                            if len(self.pawn.validMoves(coordinates, self.board.theBoard, True)) > 0:
                                validMovesb.append(self.pawn.validMoves(coordinates, self.board.theBoard, True))

                        elif piece == 'n':
                            if len(self.knight.validMoves(coordinates, self.board.theBoard)) > 0:
                                validMovesb.append(self.knight.validMoves(coordinates, self.board.theBoard, True))

                        elif piece == 'b':
                            if len(self.bishop.validMoves(coordinates, self.board.theBoard)) > 0:
                                validMovesb.append(self.bishop.validMoves(coordinates, self.board.theBoard))

                        elif piece == 'q':
                            if len(self.queen.validMoves(coordinates, self.board.theBoard)) > 0:
                                validMovesb.append(self.queen.validMoves(coordinates, self.board.theBoard))

                        elif piece == 'r':
                            if len(self.rook.validMoves(coordinates, self.board.theBoard, True)) > 0:
                                validMovesb.append(self.rook.validMoves(coordinates, self.board.theBoard, True))

                        elif piece == 'k':
                            if len(self.king.validMoves(coordinates, self.board.theBoard)) > 0:
                                validMovesb.append(self.king.validMoves(coordinates, self.board.theBoard))

                else:
                    if piece.isupper():
                        if piece == 'P':
                            if len(self.pawn.validMoves(coordinates, self.board.theBoard, True)) > 0:
                               validMovesw.append(self.pawn.validMoves(coordinates, self.board.theBoard, True))

                        elif piece == 'N':
                            if len(self.knight.validMoves(coordinates, self.board.theBoard)) > 0:
                                validMovesw.append(self.knight.validMoves(coordinates, self.board.theBoard, True))

                        elif piece == 'B':
                            if len(self.bishop.validMoves(coordinates, self.board.theBoard)) > 0:
                                validMovesw.append(self.bishop.validMoves(coordinates, self.board.theBoard))

                        elif piece == 'Q':
                            if len(self.queen.validMoves(coordinates, self.board.theBoard)) > 0:
                                validMovesw.append(self.queen.validMoves(coordinates, self.board.theBoard))

                        elif piece == 'R':
                            if len(self.rook.validMoves(coordinates, self.board.theBoard, True)) > 0:
                                validMovesw.append(self.rook.validMoves(coordinates, self.board.theBoard, True))

                        elif piece == 'K':
                            if len(self.king.validMoves(coordinates, self.board.theBoard)) > 0:
                                validMovesw.append(self.king.validMoves(coordinates, self.board.theBoard))

        validMovesb = [item for sublist in validMovesb for item in sublist]
        validMovesw = [item for sublist in validMovesw for item in sublist]
        validMovesb = list(dict.fromkeys(validMovesb))
        validMovesw = list(dict.fromkeys(validMovesw))

        if team: # team = true is white
            #print("White's occupying squares")
            #print(validMovesw)
            return validMovesw

        else:
            #print("Black's occupying squares")
            #print(validMovesb)
            return validMovesb


    def check(self, board, team): # returns true if the given player is under check
        check = False
        kPos = self.king.getPos(board, team)

        if team:
            squares = self.occupiedSquares(False)
        else:
            squares = self.occupiedSquares(True)

        for square in squares:
            if square == kPos:
                check = True
        
        print(squares)
        print(kPos)

        return check

    def stalemate(self):
        pass

    def checkmate(self, coordinates): # returns true if given player won 
        team = True
        player = False
        if self.board.theBoard[coordinates[0]][coordinates[1]].islower():
            team = False
            player = True
        
        kPos = self.king.getPos(self.board.theBoard, player) 
        kingMoves = self.king.validMoves((kPos[0], kPos[1]), self.board.theBoard, self.occupiedSquares(team))

        print(f"kMoves = {kingMoves}")
        if len(kingMoves) == 0:
            print("CHECKMATE!!")
            return True

main = Main()

def start():
    print("""
        WELCOME TO CHESS IN THE TERMINAL!
    =========================================
            """)

    while True:
        player = main.board.currentPlayer()
        main.board.printBoard(main.board.theBoard)
        inCheck = main.check(main.board.theBoard, player)

        if inCheck:
            print("CHECK!")

        inp = main.takeInp()

        if main.validInp(inp):
            coordinates = main.board.convertCoordinate(inp)
            if main.board.validPiece(coordinates, main.board.theBoard):
                if main.board.validateTurn(coordinates):
                    
                    tempPiece = main.board.theBoard[coordinates[2]][coordinates[3]]
                    temp = False
                    if main.board.theBoard[coordinates[2]][coordinates[3]].isalpha():
                        temp = True
                        t = replacer(main.board.theBoard[coordinates[2]], tempPiece, coordinates[3])
                    
                    if main.piece(coordinates):
                        moved = True
                    else:
                        moved = False

                    inCheck = main.check(main.board.theBoard, player)

                    if inCheck and moved: 
                        # puts back the piece if it's invalid
                        # and the player is asked to make another move
                        main.board.moves -= 1
                        afterCoords = []
                        afterCoords.append(coordinates[2])
                        afterCoords.append(coordinates[3])
                        afterCoords.append(coordinates[0])
                        afterCoords.append(coordinates[1])
                        main.board.theBoard = main.board.move(main.board.theBoard, afterCoords, False) 

                        if temp: 
                            main.board.theBoard[coordinates[2]] = t

                        continue

                    if main.checkmate(coordinates):
                        main.board.printBoard(main.board.theBoard)
                        print("YOOU WOOON!!!")
                        break
                    
                    else:
                        continue

                else:
                    print("validateTurn error")
                    print(f"{err}: That's not valid, try again!")
                    continue
            else:
                print(f"{err}: The selected piece is not valid")
                continue
        else:
            print(f"{err}: Enter a valid option!")

if __name__ == "__main__":
    start()
