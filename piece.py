from main import Main

main = Main()

class Piece(object):
    def __init__(self):
        pass

    def pin(self):
        pass

    def check(self, board, team):
        print("fired")
        check = False
        kPos = main.king.getPos(board, team)

        if team:
            squares = main.occupiedSquares(False)
        else:
            squares = main.occupiedSquares(True)

        for square in squares:
            if square == kPos:
                check = True

        print(f"{check}")
        return check

p = Piece()
print(p.check(main.board.theBoard, True))
