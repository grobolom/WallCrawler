from app.Map import RoomMaker
from app import Tile

class TestRoomMaker:
    def test_it_should_make_a_room(self):
        rooms = []
        map = {
            'tiles': [[ None for i in range(80) ] for j in range(20) ],
            'size': [80, 20]
        }
        room_corner = (4, 10)
        room_size = (5, 5)

        r = RoomMaker()
        map = r.addRoom(map, room_corner, room_size)

        assert type(map['tiles'][15][9]) == Tile
