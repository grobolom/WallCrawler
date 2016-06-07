import copy

class ShadowCaster:
    def shade(self, squares, center_point):
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
