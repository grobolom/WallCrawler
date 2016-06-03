class PositionReducer:
    def reduce(self, state, action):
        new_state = state

        character = state['character']
        position = character.position

        map_size = state['map']['size']

        name = action['name']
        if name == 'MOVE_CHARACTER':
            position = action['to']

        character.position = position

        new_state['character'] = character

        return new_state
