from blessed import Terminal

class MapView:
    """
    given an array of positions, grab them from the map and draw what is there
    """
    def draw(self, map, positions, objects):
        term = Terminal()

        tiles = [[
            map[y][x].getAsciiRep()
            for (x, y) in row ]
            for row in positions ]

        for obj in objects:
            if self._isOnScreen(positions, obj):
                x, y = self._getScreenPos(positions, obj)
                if map[y][x].lit == True:
                    tiles[y][x] = term.red(obj.ascii_rep)

        return tiles

    def _isOnScreen(self, positions, obj):
        rows = len(positions) - 1
        columns = len(positions[0]) - 1

        min_pos = positions[0][0]
        max_pos = positions[rows][columns]

        return obj.position[0] >= min_pos[0] and \
                obj.position[1] >= min_pos[1] and \
                obj.position[0] <= max_pos[0] and \
                obj.position[1] <= max_pos[1]


    def _getScreenPos(self, positions, obj):
        min_pos = positions[0][0]
        return (obj.position[0] - min_pos[0], obj.position[1] - min_pos[1])
