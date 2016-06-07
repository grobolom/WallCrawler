import copy

class ShadowCaster:
    def shade(self, squares, center):
        # we'll be applying these octant transforms to the 'real' grid
        # coordinates. We have a 'xx xy' and 'yx yy' - for example, we need
        # to flip the bottom-right coordinates to the first octant, so
        # [3, 2] needs to become [2, -3]
        octant_transforms = [
            #[ 1,  0,  0,  1], # E NE
            [ 1,  0,  0, -1], # E SE
            [ 0,  1, -1,  0], # S SE
            #[ 0, -1, -1,  0], # S SW
            #[-1,  0,  0, -1], # W SW
            #[-1,  0,  0,  1], # W NW
            #[ 0, -1,  1,  0], # N NW
            #[ 0,  1,  1,  0], # N NE
        ]

        height = len(squares)
        results = [[ ' ' for i in range(height) ] for j in range(height) ]
        results[center[1]][center[0]] = '@'

        for o in octant_transforms:
            self.castShadow(1, center, [1.0, 0.0], squares, results, o)

        return results

    def castShadow(self, x, center, sector, squares, results, octant):
        center_x = center[0]
        center_y = center[1]

        child_scan = False
        last_square = ''

        top_slope    = sector[0]
        new_top_slope = top_slope
        bottom_slope = sector[1]

        for y in range(x, -1, -1):

            # this, in the loop. For example, [3, 2] in the first octant moved
            # to the third octant should turn into [2, -3]. So the new x is
            # 3 (x) * 0 + 2 (y) * 1 and the new y is 3 (x) * -1 + 2 (y) * 0.
            real_x = center_x + x * octant[0] + y * octant[1]
            real_y = center_y + x * octant[2] + y * octant[3]

            if real_x < 0 or real_y < 0 or \
               real_y >= len(squares) or real_y >= len(squares):
                return

            square = squares[real_y][real_x]
            if y == x:
                last_square = square

            nw_slope = (y + 0.5) / (x - 0.5)
            se_slope = (y - 0.5) / (x + 0.5)
            ne_slope = (y + 0.5) / (x + 0.5)

            print([x, y], [real_x, real_y], square, sector, [nw_slope, se_slope])

            if bottom_slope > nw_slope and child_scan:
                new_sector = [ new_top_slope, nw_slope ]
                print('child scan: ', x + 1, sector, new_sector)
                self.castShadow(x + 1, center, new_sector, squares, results, octant)
                break

            if bottom_slope > nw_slope:
                break

            if top_slope < se_slope:
                continue

            print(x, y, 'not skipping')

            results[real_y][real_x] = squares[real_y][real_x]

            if last_square == '#' and square == '.':
                new_top_slope = ne_slope
                child_scan = True

            if last_square == '.' and square == '#':
                new_sector = [ new_top_slope, nw_slope ]
                print('. to #: ', x + 1, sector, new_sector)
                self.castShadow(x + 1, center, new_sector, squares, results, octant)

            if y == 0 and square == '.':
                new_sector = [ new_top_slope, bottom_slope ]
                print('last scan: ', x + 1, sector, new_sector)
                self.castShadow(x + 1, center, new_sector, squares, results, octant)

            last_square = square

        return squares

    def castOctant(self, squares, octant):
        results = self.getShadowMask(squares)

        self.castLight(1, [1.0, 0.0], squares, results, octant)

        return results

    def getShadowMask(self, squares):
        height = len(squares)
        results = [[ 's' for i in range(height) ] for j in range(height) ]
        results[height - 1][0] = '@'

        return results

    def castLight(self, x, sector, squares, results, octant):
        height = x
        max_y = len(squares) - 1

        # obviously don't run off the end of any arrays
        if x > max_y:
            return

        top_slope = sector[0]
        bottom_slope = sector[1]

        # have the last square matching whatever the first one we look at so
        # if we do the matching -> not matching transitions we don't worry
        # about them screwing up on the first square
        last_square = squares[x][x]
        new_top_slope = top_slope

        # we need this to mark if we have a second scan - this way we can fire
        # off when we reach past the visible range of the scan, even though
        # that scan won't go any further
        child_scan = False

        for y in range(height, 0 - 1, -1):
            # for now we are working with a square for convenience so we have
            # to adjust the height to a reverse value
            fixed_y = max_y - y

            square = squares[fixed_y][x]

            # we care about the top left and bottom right of each square for
            # checking if it's lit. We can switch to the diagonal technique
            # by adjusting these values
            nw_slope = (y + 0.5) / (x - 0.5)
            se_slope = (y - 0.5) / (x + 0.5)

            # we need this when changing from a blocked square to an unblocked
            ne_slope = (y + 0.5) / (x + 0.5)

            # this square is past the light cone, so we're done
            if bottom_slope > nw_slope and child_scan:
                new_sector = [ new_top_slope, nw_slope ]
                self.castLight(x + 1, new_sector, squares, results, octant)
                break

            if bottom_slope > nw_slope:
                break

            # this square is before the light cone, so keep scanning for it
            if top_slope < se_slope:
                continue

            # light up the square - for now we mark it, later we'll figure out
            # how to switch it
            results[fixed_y][x] = squares[fixed_y][x]

            if last_square == '#' and square == '.':
                new_top_slope = ne_slope
                child_scan = True

            if last_square == '.' and square == '#':
                new_sector = [ new_top_slope, nw_slope ]
                self.castLight(x + 1, new_sector, squares, results, octant)

            if y == 0 and square == '.':
                new_sector = [ new_top_slope, bottom_slope ]
                self.castLight(x + 1, new_sector, squares, results, octant)

            last_square = square

        return squares
