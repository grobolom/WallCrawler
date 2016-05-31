import unittest

from app.Map import RoomMaker
from app import Floor

class TestRoomMaker(unittest.TestCase):
    def test_it_should_make_a_room(self):
        rooms = []
        map = {
            'tiles': [[ None for i in range(80) ] for j in range(20) ],
            'size': [80, 20]
        }
        room_corner = (4, 4)
        room_size = (5, 5)

        r = RoomMaker()
        map = r.addRoom(map, room_corner, room_size)

        assert type(map['tiles'][8][8]) == Floor

    def test_it_should_not_add_a_room_off_the_edge_of_the_map(self):
        rooms = []
        map = {
            'tiles': [[ None for i in range(80) ] for j in range(20) ],
            'size': [80, 20]
        }
        room_corner = (80, 20)
        room_size = (5, 5)

        r = RoomMaker()

        with self.assertRaises(Exception) as context:
            r.addRoom(map, room_corner, room_size)
