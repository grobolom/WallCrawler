import app
from app.Map import MapGenerator

class TestMapGenerator:
    def test_it_should_determine_if_a_square_is_empty(self):
        pos = [0, 0]
        map = [[ app.Floor() ]]
        sut = MapGenerator()

        assert sut.isEmpty(pos, map) == False

    def test_it_should_return_true_if_a_surrounding_square_is_full(self):
        pos = [1, 1]
        map = [
            [ app.Floor(), app.Tile(), app.Tile() ],
            [ app.Floor(), app.Tile(), app.Tile() ],
            [ app.Floor(), app.Tile(), app.Tile() ],
        ]
        sut = MapGenerator()

        assert sut.hasANotEmptySquareNearby(pos, map) == True

    def test_it_should_return_false_if_the_room_will_not_fit(self):
        pos = [1, 1]
        map = [
            [ app.Floor(), app.Tile(), app.Tile() ],
            [ app.Floor(), app.Tile(), app.Tile() ],
            [ app.Floor(), app.Tile(), app.Tile() ],
        ]
        map_size = [3, 3]
        room_size = [3, 3]
        sut = MapGenerator()

        assert sut.roomWouldFit(pos, room_size, map, map_size) == False

    def test_it_should_return_true_if_the_room_will_fit(self):
        pos = [1, 1]
        map = [
            [ app.Floor(), app.Tile(), app.Tile() ],
            [ app.Floor(), app.Tile(), app.Tile() ],
            [ app.Floor(), app.Tile(), app.Tile() ],
        ]
        map_size = [3, 3]
        room_size = [2, 2]
        sut = MapGenerator()

        assert sut.roomWouldFit(pos, room_size, map, map_size) == True

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