class DeadMonsterCleaner:
    def reduce(self, state, action):
        new_state = state

        objects = new_state['objects']
        character = new_state['character']

        gained_xp = self.getGainedExp(objects)

        character.xp += gained_xp

        new_objects = [
            o for o in objects if not (o.type == 'monster' and o.isDead())
        ]

        new_state['objects'] = new_objects
        new_state['character'] = character

        return new_state

    def getGainedExp(self, objects):
        xp = 0
        for o in objects:
            if o.type == 'monster' and o.isDead():
                xp += o.xp
        return xp
