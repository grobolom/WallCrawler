class LightCaster:
    def getNewSectors(self, squares, sectors):
        max_y = len(squares) - 1
        result = []

        sector_index = 0
        sector = sectors[sector_index]
        last_square = squares[0]

        result = []
        done = True

        for i, square in enumerate(squares):
            y = max_y - i
            pos = [max_y, y]

            if self.squarePastSector(pos, sector):
                result += [ sector ]
                sector_index += 1

            if square == '#' and last_square == '.':
                result += [ [ sector[0], (y + 0.5) / (max_y - 0.5) ] ]
                sector = [ (y + 0.5) / (max_y - 0.5), sector[1] ]
                sector_index += 1

            if square == '.' and last_square == '#':
                sector[0] = (y + 0.5) / (max_y + 0.5)
                done = False

            last_square = square

        if not done:
            result += [ sector ]

        return result

    def getShadowedSquares(self, squares, sectors):
        max_y = len(squares) - 1
        result = []

        sector_index = 0
        sector = sectors[sector_index]

        for i, square in enumerate(squares):
            y = max_y - i
            pos = [max_y, y]

            if self.squarePastSector(pos, sector):
                sector_index += 1

            if sector_index > len(sectors) - 1:
                result += ['s']
                continue

            sector = sectors[sector_index]

            if self.squareInSector(pos, sector):
                result += ['.']
            else:
                result += ['s']

        return result

    def squarePastSector(self, square, sector):
        x = float(square[0])
        y = float(square[1])

        nw_slope = (y + 0.5) / (x - 0.5)

        bottom_slope = sector[1]

        return nw_slope < bottom_slope

    def squareInSector(self, square, sector):
        x = float(square[0])
        y = float(square[1])

        center_slope = y / x
        se_slope = (y - 0.5) / (x + 0.5)
        nw_slope = (y + 0.5) / (x - 0.5)

        top_slope = sector[0]
        bottom_slope = sector[1]

        if center_slope <= top_slope and center_slope >= bottom_slope:
            return True

        if se_slope < top_slope and se_slope >= bottom_slope:
            return True

        if nw_slope <= top_slope and nw_slope > bottom_slope:
            return True

        return False
