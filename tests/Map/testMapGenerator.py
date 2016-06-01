import app
from app.Map import MapGenerator

class TestMapGenerator:

    def test_it_should_make_a_map(self):
        sut = MapGenerator()

        rooms         = 30
        min_room_size = [2, 2]
        max_room_size = [10, 10]
        map_size      = [80, 40]

        map = sut.getMap(rooms, min_room_size, max_room_size, map_size)

        # assert self._mapHasAtLeastNRooms(rooms, map, min_room_size)

    def _mapHasAtLeastNRooms(rooms, map, min_room_size):
        room_squares = min_room_size[0] * min_room_size[1]
        min_squares_needed = rooms * room_squares
        for y, row in map.items():
            for x, item in row.items():
                if type(item) != app.Tile:
                    min_squares_needed -= 1

        return min_squares_needed <= 0
