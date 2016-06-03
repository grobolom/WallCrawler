class DeadMonsterCleaner:
    def reduce(self, state, action):
        new_state = state

        state['objects'] = []

        return state
