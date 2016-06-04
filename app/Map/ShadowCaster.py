class ShadowCaster:
    def getShadowMap(self, octet):
        height = len(octet)
        width = len(octet[0])

        result = [[
            ' ' for col in range(width) ]
                for row in range(height) ]

        empty = True
        for x in range(width):
            for y in range(height - 1, -1, -1):
                result[y][x] = self.handleSquare(y, x, octet)
                return '#'

        return [ ''.join(row) for row in result ]

    def squareInSector(self, square, sector):
        return True
