class AttackReducer:
    def reduce(self, action, state):
        if action['name'] != 'ATTACK_CHARACTER':
            return state
        return state
