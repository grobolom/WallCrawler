class CharacterShovel:
    def reduce(self, state, action):
        new_state = state

        objects = new_state['objects']
        objects = [e for e in objects if e.type != 'char']
        objects.append(state['character'])

        new_state['objects'] = objects

        return new_state
