from main import Main

main = Main()
class Piece:
    def __init__(self):
        m = Main()

    def pin(self):
        pass

    def check(self, board):
        square = main.occupiedSquares(True)
        print(square)

p = Piece()
m = Main()
p.check(m.board.theBoard)