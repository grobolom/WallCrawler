import app

from . import RoomMaker

class MapGenerator:
    def getMap(self, rooms, min_room_size, max_rooms_size, map_size):
        pass

    def findValidPlacementSpot(self, room_size, map):
        random_square = self.getRandomMapSquare(map)

        return self.isEmpty(random_square, map) and \
               self.hasANotEmptySquareNearby(random_square, map) and \
               self.roomWouldFit(random_square, map, room_size)

    def isEmpty(self, pos, map):
        x = pos[0]
        y = pos[1]
        return map[y][x] == None or type(map[y][x]) == app.Tile

    def hasANotEmptySquareNearby(self, pos, map):
        x = pos[0]
        y = pos[1]

        return not self.isEmpty([x - 1, y], map) or \
               not self.isEmpty([x + 1, y], map) or \
               not self.isEmpty([x, y - 1], map) or \
               not self.isEmpty([x, y + 1], map)

    def roomWouldFit(self, pos, size, map, map_size):
        return not RoomMaker()._roomGoesPastMapEdge(map_size, pos, size) and \
               not RoomMaker()._roomOverlapsExistingFloor(map, pos, size)
