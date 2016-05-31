import app
from app.reducers import CharacterMover

class TestCharacterMover:
    def test_it_should_move_the_character_to_a_target_square(self):
        action = {
            'name': 'MOVE_CHARACTER',
            'to': [1, 0]
        }

        state = {
            'character': {
                'position': [0, 0],
            },
            'map': {
                'tiles': [[ app.Floor(), app.Floor() ]],
                'size': [2, 0],
            },
        }

        reducer = CharacterMover()
        new_state = reducer.reduce(state, action)

        assert new_state['character']['position'] == [1, 0]
