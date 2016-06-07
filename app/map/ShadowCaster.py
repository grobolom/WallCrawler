import copy

class ShadowCaster:
    def shade(self, squares, center):
        # we'll be applying these octant transforms to the 'real' grid
        # coordinates. We have a 'xx xy' and 'yx yy' - for example, we need
        # to flip the bottom-right coordinates to the first octant, so
        # [3, 2] needs to become [2, -3]
        octant_transforms = [
            [ 1,  0,  0,  1], # E NE
            [ 1,  0,  0, -1], # E SE
            [ 0,  1, -1,  0], # S SE
            [ 0, -1, -1,  0], # S SW
            [-1,  0,  0, -1], # W SW
            [-1,  0,  0,  1], # W NW
            [ 0, -1,  1,  0], # N NW
            [ 0,  1,  1,  0], # N NE
        ]

        height = len(squares)
        width = len(squares[0])

        results = [[ ' ' for i in range(width) ] for j in range(height) ]
        results[center[1]][center[0]] = '@'

        for o in octant_transforms:
            self.castShadow(1, center, [1.0, 0.0], squares, results, o)

        return results

    def castShadow(self, col, center, sector, squares, results, octant):
        print('entering sector: ', sector)
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
                if y == x:
                    last_square = square

                nw_slope = (y + 0.5) / (x - 0.5)
                se_slope = (y - 0.5) / (x + 0.5)
                ne_slope = (y + 0.5) / (x + 0.5)

                if bottom_slope >= nw_slope:
                    break

                if top_slope <= se_slope:
                    continue

                results[real_y][real_x] = squares[real_y][real_x]

                if last_square == '#' and square == '.':
                    top_slope = ne_slope

                if last_square == '.' and square == '#':
                    new_sector = [ top_slope, nw_slope ]
                    self.castShadow(x + 1, center, new_sector, squares, results, octant)

                last_square = square

            if last_square == '#':
                break
