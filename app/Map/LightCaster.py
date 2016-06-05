class LightCaster:
    def getMask(self, squares):

        for k, x in enumerate(squares):
            print(x)

        result = []
        last_sectors = [[ 1.0, 0.0 ]]
        for k, row in enumerate(reversed(squares)):
            squares = [ s for s in list(row) if s != ' ' ]
            res = self.getShadowedSquares(squares, last_sectors)

            line = ''
            for k, s in enumerate(res):
                if s == 's':
                    line += 's'
                else:
                    line += squares[k]

            result += [ line ]
            last_sectors = self.getNewSectors(squares, last_sectors)

            if k > 11:
                print(squares)
                print(res)
                print(last_sectors)

        max_y = len(result)
        result.reverse()

        results = [ row.rjust(max_y, ' ') for row in result ]

        for k, x in enumerate(results):
            print(x + str(max_y - k - 1))

        return results

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
            x = max_y
            pos = [max_y, y]

            if self.squareBeforeSector(pos, sector):
                continue

            if self.squareInSector(pos, sector) and \
               square == '#' and last_square == '.':

                new_slope = (y + 0.5) / (x - 0.5)
                new_sector = [ sector[0], new_slope ]
                result += [ new_sector ]
                done = True

                sector = [ new_slope, sector[1] ]
                if sector[0] < sector[1]:
                    sector_index += 1
                    sector = sectors[sector_index]

            if self.squareInSector(pos, sector) and \
               square == '.' and last_square == '#':

                new_slope = (y + 0.5) / (x + 0.5)
                sector = [ new_slope, sector[1] ]

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

        if squares == ['.']:
            return ['.']

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

    def squareBeforeSector(self, square, sector):
        x = float(square[0])
        y = float(square[1])

        se_slope = (y + 0.5) / (x - 0.5)

        top_slope = sector[0]

        return se_slope > top_slope

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
