import copy

class ShadowCaster:
    # we'll be applying these octant transforms to the 'real' grid
    # coordinates. We have a 'xx xy' and 'yx yy' - for example, we need
    # to flip the bottom-right coordinates to the first octant, so
    # [3, 2] needs to become [2, -3]
    OCTANT_TRANSFORMS = [
        [ 1,  0,  0,  1], # E NE
        [ 1,  0,  0, -1], # E SE
        [ 0,  1, -1,  0], # S SE
        [ 0, -1, -1,  0], # S SW
        [-1,  0,  0, -1], # W SW
        [-1,  0,  0,  1], # W NW
        [ 0, -1,  1,  0], # N NW
        [ 0,  1,  1,  0], # N NE
    ]

    def shade(self, squares, center):
        results = self.getShadowMask(squares, center)

        for o in self.OCTANT_TRANSFORMS:
            self.castShadow(1, center, [1.0, 0.0], squares, results, o)

        return results

    def getShadowMask(self, squares, center):
        height = len(squares)
        width = len(squares[0])

        # we are using a list of empty squares as our 'shadow mask' - if we
        # find a square is lit, we will replace it with the real value
        results = [[ ' ' for i in range(width) ] for j in range(height) ]
        results[center[1]][center[0]] = '@'

        return results


    def castShadow(self, col, center, sector, squares, results, octant):
        center_x = center[0]
        center_y = center[1]

        top_slope    = sector[0]
        bottom_slope = sector[1]

        for x in range(col, len(squares[0])):
            last_square = ''
            for y in range(x, -1, -1):

                # this, in the loop. For example, [3, 2] in the first octant moved
                # to the third octant should turn into [2, -3]. So the new x is
                # 3 (x) * 0 + 2 (y) * 1 and the new y is 3 (x) * -1 + 2 (y) * 0.
                real_x = center_x + x * octant[0] + y * octant[1]
                real_y = center_y + x * octant[2] + y * octant[3]

                if real_x < 0 or real_y < 0 or \
                   real_x >= len(squares[0]) or real_y >= len(squares):
                    continue

                square = squares[real_y][real_x]

                # for proper handling of transitions from blocked to non-, we
                # want to treat the square before the first as matching the
                # first square
                if y == x:
                    last_square = square

                # these slopes can be adjusted to handle calculations using
                # integer math but also for different vision styles like
                # diagonal corners
                nw_slope = (y + 0.5) / (x - 0.5)
                se_slope = (y - 0.5) / (x + 0.5)
                ne_slope = (y + 0.5) / (x + 0.5)

                # means the square we are looking at is past the light sector,
                # so we don't have to keep walking down the column
                if bottom_slope >= nw_slope:
                    break

                # we haven't reached the sector yet
                if top_slope <= se_slope:
                    continue

                results[real_y][real_x] = squares[real_y][real_x]

                # blocked to non-blocked - we set the top slope of the existing
                # sector to the se corner of the previous square, which is the
                # ne sector of the current one. Now when we keep going further
                # down the x coordinates with this scan, we will shrink more
                # and more as we hit more blocked squares
                if self.blockedToNot(square, last_square):
                    top_slope = ne_slope

                # if we hit a blocking square from a non-blocking square, we 
                # start a child scan - but then we continue scanning with
                # the current one. In this way our scans split into two
                # when we reach a blocking square in the middle of a column - 
                # the new scan takes over the top portion and the original scan
                # continues down the bottom portion
                if last_square == '.' and square == '#':
                    new_sector = [ top_slope, nw_slope ]
                    self.castShadow(x + 1, center, new_sector, squares, results, octant)

                last_square = square

            # this is important for ending a scan if we ended on a set of
            # blocking squares. Since we create a child scan when we hit a
            # blocker, if we hit the bottom of the row without finding any more
            # open squares we need to end our current scan - the last child scan
            # will take over for us
            #
            # ......... -> ........
            # @...#.... -> @...#
            #
            if last_square == '#':
                break
    def blockedToNot(self, square, last_square):
        if last_square == '#' and square == '.':
            return True
        return False
