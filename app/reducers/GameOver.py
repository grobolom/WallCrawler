class GameOver:
    def reduce(self, state, action):
        new_state = state

        if action['name'] == 'GAME_OVER':
            new_state['game_over'] = True

        if self.hasNoMonsters(state['objects']):
            new_state['game_over'] = True

        return new_state

    def hasNoMonsters(self, objects):
        for o in objects:
            if o.type == 'monster':
                return False
        return True
