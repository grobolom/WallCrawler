class GameOver:
    def reduce(self, state, action):
        new_state = state

        if action['name'] == 'GAME_OVER' or \
            self.hasNoMonsters(state['objects']) or \
            self.characterDead(state['character']): 
            new_state['game_over'] = True

        return new_state

    def hasNoMonsters(self, objects):
        for o in objects:
            if o.type == 'monster':
                return False
        return True

    def characterDead(self, character):
        return character.hp <= 0
