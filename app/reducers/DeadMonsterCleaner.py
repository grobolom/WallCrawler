class DeadMonsterCleaner:
    def reduce(self, state, action):
        new_state = state

        objects = new_state['objects']
        new_objects = [ o for o in objects if o.hp > 0 ]
        new_state['objects'] = new_objects

        return new_state
