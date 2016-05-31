class PositionReducer:
    def reduce(self, state, action):
        new_state = state

        character = state['character']
        position = [character.x, character.y]

        objects = []
        if 'objects' in state:
            objects = state['objects']

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

        character.x = position[0]
        character.y = position[1]

        objects = [x for x in objects if x.type != 'char' ]
        objects.append(character)

        new_state['objects'] = objects

        return new_state
