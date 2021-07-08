from main import Main

main = Main()

class Piece(object):
    def __init__(self):
        main = Main()

    def pin(self):
        pass

    def check(self, board, team):
        if team:
            kPos = main.king.getPos(board, False)
        else:
            kPos = main.king.getPos(board, True)


        check = False
        squares = main.occupiedSquares(team)
        for square in squares:
            if square == kPos:
                check = True

        print(f"{check}")
        return check

p = Piece()
m = Main()
print(p.check(m.board.theBoard, False))
