import app

class MapToTileConverter:
    def convertToTiles(self, squares):
        return [[
            self.getTile(square) for square in row ]
                            for row in squares ]

    def getTile(self, square):
        if square == '.':
            return app.Floor()
        if square == '#':
            return app.Wall()
        return app.Tile()
