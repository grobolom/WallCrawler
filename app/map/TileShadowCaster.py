import app
from app.map import ShadowCaster

class TileShadowCaster(ShadowCaster):
    def getShadowMask(self, squares, center):
        height = len(squares)
        width = len(squares[0])

        # we are using a list of empty squares as our 'shadow mask' - if we
        # find a square is lit, we will replace it with the real value
        results = [[ app.Tile() for i in range(width) ] for j in range(height) ]
        results[center[1]][center[0]].ascii_rep = '@'

        return results

    def isBlocked(self, square):
        return square != None and square.blocking

    def lightUpSquare(self, position, squares, results):
        x = position[0]
        y = position[1]

        results[y][x] = squares[y][x]

    def notToBlocked(self, square, last_square):
        return square.blocking and not last_square.blocking

    def blockedToNot(self, square, last_square):
        return not square.blocking and last_square.blocking
