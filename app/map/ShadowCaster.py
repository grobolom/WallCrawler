class ShadowCaster:
    def castOctant(self, squares):
        # since we're working with a square area cols = rows
        height = len(squares)

        self.castLight(3, [1.0, 0.0], squares)

        return squares

    def castLight(self, x, sector, squares):
        height = x
        top_slope = sector[0]
        bottom_slope = sector[1]

        # have the last square matching whatever the first one we look at so
        # if we do the matching -> not matching transitions we don't worry
        # about them screwing up on the first square
        last_square = squares[height][height]
        new_top_slope = top_slope

        for fake_y in range(height - 1, len(squares) + 1):
            # for now we are working with a square for convenience so we have
            # to adjust the height to a reverse value
            y = len(squares) - fake_y
            square = squares[fake_y - 1][x]

            # we care about the top left and bottom right of each square for
            # checking if it's lit. We can switch to the diagonal technique
            # by adjusting these values
            nw_slope = (y + 0.5) / (x - 0.5)
            se_slope = (y - 0.5) / (x + 0.5)

            # we need this when changing from a blocked square to an unblocked
            ne_slope = (y + 0.5) / (x + 0.5)

            print(square, x, y, nw_slope, se_slope)

            # this square is past the light cone, so we're done
            if bottom_slope > nw_slope:
                break

            # this square is before the light cone, so keep scanning for it
            if top_slope < se_slope:
                continue

            # light up the square - for now we mark it, later we'll figure out
            # how to switch it
            squares[fake_y - 1][x] = '!'

            if last_square == '#' and square == '.':
                new_top_slope = ne_slope
                print('blocking to non-blocking', new_top_slope)

            if last_square == '.' and square == '#':
                self.castLight(x + 1, [ new_top_slope, nw_slope ], squares)
                print('non-blocking to blocking', new_top_slope, nw_slope)
