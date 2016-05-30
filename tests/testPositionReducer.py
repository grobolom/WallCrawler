from app import PositionReducer

class TestPositionReducer:
    def test_it_should_move_up(self):
        reducer = PositionReducer()
        state = {
            'character_position': [5, 5],
            'map_size': [6, 6],
        }
        action = { 'name': 'MOVE_UP' }
        new_state = reducer.reduce(state, action)

        assert new_state['character_position'] == [5, 4]

    def test_it_should_not_move_past_the_top_of_the_map(self):
        reducer = PositionReducer()
        state = {
            'character_position': [0, 0],
            'map_size': [6, 6],
        }
        action = { 'name': 'MOVE_UP' }
        new_state = reducer.reduce(state, action)

        assert new_state['character_position'] == [0, 0]

    def test_it_should_not_move_past_the_bottom_of_the_map(self):
        reducer = PositionReducer()
        state = {
            'character_position': [5, 5],
            'map_size': [6, 6],
        }
        action = { 'name': 'MOVE_DOWN' }
        new_state = reducer.reduce(state, action)

        assert new_state['character_position'] == [5, 5]


    def test_it_should_not_move_past_the_left_of_the_map(self):
        reducer = PositionReducer()
        state = {
            'character_position': [0, 0],
            'map_size': [6, 6],
        }
        action = { 'name': 'MOVE_LEFT' }
        new_state = reducer.reduce(state, action)

        assert new_state['character_position'] == [0, 0]

    def test_it_should_not_move_past_the_right_of_the_map(self):
        reducer = PositionReducer()
        state = {
            'character_position': [5, 5],
            'map_size': [6, 6],
        }
        action = { 'name': 'MOVE_RIGHT' }
        new_state = reducer.reduce(state, action)

        assert new_state['character_position'] == [5, 5]
