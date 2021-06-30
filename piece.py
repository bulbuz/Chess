

class Piece:
    def __init__(self):
        pass

    def pin(self):
        pass

    def check(self, validMoves, board):
        for coordinates in validMoves:
            for idx, value in enumerate(coordinates):
                if board[value][idx+1] == 'k':
                    return True

