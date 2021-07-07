from main import Main

main = Main()
class Piece(object):
    def __init__(self):
        m = Main()

    def pin(self):
        pass

    def check(self, board):
        check = False 
        square = main.occupiedSquares(True)
         

        return check

p = Piece()
m = Main()
print(p.check(m.board.theBoard))
