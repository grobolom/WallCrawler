class CharacterShovel:
    def reduce(self, state, action):
        new_state = state
        state['objects'].append(state['character'])
        return new_state
