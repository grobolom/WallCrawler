import unittest

import app
from app.Map import RoomMaker

class TestRoomMaker(unittest.TestCase):
    def test_it_should_make_a_room(self):
        map = {
            'tiles': [[ None for i in range(80) ] for j in range(20) ],
            'size': [80, 20]
        }
        room_corner = (4, 4)
        room_size = (5, 5)

        r = RoomMaker()
        map = r.addRoom(map, room_corner, room_size)

        assert type(map['tiles'][8][8]) == app.Floor

    def test_it_should_not_add_a_room_off_the_edge_of_the_map(self):
        map = {
            'tiles': [[ None for i in range(3) ] for j in range(3) ],
            'size': [3, 3]
        }
        room_corner = [1, 1]
        room_size = [3, 3]

        r = RoomMaker()

        with self.assertRaises(Exception) as context:
            r.addRoom(map, room_corner, room_size)
        assert 'room too big' in context.exception

    def test_it_should_not_overlap_rooms(self):
        map = {
            'tiles': [[ None for i in range(80) ] for j in range(20) ],
            'size': [80, 20]
        }
        r = RoomMaker()

        r.addRoom(map, (0, 0), (5, 5))
        with self.assertRaises(Exception) as context:
            r.addRoom(map, (2, 2), (7, 7))

    def test_it_should_be_ok_overwriting_tiles(self):
        map = {
            'tiles': [[ app.Tile() for i in range(80) ] for j in range(20) ],
            'size': [80, 20]
        }
        room_corner = (4, 4)
        room_size = (5, 5)

        r = RoomMaker()
        map = r.addRoom(map, room_corner, room_size)

        assert type(map['tiles'][8][8]) == app.Floor
