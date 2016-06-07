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

        for y in range(height, -1, -1):
            nw_slope = (y + 0.5) / (x - 0.5)
            se_slope = (y - 0.5) / (x + 0.5)

            # this square is past the light cone, so we're done
            if bottom_slope > nw_slope:
                break

            # this square is before the light cone, so keep scanning for it
            if top_slope < se_slope:
                continue

            print(x, y, nw_slope, se_slope)
