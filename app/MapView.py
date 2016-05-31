class MapView:
    """
    given an array of positions, grab them from the map and draw what is there
    """
    def draw(self, map, positions, objects):
        tiles = [[
            map[x][y].ascii_rep
            for (x, y) in row ]
            for row in positions ]

        for obj in objects:
            if self._isOnScreen(positions, obj):
                screen_x, screen_y = self._getScreenPos(positions, obj)
                tiles[screen_y][screen_x] = obj.ascii_rep

        return tiles

    def _isOnScreen(self, positions, obj):
        rows = len(positions) - 1
        columns = len(positions[0]) - 1

        min_pos = positions[0][0]
        max_pos = positions[rows][columns]

        return obj.x >= min_pos[0] and \
                obj.y >= min_pos[1] and \
                obj.x <= max_pos[0] and \
                obj.y <= max_pos[1]


    def _getScreenPos(self, positions, obj):
        min_pos = positions[0][0]
        return (obj.x - min_pos[0], obj.y - min_pos[1])
