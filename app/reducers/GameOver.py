class GameOver:
    def reduce(self, state, action):
        new_state = state
        if action['name'] == 'GAME_OVER':
            new_state['game_over'] = True
        return new_state
