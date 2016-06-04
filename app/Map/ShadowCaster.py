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
        x = float(square[0])
        y = float(square[1])

        center_slope = y / x
        se_slope = (y - 0.5) / (x + 0.5)
        nw_slope = (y + 0.5) / (x - 0.5)

        top_slope = sector[0]
        bottom_slope = sector[1]

        print(center_slope, top_slope, bottom_slope)

        if center_slope <= top_slope and center_slope >= bottom_slope:
            return True

        if se_slope < top_slope and se_slope >= bottom_slope:
            return True

        if nw_slope <= top_slope and nw_slope > bottom_slope:
            return True

        return False
