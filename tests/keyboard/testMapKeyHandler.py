import app
from app.keyboard import MapKeyHandler

class TestMapKeyHandler:
    def test_it_should_try_to_move_the_character_up(self):
        key = 'k'
        state = {
            'character': app.Character({'x': 1, 'y': 1})
        }

        expected = {
            'name': 'MOVE_CHARACTER',
            'to': [1, 0]
        }

        assert expected == MapKeyHandler().getAction(key, state)
