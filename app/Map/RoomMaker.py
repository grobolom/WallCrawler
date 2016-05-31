from app import Floor

class RoomMaker:
    def addRoom(self, map, room_corner, room_size):
        new_map = map

        tiles = map['tiles']
        for x in range(room_size[0]):
            for y in range(room_size[1]):
                tiles[y + room_corner[1]][x + room_corner[0]] = Floor()

        new_map['tiles'] = tiles

        return new_map
