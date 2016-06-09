import app
import random

from . import RoomMaker
from . import RandomRoomMaker

class MapGenerator:
    def getMap(self, rooms, min_room_size, max_room_size, map_size):
        map_x = map_size[0]
        map_y = map_size[1]

        map = { 
            'tiles': [[
                app.Wall() for i in range(map_x) ]
                           for j in range(map_y) ],
            'size': map_size,
        }

        map = RoomMaker().addRoom(map, [map_x // 2, map_y // 2], [4, 4])

        for i in range(rooms):
            while True:
                r = self.getRandomMapSquare(map_size)
                rs = RandomRoomMaker().getRandomRoom(min_room_size, max_room_size)
                is_valid = self.isValidPlacementSpot(r, rs, map['tiles'], map_size)

                if is_valid:
                    try:
                        map = RoomMaker().addRoom(map, r, rs)
                    except Exception:
                        continue
                    break;

        return map

    def isValidPlacementSpot(self, pos, room_size, map, map_size):
        a = self.isEmpty(pos, map)
        b = self.hasANotEmptySquareNearby(pos, map)
        c = self.roomWouldFit(pos, room_size, map, map_size)

        return a and b and c

    def getRandomMapSquare(self, map_size):
        return [
            random.randint(1, map_size[0] - 2),
            random.randint(1, map_size[1] - 2),
        ]

    def isEmpty(self, pos, map):
        x = pos[0]
        y = pos[1]
        return (
            map[y][x] == None or \
            type(map[y][x]) == app.Tile or \
            type(map[y][x]) == app.Wall
        )

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
