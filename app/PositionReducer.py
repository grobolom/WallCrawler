class PositionReducer:
    def reduce(self, state, action):
        new_state = state

        character = state['character']
        position = [character.x, character.y]

        map_size = state['map']['size']

        name = action['name']
        if name == 'MOVE_UP':
            position[1] = max(0, position[1] - 1)
        if name == 'MOVE_DOWN':
            position[1] = min(map_size[1] - 1, position[1] + 1)

        if name == 'MOVE_LEFT':
            position[0] = max(0, position[0] - 1)
        if name == 'MOVE_RIGHT':
            position[0] = min(map_size[0] - 1, position[0] + 1)

        return new_state
