import app
from app.monsters import Rat
from app import Character

class TestRat:
    def test_it_should_move_around(self):
        sut = Rat(position = [0, 0], id = 3)
        state = {
            'map': {
                'tiles': [[ app.Floor(), app.Floor() ]],
                'size': [2, 1],
            },
            'objects': [],
            'character': Character(position=[0, 0]),
        }
        action = sut.getAction(state)
        expected = {
            'name': 'MOVE',
            'target': sut.id,
            'to': [1, 0],
        }

        assert action == expected
