class ViewSwitcher:
    def reduce(self, state, action):
        new_state = state

        if action['name'] == 'SWITCH_VIEW':
            new_state['view'] = action['to']

        return new_state
