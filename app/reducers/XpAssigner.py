class XpAssigner:
    def reduce(self, state, action):
        new_state = state

        xp = 0
        for o in state['objects']:
            if o.type == 'monster' and o.isDead():
                xp += o.xp

        new_state['character'].xp += xp

        return new_state
