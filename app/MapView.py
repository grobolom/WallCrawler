class MapView:
    """
    given an array of positions, grab them from the map and draw what is there
    """
    def draw(self, map, positions):
        return [[
            map[x][y].ascii_rep
            for (x, y) in row ]
            for row in positions ]
