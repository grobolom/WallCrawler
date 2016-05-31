from app import Floor

class RoomMaker:
    def addRoom(self, map, room_corner, room_size):
        new_map = map

        if self._roomGoesPastMapEdge(map['size'], room_corner, room_size):
            raise Exception('room too big')

        tiles = map['tiles']
        for x in range(room_size[0]):
            for y in range(room_size[1]):
                tiles[y + room_corner[1]][x + room_corner[0]] = Floor()

        new_map['tiles'] = tiles

        return new_map

    def _roomGoesPastMapEdge(self, map_size, room_corner, room_size):
        return room_corner[0] + room_size[0] - 1 > map_size[0] or \
               room_corner[1] + room_size[1] - 1 > map_size[1]
