class LightCaster:
    def getMask(self, squares):

        """
        for k, x in enumerate(squares):
            print(x)
        """

        result = []
        last_sectors = [[ 1.0, 0.0 ]]
        for k, row in enumerate(reversed(squares)):
            squares = [ s for s in list(row) if s != ' ' ]
            res = self.getShadowedSquares(squares, last_sectors)
            # print( ''.join(res).rjust(17, ' ') )

            line = ''
            for k, s in enumerate(res):
                if s == 's':
                    line += 's'
                else:
                    line += squares[k]

            result += [ line ]
            last_sectors = self.getNewSectors(squares, last_sectors)

            if k > 17:
                print(''.join(squares))
                print(''.join(res))
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

            """
            if x == 14 and y == 5:
                print(
                    x,
                    y,
                    'center: ' + str(float(y) / float(x)),
                    'nw: ' + str((float(y) + 0.5) / (float(x) - 0.5)),
                    'se: ' + str((float(y) - 0.5) / (float(x) + 0.5)),
                    self.squareBeforeSector(pos, sector),
                    self.squareInSector(pos, sector),
                    self.squarePastSector(pos, sector),
                    sector,
                    sector_index,
                )
                print(sectors)
            """

            if self.squareBeforeSector(pos, sector):
                continue

            if self.squarePastSector(pos, sector):
                result += [ sector ]
                sector_index += 1
                if sector_index >= len(sectors):
                    break
                sector = sectors[sector_index]

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

        if not done and sector != result[-1]:
            result += [ sector ]

        if len(result) == 0:
            result += [ sector ]

        return [ o for o in result if o[0] > o[1] ]

    def getShadowedSquares(self, squares, sectors):
        max_y = len(squares) - 1
        result = []

        sector_index = 0
        sector = sectors[sector_index]

        if squares == ['.']:
            return ['.']

        for i, square in enumerate(squares):
            y = max_y - i
            x = max_y
            pos = [max_y, y]

            if x == 14:
                print(
                    x,
                    y,
                    self.squareBeforeSector(pos, sector),
                    self.squareInSector(pos, sector),
                    self.squarePastSector(pos, sector),
                    'center: ' + str(float(y) / float(x)),
                    sector,
                )

            if self.squarePastSector(pos, sector):
                sector_index += 1

            if sector_index > len(sectors) - 1:
                result += ['s']
                continue

            sector = sectors[sector_index]
            # print(sector)

            if self.squareInSector(pos, sector):
                result += ['.']
            else:
                result += ['s']

        return result

    def squareBeforeSector(self, square, sector):
        x = float(square[0])
        y = float(square[1])

        if x == 0:
            return False

        se = (y - 0.5) / (x + 0.5)
        sw = (y - 0.5) / (x - 0.5)
        nw = (y + 0.5) / (x - 0.5)
        ne = (y + 0.5) / (x + 0.5)
        center = y / x
        top = sector[0]
        bottom = sector[1]

        return top < center and bottom < center

    def squarePastSector(self, square, sector):
        x = float(square[0])
        y = float(square[1])

        if x == 0:
            return False

        se = (y - 0.5) / (x + 0.5)
        sw = (y - 0.5) / (x - 0.5)
        nw = (y + 0.5) / (x - 0.5)
        ne = (y + 0.5) / (x + 0.5)
        center = y / x
        top = sector[0]
        bottom = sector[1]

        return top > center and bottom > center

    def squareInSector(self, square, sector):
        x = float(square[0])
        y = float(square[1])

        if x == 0:
            return True

        center = y / x
        se = (y - 0.5) / (x + 0.5)
        sw = (y - 0.5) / (x - 0.5)
        nw = (y + 0.5) / (x - 0.5)
        ne = (y + 0.5) / (x + 0.5)
        top = sector[0]
        bottom = sector[1]

        return (top >= center and bottom <= center)
