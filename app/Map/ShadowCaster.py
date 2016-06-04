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

        if center_slope <= top_slope and center_slope >= bottom_slope:
            return True

        if se_slope < top_slope and se_slope >= bottom_slope:
            return True

        if nw_slope <= top_slope and nw_slope > bottom_slope:
            return True

        return False

    def getSectors(self, column, start_sectors):
        height = len(column) - 1

        last_square = '.'
        if column[0] == '#':
            last_square = '#'

        top_slope = start_sectors[0][0]
        bottom_slope = start_sectors[0][1]

        sector = []
        sectors = []
        dumped = False
        for k, current in enumerate(column):
            y = height - k
            square = [height, y]
            if not self.squareInSector(square, start_sectors[0]):
                continue

            if last_square != current and current == '.':
                top_slope = (float(y) + 0.5) / (float(height) + 0.5)
                dumped = False

            if last_square != current and current == '#':
                bottom_slope = (float(y) + 0.5) / (float(height) - 0.5)
                sector = [ top_slope, bottom_slope ]
                bottom_slope = 0.0
                sectors += [ sector ]
                dumped = True

            sector = [top_slope, bottom_slope]
            last_square = current

        if not dumped:
            sectors += [ sector ]

        return sectors
