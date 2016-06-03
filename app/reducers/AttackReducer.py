class AttackReducer:
    def reduce(self, action, state):
        if action['name'] != 'ATTACK_CHARACTER':
            return state

        new_state = state
        new_state['objects'][0].hp -= 1

        return new_state
