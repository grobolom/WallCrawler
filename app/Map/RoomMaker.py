import app

class RoomMaker:
    def addRoom(self, map, room_corner, room_size):
        new_map = map
        tiles   = map['tiles']

        if self._roomGoesPastMapEdge(map['size'], room_corner, room_size):
            raise Exception('room too big')

        if self._roomOverlapsExistingFloor(tiles, room_corner, room_size):
            raise Exception('room already exists here')

        for x in range(room_size[0]):
            for y in range(room_size[1]):
                tiles[y + room_corner[1]][x + room_corner[0]] = app.Floor()

        new_map['tiles'] = tiles

        return new_map

    def _roomGoesPastMapEdge(self, map_size, room_corner, room_size):
        return room_corner[0] + room_size[0] > map_size[0] or \
               room_corner[1] + room_size[1] > map_size[1]

    def _roomOverlapsExistingFloor(self, tiles, corner, size):
        for x in range(size[0]):
            for y in range(size[1]):
                t = tiles[y + corner[1]][x + corner[0]]
                if t != None and type(t) != app.Tile:
                    return True
        return False
