import app

class MapGenerator:
    def getMap(self, rooms, min_room_size, max_rooms_size, map_size):
        pass

    def findValidPlacementSpot(self, room_size, map):
        random_square = self.getRandomMapSquare(map)

        return self.isEmpty(random_square, map) and \
               self.hasANotEmptySquareNearby(random_square, map) and \
               self.roomWouldFit(random_square, map)

    def isEmpty(self, pos, map):
        x = pos[0]
        y = pos[1]
        return map[y][x] == None or type(map[y][x]) == app.Tile
