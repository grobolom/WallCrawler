import app
from app.Map import RandomRoomMaker

class TestRandomRoomMaker:
    def test_it_should_make_a_room_of_random_size(self):
        sut = RandomRoomMaker()

        result = sut.getRandomRoom(5, 30)

        assert result[0] >= 5 and result[0] <= 30
        assert result[1] >= 5 and result[1] <= 30