class MapStuff:
    def findANearbySquare(position, map):
        pos_x, pos_y = position
        map_x, map_y = map['size']

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        random.shuffle(directions)

        for d in directions:
            x = pos_x + d[0]
            y = pos_y + d[1]

            if x < 0 or y < 0 or x >= map_x or y >= map_y:
                continue

            if type(map['tiles'][y][x]) == app.Floor:
                return [x, y]
