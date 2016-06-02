import app
import random
from app.utils import VectorHandler

class RoomMaker:
    def addRoom(self, map, room_corner, room_size):
        new_map = map
        tiles   = map['tiles']

        if self._roomGoesPastMapEdge(map['size'], room_corner, room_size):
            raise Exception('room too big')

        if self._roomOverlapsExistingFloor(tiles, room_corner, room_size):
            raise Exception('room already exists here')

        handler = VectorHandler()
        corner, size = handler.getPositiveVectors(room_corner, room_size)

        random_char = random.choice('abcdefghijklmnop')

        for x in range(size[0]):
            for y in range(size[1]):
                y_pos = y + corner[1]
                x_pos = x + corner[0]

                tiles[y_pos][x_pos] = app.Floor()
                tiles[y_pos][x_pos].ascii_rep = random_char

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
