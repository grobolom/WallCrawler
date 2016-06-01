import app
from app.reducers import CharacterMover

class TestCharacterMover:
    def test_it_should_move_the_character_to_a_target_square(self):
        action = {
            'name': 'MOVE_CHARACTER',
            'to': [1, 0]
        }

        state = {
            'character': app.Character({'x': 0, 'y': 0 }),
            'map': {
                'tiles': [[ app.Floor(), app.Floor() ]],
                'size': [2, 1],
            },
        }

        reducer = CharacterMover()
        new_state = reducer.reduce(state, action)

        assert new_state['character'].x == 1
        assert new_state['character'].y == 0

    def test_it_should_not_move_the_character_into_a_wall(self):
        action = {
            'name': 'MOVE_CHARACTER',
            'to': [1, 0]
        }

        state = {
            'character': app.Character({'x': 0, 'y': 0 }),
            'map': {
                'tiles': [[ app.Floor(), app.Wall() ]],
                'size': [2, 1],
            },
        }

        reducer = CharacterMover()
        new_state = reducer.reduce(state, action)

        assert new_state['character'].x == 0
        assert new_state['character'].y == 0

    def test_it_should_not_move_the_character_out_of_bounds(self):
        action = {
            'name': 'MOVE_CHARACTER',
            'to': [5, 0]
        }

        state = {
            'character': app.Character({'x': 0, 'y': 0 }),
            'map': {
                'tiles': [[ app.Floor(), app.Wall() ]],
                'size': [2, 1],
            },
        }

        reducer = CharacterMover()
        new_state = reducer.reduce(state, action)

        assert new_state['character'].x == 0
        assert new_state['character'].y == 0
