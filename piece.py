from main import Main

main = Main()

class Piece(object):
    def __init__(self):
        main = Main()

    def pin(self):
        pass

    def check(self, board, team):
        kPos = main.king.getPos(board, team)
        print(f"king position: {kPos}")

        check = False
        squares = main.occupiedSquares(team)
        print(f"occupied squares{squares}")
        for square in squares:
            if square == kPos:
                check = True

        return check

p = Piece()
m = Main()
print(p.check(m.board.theBoard, True))
