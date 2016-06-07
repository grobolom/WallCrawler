import app
from app.monsters import Rat

class TestRat:
    def test_it_should_move_around(self):
        sut = Rat(position = [0, 0])
        map = {
            'tiles': [[ app.Floor(), app.Floor() ]],
            'size': [2, 1],
            'objects': [],
        }
        action = sut.getAction(map)
        expected = {
            'name': 'MOVE',
            'target': sut,
            'to': [1, 0],
        }

        assert action == expected
