import app
from app.Map import RandomRoomMaker

class TestRandomRoomMaker:
    def test_it_should_make_a_room_of_random_size(self):
        sut = RandomRoomMaker()

        result = sut.getRandomRoom(5, 30)

        assert result[0] >= 5  and result[0] <= 30 or \
               result[0] <= -5 and result[0] >= -30

        assert result[1] >= 5  and result[1] <= 30 or \
               result[1] <= -5 and result[1] >= -30

    def test_it_should_get_room_sizes_both_positive_and_negative(self):
        sut = RandomRoomMaker()

        result = sut.getPossibleRoomSizes(5, 30)
        expected = range(5, 30) + range(-5, -30, -1)

        assert result == expected
